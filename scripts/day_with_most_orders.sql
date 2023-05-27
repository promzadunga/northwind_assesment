SELECT DAYNAME(order_date) AS day_of_week, COUNT(*) AS order_count
FROM orders
GROUP BY day_of_week
ORDER BY order_count DESC
LIMIT 1;
