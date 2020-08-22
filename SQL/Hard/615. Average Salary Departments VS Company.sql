# # Write your MySQL query statement below 
SELECT c.month AS pay_month, 
       d.department_id, 
       CASE 
         WHEN c.salary > d.salary THEN 'lower' 
         WHEN c.salary < d.salary THEN 'higher' 
         ELSE 'same' 
       end     AS comparison 
FROM   (SELECT Avg(amount)                    AS salary, 
               Date_format(pay_date, '%Y-%m') AS month 
        FROM   salary s 
        GROUP  BY Date_format(pay_date, '%Y-%m')) c 
       JOIN (SELECT Avg(amount)                    AS salary, 
                    Date_format(pay_date, '%Y-%m') AS month, 
                    department_id 
             FROM   salary s 
                    JOIN employee e 
                      ON s.employee_id = e.employee_id 
             GROUP  BY Date_format(pay_date, '%Y-%m'), 
                       department_id) d 
         ON c.month = d.month 