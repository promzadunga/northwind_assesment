/* we first need to modify the fk constrain to handle violation error so that records removed from orders can also be removed from orders_details*/

ALTER TABLE order_details
DROP FOREIGN KEY fk_order_details__orders;

ALTER TABLE order_details
ADD CONSTRAINT fk_order_details__orders
FOREIGN KEY (order_id)
REFERENCES orders(id)
ON DELETE CASCADE;

/* This is the query that removes the duplicates and it is always recommended to run such queries in test environment first to avoid unintended deletion of data*/

DELETE t1
FROM orders t1
JOIN (
    SELECT customer_id, MAX(order_date) AS max_order_date
    FROM orders
    GROUP BY customer_id
    HAVING COUNT(*) > 1
) t2 ON t1.customer_id = t2.customer_id AND t1.order_date < t2.max_order_date;
