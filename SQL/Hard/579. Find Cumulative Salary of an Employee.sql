# write your mysql query statement belowSELECT   id, 
         month, 
         salary 
FROM     ( 
                  SELECT   id, 
                           month, 
                           sum(salary) OVER (partition BY id ORDER BY month ASC rows BETWEEN 2 PRECEDING AND      CURRENT row) AS salary ,
                           row_number() OVER (partition BY id ORDER BY month DESC)                                             AS ranking
                  FROM     employee) tmp 
WHERE    ranking != 1 
ORDER BY id, 
         month DESC