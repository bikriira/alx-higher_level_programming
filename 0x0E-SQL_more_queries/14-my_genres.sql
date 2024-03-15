-- Script Documentation:
-- This script lists all genres of the show "Dexter"
-- 		from the hbtn_0d_tvshows database.

-- SQL Query:
SELECT tv_genres.name
FROM tv_show_genres
INNER JOIN tv_genres
    ON tv_show_genres.genre_id = tv_genres.id
INNER JOIN tv_shows AS show_ref
    ON tv_show_genres.show_id = show_ref.id
WHERE show_ref.title = 'Dexter'
ORDER BY tv_genres.name;
