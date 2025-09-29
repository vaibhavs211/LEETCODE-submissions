# Write your MySQL query statement below
WITH ranked AS (
    SELECT id,email,
        ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS rn
    FROM person
)
DELETE FROM person 
WHERE id IN (SELECT id FROM ranked WHERE rn>1);