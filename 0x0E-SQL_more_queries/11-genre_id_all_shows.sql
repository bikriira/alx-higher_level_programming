-- A script that lists all shows contained in the database hbtn_0d_tvshows.

-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- If a show doesn’t have a genre, display NULL
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command


SELECT b.title, a.genre_id
	FROM tv_show_genres a
	RIGHT JOIN tv_shows b
		ON a.show_id = b.id
	ORDER BY b.title, a.genre_id;
