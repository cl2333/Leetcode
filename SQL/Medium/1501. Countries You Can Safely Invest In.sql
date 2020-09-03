# write your mysql query statement below 

WITH cte AS 
( 
       SELECT c.NAME AS country, 
              duration 
       FROM   person p 
       JOIN   country c 
       ON     LEFT(p.phone_number,3) = c.country_code 
       JOIN   calls 
       ON     calls.caller_id = p.id 
       OR     calls.callee_id = p.id )SELECT   country 
FROM     cte 
GROUP BY country 
HAVING   Avg(duration) > 
         ( 
                SELECT Avg(duration) 
                FROM   cte)