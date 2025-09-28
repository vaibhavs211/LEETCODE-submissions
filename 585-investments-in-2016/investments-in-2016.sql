# Write your MySQL query statement below
# Write your MySQL query statement below
SELECT ROUND(SUM(a.tiv_2016),2) AS tiv_2016 FROM insurance a
WHERE EXISTS (SELECT pid FROM insurance b WHERE (a.tiv_2015 = b.tiv_2015 AND a.pid<>b.pid))
AND NOT EXISTS (SELECT pid FROM insurance c WHERE a.pid<>c.pid AND a.lat=c.lat AND a.lon = c.lon)