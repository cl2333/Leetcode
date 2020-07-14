SELECT d.NAME AS Department, 
       e.employee, 
       e.salary 
FROM   department d 
JOIN 
       ( 
                SELECT   NAME AS Employee, 
                         salary, 
                         departmentid, 
                         Rank() OVER (partition BY departmentid ORDER BY salary DESC ) AS ranking 
                FROM     employee ) e 
ON     d.id = e.departmentid 
WHERE  ranking = 1


-- only use join would be much faster than using rank()
-- find the highest salary for each department first
-- then find the employees that get the highest salary


SELECT department, 
       e.NAME AS employee, 
       e.salary 
FROM   employee e 
       JOIN (SELECT departmentid, 
                    d.NAME      AS Department, 
                    Max(salary) AS salary 
             FROM   employee e 
                    JOIN department d 
                      ON e.departmentid = d.id 
             GROUP  BY 1, 
                       2) tmp 
         ON e.departmentid = tmp.departmentid 
            AND e.salary = tmp.salary 