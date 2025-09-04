# Write your MySQL query statement below
SELECT q1.person_name 
FROM queue q1, queue q2
WHERE q1.turn>=q2.turn
GROUP BY q1.person_id
HAVING SUM(q2.weight) <= 1000
ORDER BY SUM(q2.weight) DESC
LIMIT 1;