SELECT HOUR(order_date) AS hour_of_day, COUNT(*) AS order_count
FROM orders
GROUP BY hour_of_day
ORDER BY order_count DESC
LIMIT 1;
