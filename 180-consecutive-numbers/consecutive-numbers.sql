# Write your MySQL query statement below
SELECT DISTINCT(s1.num) AS consecutivenums
FROM logs s1, logs s2, logs s3
WHERE s2.id = s1.id+1
AND s3.id = s1.id+2
AND s1.num = s2.num AND s2.num = s3.num;