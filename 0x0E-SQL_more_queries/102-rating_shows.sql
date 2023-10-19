-- List all shows and their total rating

SELECT title, SUM(rate) AS rating
FROM tv_shows
    INNER JOIN tv_show_ratings AS r
        ON tv_shows.id = r.show_id
GROUP BY title
ORDER BY rating DESC;
