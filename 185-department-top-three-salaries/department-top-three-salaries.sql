# Write your MySQL query statement below
SELECT d.name AS department,
       e.name AS employee,
       e.salary
FROM (
    SELECT e.*,
           DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS rnk
    FROM Employee e
) e
JOIN Department d
  ON e.departmentId = d.id
WHERE e.rnk <= 3;
