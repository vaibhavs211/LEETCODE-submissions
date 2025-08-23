SELECT o.id,
       CASE
         WHEN MOD(o.id,2) = 1 THEN 
              COALESCE( (SELECT s.student FROM seat s WHERE s.id = o.id+1),
                        o.student )
         ELSE 
              (SELECT s.student FROM seat s WHERE s.id = o.id-1)
       END AS student
FROM seat o;
