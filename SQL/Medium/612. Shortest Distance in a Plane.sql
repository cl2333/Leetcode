# Write your MySQL query statement below 
SELECT 
Round(Min(Sqrt(( a.x - b.x ) * ( a.x - b.x ) + ( a.y - b.y ) * ( a.y - b.y ))), 2) AS shortest 
FROM   point_2d a 
       JOIN point_2d b 
         ON ( a.x != b.x 
               OR a.y != b.y ) 