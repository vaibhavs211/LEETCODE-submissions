# Write your MySQL query statement below
SELECT c.category, COALESCE(a.cnt, 0) AS accounts_count
FROM (
    SELECT 'Low Salary' AS category
    UNION ALL
    SELECT 'Average Salary'
    UNION ALL
    SELECT 'High Salary'
) c
LEFT JOIN (
    SELECT CASE 
             WHEN income < 20000 THEN 'Low Salary'
             WHEN income > 50000 THEN 'High Salary'
             ELSE 'Average Salary'
           END AS category,
           COUNT(*) AS cnt
    FROM accounts
    GROUP BY category
) a
ON c.category = a.category;
