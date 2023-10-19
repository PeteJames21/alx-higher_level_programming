-- Display the total rating of all genres

SELECT tv_genres.name, SUM(r.rate) AS rating
FROM tv_show_ratings AS r
    LEFT JOIN tv_show_genres AS g
        ON g.show_id = r.show_id
    INNER JOIN tv_genres
        ON g.genre_id = tv_genres.id
GROUP BY tv_genres.name
ORDER BY rating DESC;
