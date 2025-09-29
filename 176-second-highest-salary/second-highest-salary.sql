# Write your MySQL query statement below
SELECT MAX(salary) AS secondhighestsalary
FROM employee 
WHERE salary < (SELECT MAX(salary) FROM employee)