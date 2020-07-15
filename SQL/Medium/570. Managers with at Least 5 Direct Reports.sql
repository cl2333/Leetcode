/* Write your T-SQL query statement below */ 
SELECT DISTINCT e1.NAME 
FROM   (SELECT NAME, 
               id 
        FROM   employee) e1 
       LEFT JOIN (SELECT managerid, 
                         Count(*) AS freq 
                  FROM   employee 
                  GROUP  BY managerid) e2 
              ON e1.id = e2.managerid 
WHERE  e2.freq >= 5; 


SELECT NAME 
FROM   employee 
WHERE  id IN (SELECT managerid 
              FROM   employee 
              GROUP  BY managerid 
              HAVING Count(*) >= 5) 