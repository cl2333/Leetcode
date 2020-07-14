/* Write your T-SQL query statement below */ 
SELECT email 
FROM   person 
GROUP  BY email 
HAVING Count(email) > 1; 