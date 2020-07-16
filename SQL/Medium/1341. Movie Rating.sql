# Write your MySQL query statement below 
(SELECT name AS results 
 FROM   movie_rating r 
        JOIN users u 
          ON r.user_id = u.user_id 
 GROUP  BY r.user_id 
 ORDER  BY Count(*) DESC, 
           name ASC 
 LIMIT  1) 
UNION 
(SELECT title AS results 
 FROM   movie_rating r 
        JOIN movies m 
          ON r.movie_id = m.movie_id 
 WHERE  Month(created_at) = 2 
 GROUP  BY r.movie_id 
 ORDER  BY Avg(rating) DESC, 
           title ASC 
 LIMIT  1) 