SELECT customer_id, TIMESTAMPDIFF(DAY, MIN(order_date), MAX(order_date)) AS purchase_interval
FROM orders
GROUP BY customer_id
HAVING COUNT(*) > 1
ORDER BY purchase_interval DESC;
