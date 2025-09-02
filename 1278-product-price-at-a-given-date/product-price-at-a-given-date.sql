/* Write your PL/SQL query statement below */
SELECT DISTINCT np1.product_id,
       COALESCE(np2.price, 10) AS price
FROM products np1
LEFT JOIN (
    SELECT p1.product_id, p1.new_price AS price
    FROM products p1
    WHERE p1.change_date = (
        SELECT MAX(p2.change_date)
        FROM products p2
        WHERE p1.product_id = p2.product_id
          AND p2.change_date <= TO_DATE('16-08-2019', 'DD-MM-YYYY')
    )
) np2
ON np1.product_id = np2.product_id;
