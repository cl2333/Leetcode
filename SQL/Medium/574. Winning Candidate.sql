# write your mysql query statement below 

WITH cte AS 
( 
         SELECT   candidateid, 
                  count(*) AS counting 
         FROM     vote 
         GROUP BY candidateid )SELECT NAME 
FROM   ( 
              SELECT candidateid 
              FROM   cte 
              WHERE  counting = 
                     ( 
                            SELECT Max(counting) 
                            FROM   cte)) v 
JOIN   candidate c 
ON     v.candidateid = c.id


select name
from candidate c join vote v on c.id = v.candidateid
group by name
order by count(*) desc
limit 1