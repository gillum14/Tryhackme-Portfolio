-- Database SQL Basics
-- This file supports my SQL notes by demonstrating basic queries
-- using a small cafe orders example.

CREATE TABLE cafe_orders (
    order_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    item_ordered TEXT,
    category TEXT,
    price REAL,
    order_status TEXT
);

INSERT INTO cafe_orders (order_id, customer_name, item_ordered, category, price, order_status)
VALUES
    (1, 'Alex', 'Coffee', 'Drink', 3.50, 'Completed'),
    (2, 'Jordan', 'Tea', 'Drink', 2.75, 'Completed'),
    (3, 'Sam', 'Blueberry Muffin', 'Food', 4.25, 'Pending'),
    (4, 'Taylor', 'Latte', 'Drink', 5.00, 'Completed'),
    (5, 'Morgan', 'Bagel', 'Food', 3.25, 'Cancelled'),
    (6, 'Casey', 'Iced Coffee', 'Drink', 4.50, 'Pending');

-- SELECT chooses which columns to display.
SELECT customer_name, item_ordered, price
FROM cafe_orders;

-- WHERE filters records based on a condition.
SELECT *
FROM cafe_orders
WHERE order_status = 'Pending';

-- ORDER BY sorts the results.
SELECT customer_name, item_ordered, price
FROM cafe_orders
ORDER BY price DESC;

-- This query shows only drink orders.
SELECT customer_name, item_ordered, category
FROM cafe_orders
WHERE category = 'Drink';

-- This query finds completed orders over $4.00.
SELECT customer_name, item_ordered, price, order_status
FROM cafe_orders
WHERE order_status = 'Completed'
AND price > 4.00;

-- This query counts how many orders exist in each status.
SELECT order_status, COUNT(*) AS total_orders
FROM cafe_orders
GROUP BY order_status;
