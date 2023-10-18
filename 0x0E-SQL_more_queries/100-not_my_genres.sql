-- List all genres not linked to the show "Dexter"

SELECT DISTINCT tv_genres.name
FROM tv_genres
    INNER JOIN (
        SELECT tv_show_genres.genre_id
        FROM tv_show_genres
            INNER JOIN tv_shows
                ON tv_show_genres.show_id = tv_shows.id
        WHERE tv_shows.title <> "Dexter"
    ) AS t
        ON t.genre_id = tv_genres.id
;
