/* Write your T-SQL query statement below */

SELECT DISTINCT l3.num AS ConsecutiveNums 
FROM   ( logs l1 
         JOIN logs l2 
           ON l2.id - 1 = l1.id 
         JOIN logs l3 
           ON l3.id - 1 = l2.id 
              AND l3.id - 2 = l1.id ) 
WHERE  l1.num = l2.num 
       AND l2.num = l3.num 
       AND l3.num = l1.num 


-- using lead and lag
SELECT DISTINCT( a.num ) AS ConsecutiveNums 
FROM   (SELECT num, 
               Lag(num) 
                 OVER () AS above, 
               Lead(num) 
                 OVER () AS below 
        FROM   logs) a 
WHERE  num = above 
       AND num = below 