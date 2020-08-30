# # write your mysql query statement below 

WITH cte1 AS 
( 
         SELECT   activity, 
                  count(activity) AS counts 
         FROM     friends 
         GROUP BY activity ), cte2 AS 
( 
       SELECT max(counts) 
       FROM   cte1 
       UNION ALL 
       SELECT min(counts) 
       FROM   cte1 )SELECT activity 
FROM   cte1 
WHERE  counts NOT IN 
       ( 
              SELECT * 
              FROM   cte2)