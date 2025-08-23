-- Users with max number of ratings
(
    SELECT MIN(u.name) AS results
    FROM users u
    WHERE u.user_id IN (
        SELECT user_id
        FROM (
            SELECT user_id, COUNT(*) AS rating_count
            FROM movierating
            GROUP BY user_id
        ) t
        WHERE rating_count = (
            SELECT MAX(COUNT(*))
            FROM movierating
            GROUP BY user_id
        )
    )
)
UNION ALL
(
    SELECT MIN(m.title) AS results
    FROM movies m
    WHERE m.movie_id IN (
        SELECT movie_id
        FROM (
            SELECT movie_id, AVG(rating) AS avg_rating
            FROM movierating
            WHERE TO_CHAR(created_at, 'MM-YYYY') = '02-2020'
            GROUP BY movie_id
        ) t
        WHERE avg_rating = (
            SELECT MAX(AVG(rating))
            FROM movierating
            WHERE TO_CHAR(created_at, 'MM-YYYY') = '02-2020'
            GROUP BY movie_id
        )
    )
);
