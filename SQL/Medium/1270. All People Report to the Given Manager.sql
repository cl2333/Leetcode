-- write your mysql query statement below 
WITH recursive cte AS 
( 
       SELECT 0 AS n , 
              1 AS employee_id 
       FROM   employees 
       UNION ALL 
       SELECT cte.n+1, 
              e.employee_id 
       FROM   employees e 
       JOIN   cte 
       ON     e.manager_id = cte.employee_id 
       WHERE  n < 3 )

SELECT DISTINCT employee_id 
FROM            cte 
WHERE           employee_id != 1 ;