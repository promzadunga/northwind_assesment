from pyspark.sql import SparkSession
from pyspark.sql.functions import col, datediff, expr
from pyspark.sql.window import Window
from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import VectorAssembler
from datetime import datetime, timedelta
from pymongo import MongoClient



# Create a SparkSession
spark = SparkSession.builder \
    .appName("Northwind Orders Prediction") \
    .config("spark.jars", "/home/proman/mysql-connector-java.jar") \
    .getOrCreate()

# Configure MySQL connection properties
mysql_url = "jdbc:mysql://localhost:3306/northwind"
mysql_properties = {
    "user": "root",
    "password": "mysql_password",
    "driver": "com.mysql.jdbc.Driver"
}

# Read the customers and orders tables from MySQL
customers_df = spark.read.jdbc(mysql_url, "customers", properties=mysql_properties)
orders_df = spark.read.jdbc(mysql_url, "orders", properties=mysql_properties)

customers_df = customers_df.na.fill(None)
orders_df = orders_df.na.fill(None)

# Convert date columns in orders_df DataFrame
orders_df = orders_df.withColumn("order_date", to_date(col("order_date"), "yyyy-MM-dd")) \
                     .withColumn("shipped_date", to_date(col("shipped_date"), "yyyy-MM-dd")) \
                     .withColumn("paid_date", to_date(col("paid_date"), "yyyy-MM-dd"))

# Calculating the days since the last order for each customer
window_spec = Window.partitionBy("customer_id").orderBy(col("order_date").desc())
customers_df = customers_df.withColumn("days_since_last_order", datediff(col("order_date"), expr("LAG(order_date) OVER {}".format(window_spec)))))

# Selecting relevant columns for training
training_data = customers_df.select("customer_id", "days_since_last_order", "order_date")

# Droping rows with null values in the training data
training_data = training_data.dropna()


# Preparing the feature vector assembler
assembler = VectorAssembler(inputCols=["days_since_last_order"], outputCol="features")

# Transforming the training data using the feature vector assembler
training_data = assembler.transform(training_data)

# Train a linear regression model
lr = LinearRegression(featuresCol="features", labelCol="order_date")
model = lr.fit(training_data)

# Select a specific customer for prediction
customer_id = 1
customer_data = customers_df.filter(col("customer_id") == customer_id).select("customer_id", "days_since_last_order")

# Transform the customer data using the feature vector assembler
customer_data = assembler.transform(customer_data)

# Make predictions for the customer
predictions = model.transform(customer_data)

# Select the predicted next order date
predicted_order_date = predictions.select("prediction").first()[0]

# Print the predicted next order date
print("Predicted next order date for customer {}: {}".format(customer_id, predicted_order_date))


current_date = datetime.now()
next_week = current_date + timedelta(days=7)

predicted_customers = predictions.filter(predictions.prediction <= next_week)


# Configure MongoDB connection
mongo_uri = "mongodb://localhost:27017/"
mongo_db = "northwind"
mongo_collection = "predicted_orders"

# Connect to the MongoDB server
client = MongoClient(mongo_uri)

# Connect to the database and collection
db = client[mongo_db]
collection = db[mongo_collection]


# Convert the predicted customers DataFrame to a list of dictionaries
predicted_customers_data = predicted_customers.toPandas().to_dict(orient="records")

# Insert the predicted customers into the MongoDB collection
collection.insert_many(predicted_customers_data)

# Close the MongoDB connection
client.close()

