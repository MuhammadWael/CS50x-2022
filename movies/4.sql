SELECT COUNT(title) FROM ratings,movies
WHERE movies.id = ratings.movie_id AND ratings.rating = 10.0;