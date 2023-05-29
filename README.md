# northwind_assesment


1. Script 1 - Create a docker script to start an existing mysql docker
instance.
- placed under scrips folder named docker-compose.yml run the command below to start mysql provided that docker and docker compose are installed and the command should be ran in the folder where this file is placed
- docker-compose up -d
2. Script 2 - Create a script to import the orders details information into
the mysql database.
- placed under scripts named import_into_orders_details.sql
3. Script 3 - Write a Scala or Python Spark or scala script that would do the
following:
a. Predict the next order date for a customer, based on his purchase
patterns.
b. Only customers predicted to buying products in the next week( 7
days) must be placed in the mongo database.

placed under scrpits named perdict_customers_next_order.py


4. Explain under which conditions you would use MySQL and Mongo?
- Structured Data: If the data has a fixed schema and requires strict adherence to relationships between tables, MySQL is a good choice. also if the data is more structured and it is not large volumes of data that we are storing then Mysql will be more suitable
- Flexible and Unstructured Data: MongoDB. It allows flexible schema design, enabling easy storage and retrieval of diverse data formats. high throughput and large-scale data storage, Real-time Analytics. if we are processing large volums of data and want to process it in real-time then MongoDB is a great choice.
6. Explain your choice in context of the CAP Theorem?
-MySQL places a strong emphasis on consistency (C) and partition tolerance (P). It is an ACID-compliant database that prioritizes data consistency and integrity. In the event of a network partition or failure, MySQL uses techniques like replication and clustering to ensure data availability (A) and partition tolerance. However, achieving high availability in MySQL can sometimes require trade-offs in terms of response time and system complexity so if we want more consistent data and we can afford to have down time in our system then we can use mysql as it prioritizes C and P of the CAP theorem and compromises A.

- MongoDB, being a NoSQL database,it is designed with a focus on availability (A) and partition tolerance (P). It provides high availability by default through its distributed architecture and support for horizontal scalability. In the case of network partitions or failures, MongoDB prioritizes maintaining availability and responsiveness. MongoDB sacrifices some level of data consistency (C) to achieve higher availability and partition tolerance. It offers eventual consistency, where updates to the database propagate asynchronously, allowing for more flexible and scalable distributed systems, so if we want HA (High Availability) in our system that we can not afford down-time then MongoDB will be the right choice of selection for our design
- 
8. Explain and draw a diagram on how you would design the above

        
        |    Azure VMs     |
        | (MySQL Database) |
      
                 |
       
        | Azure Cosmos DB |
        |  (MongoDB API)  |
        
                 |
        
        |  Azure Databricks  |
       
                 |
      
        | Azure Data Factory|
        
                 |
        
        |   Azure Functions  |
        
                 |
       
        |   Azure Logic Apps |
       
                 |
        
        |  Azure Event Grid |
        +--------+--------+
                 |
        
        |  Azure Monitor  |
        
                 |
        
        | Azure Blob Storage |
      
                 |
       
        |   Azure Networking |
       
                 |
       
        | Azure Load Balancer |
        
                 |
       
        |Azure Cosmos DB  |
        | Multi-Region Replication|
       


a. What technologies would you use in the cloud stack?
Azure Virtual Machines:
Set up one or more virtual machines to host the MySQL database. we can choose the appropriate VM size based on our workload and performance requirements.
Azure Cosmos DB (MongoDB API):

Use Azure Cosmos DB with the MongoDB API to host the MongoDB database. Cosmos DB is a globally distributed database service that provides automatic scaling, high availability, and low latency.
Azure Databricks:

Utilize Azure Databricks for big data processing, analytics, and machine learning tasks. we can extract insights from our data and perform data transformations using Spark-based workflows.
Azure Data Factory:

Employ Azure Data Factory to orchestrate data movement and ETL (Extract, Transform, Load) processes. It allows us to create data pipelines to ingest data from various sources into our databases.
Azure Functions:

Use Azure Functions to implement serverless compute capabilities. we can leverage functions for tasks like data processing, triggering events, and integrating with other Azure services.
Azure Logic Apps:

Implement Azure Logic Apps for workflow automation and integration. It enables we to connect different systems and services, such as triggering actions based on specific events or conditions.
Azure Event Grid:

Utilize Azure Event Grid for event-driven architecture. we can publish and consume events across different Azure services, enabling real-time reactions and event-based communication.
Azure Monitor:

Employ Azure Monitor to gain insights into the health and performance of your resources. Monitor provides centralized monitoring, diagnostics, and analytics for your Azure environment.
Azure Blob Storage:

Use Azure Blob Storage to store and access unstructured data such as files and media. It offers scalable and durable storage for your application's data.
Azure Networking:

Configure Azure Virtual Networks, Subnets, and Network Security Groups (NSGs) to securely isolate and connect our resources. we can define network rules and access controls to protect our data.
Azure Load Balancer:

Implement Azure Load Balancer to distribute incoming network traffic across multiple VMs or instances hosting the MySQL database, ensuring high availability and scalability.
Azure Cosmos DB Multi-Region Replication:

Enable multi-region replication in Azure Cosmos DB to replicate our MongoDB data across different regions, ensuring high availability and disaster recovery.

b. How would you move data from on premises (MySQL) to the cloud.

