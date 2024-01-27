SELECT name FROM people WHERE id IN (SELECT person_id FROM stars JOIN movies WHERE movies.id = stars.movie_id AND movies.title ='Toy Story');
