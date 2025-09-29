# Write your MySQL query statement below
# Write your MySQL query statement below
SELECT p.product_name, SUM(o.unit) AS unit
FROM products p JOIN orders o
ON p.product_id = o.product_id
WHERE DATE_FORMAT(o.order_date, '%m-%y') = '02-20'
GROUP BY p.product_id
HAVING SUM(o.unit) >= 100