# Write your MySQL query statement below 
SELECT customer_id 
FROM   customer 
GROUP  BY customer_id 
HAVING Count(DISTINCT product_key) = (SELECT Count(*) 
                                      FROM   product) 