# write your mysql query statement belowSELECT id, 
       company, 
       salary 
FROM   ( 
                SELECT   id, 
                         company, 
                         salary, 
                         Count(*) OVER (partition BY company)                    AS total, 
                         Row_number() OVER(partition BY company ORDER BY salary) AS ranking, 
                         Round(Count(*) OVER (partition BY company)/2, 0)        AS med 
                FROM     employee) tmp 
WHERE  ( 
              total%2 = 0 
       AND    ranking IN (med, 
                          med+1)) 
OR     ( 
              total%2 = 1 
       AND    ranking = med)