/* Write your T-SQL query statement below */ 
SELECT q.id, 
       q.year, 
       COALESCE(npv, 0) AS NPV 
FROM   queries q 
       LEFT JOIN npv n 
              ON q.id = n.id 
                 AND q.year = n.year 