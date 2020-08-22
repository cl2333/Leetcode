# Write your MySQL query statement below 
SELECT x, 
       y, 
       z, 
       CASE 
         WHEN ( x + y <= z 
                 OR x + z <= y 
                 OR y + z <= x ) THEN 'No' 
         ELSE 'Yes' 
       end AS triangle 
FROM   triangle 