Provision Azure Resources:

Set up the necessary Azure resources, such as Azure Virtual Machines, Azure Cosmos DB, Azure Networking components, and any other required services, based on our architectural design.
Establish Connectivity:

Ensure that there is network connectivity between our on-premises environment and Azure. This can be achieved by setting up a secure VPN connection, Azure ExpressRoute, or using Azure Virtual Network gateways.
Backup and Restore Method:

Determine the method we will use to move the data from MySQL on-premises to Azure. One common approach is to take a backup of the MySQL database and restore it in Azure.
Export and Import Data:

Export the data from the on-premises MySQL database to a compatible format that can be imported into Azure. we can use MySQL utilities like mysqldump or third-party tools to export the data as SQL scripts or in a suitable intermediate format like CSV.
Data Transfer Mechanisms:

Depending on the size and complexity of the data, we can choose the appropriate mechanism to transfer the data to Azure. Some options include:

Azure Data Migration Service: Azure provides a Data Migration Service that supports migrating databases from various sources, including on-premises MySQL databases, to Azure. It simplifies the migration process and handles the data transfer and schema conversion.

Azure Database Migration Service: we can use the Azure Database Migration Service to migrate our on-premises MySQL database to Azure Database for MySQL. It offers a guided workflow, minimal downtime, and automatic schema and data migration.

Azure Data Factory: Utilize Azure Data Factory to create data pipelines and workflows for moving data from on-premises to Azure. we can define data copy activities, transformations, and scheduling to orchestrate the movement of data.

Perform Data Import:

Import the exported data into the target Azure database service, such as Azure Cosmos DB (MongoDB API) or Azure Database for MySQL. we can Follow the appropriate documentation and tools provided by Azure to perform the data import.
Validate and Test:

Once the data import is completed, we can verify the integrity and consistency of the migrated data in Azure. Run tests and checks to ensure that the data has been transferred accurately and matches the source.
Decommission On-Premises Database:

If we no longer require the on-premises MySQL database,we can safely decommission it according to our organization's processes and procedures.


# Black Friday
On the day of Black Friday, you realize that you have a large number of orders,
explain how you would make changes to your data engineering architecture
to be more robust, scalable, reliable and real time.

1. What technologies would you use?
- Apache Kafka: Kafka is a distributed streaming platform that can handle high throughput and real-time data streams. It acts as a reliable and scalable message broker for handling the influx of orders.

- Apache Spark: Spark is a distributed data processing framework that provides fast and scalable data processing capabilities. It can handle large volumes of data and perform real-time analytics and transformations on the incoming order data.

-  Apache Hadoop: Hadoop is a distributed storage and processing framework that can handle large volumes of data. It provides a scalable and fault-tolerant storage layer for storing historical order data and performing batch processing.

- Apache Airflow: Airflow is a platform for programmatically authoring, scheduling, and monitoring workflows. It can be used to orchestrate the data processing pipeline, schedule tasks, and monitor their execution.

3. Why would you choose these technologies?
- Scalability: Apache Kafka, Apache Spark and Apache Hadoop are all designed to scale horizontally, allowing you to handle increased data volumes and processing demands on Black Friday.

- Real-time Processing: Kafka and Spark enable real-time data processing, allowing you to handle and analyze the incoming order data in near real-time.

- Fault Tolerance and Reliability: Kafka and Hadoop are all known for their fault tolerance and reliability features. They can handle hardware failures, provide data replication, and ensure data durability

- Workflow Orchestration: Apache Airflow allows you to create and manage complex workflows, ensuring the seamless execution of data processing tasks and providing monitoring and error handling capabilities.
- 
5. What data patterns would you use ?

- Event-driven Architecture: Implement an event-driven architecture using Apache Kafka. Orders can be published as events to Kafka topics, enabling real-time processing and analysis.

- Stream Processing: Utilize Apache Spark's streaming capabilities to process the order data in real-time, perform aggregations, enrichments, and apply business rules.

- Microservices Architecture: Decompose the system into microservices that can independently handle different aspects of order processing, such as inventory management, payment processing, and shipping.

- Caching: Use in-memory caching technologies like Redis or Apache Ignite to cache frequently accessed data, such as customer information, product details, and pricing information, to improve response times and reduce database load.

- Batch Processing: Utilize Apache Hadoop to process historical order data and generate insights and reports. This can help in analyzing trends, customer behavior, and planning for future Black Friday events.

- Monitoring and Alerting: Implement monitoring and alerting mechanisms to detect anomalies, performance bottlenecks, and failures in the data processing pipeline. Tools like Grafana can be used for monitoring and visualization.

# Order Analysis
Please provide scripts and results for the following:
1. Which day of the week has the most orders?
- placed under scripts named day_with_most_orders.sql
3. Which time of the day do people order the most?
- placed under scripts named time_with_most_orders.sql
5. Which order does the user buy first most of the time?
- placed under scripts named order_bought_first.sql
7. What is the time interval that a user tends to purchase again?
- placed under scripts named purchase_time_interval_by_user.sql
9. Write a mysql script on how to delete the duplicate orders, of the latest date, please explain the script in detail?
- placed under scripts named delete_duplicate_orders.sql explanation put in a form of comments within the script
