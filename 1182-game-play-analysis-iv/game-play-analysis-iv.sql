# Write your MySQL query statement below
SELECT 
    ROUND(
        (COUNT(DISTINCT a.player_id)) / 
        (SELECT COUNT(DISTINCT player_id) FROM activity)
        , 2
    ) AS fraction
    FROM activity a
    JOIN (SELECT player_id, MIN(event_date) AS first
            FROM activity 
            GROUP BY player_id
    ) b
    ON a.player_id = b.player_id
    AND DATEDIFF(b.first, a.event_date) = -1;