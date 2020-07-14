/* Write your T-SQL query statement below */ 
SELECT id, 
       NAME 
FROM   students 
WHERE  department_id NOT IN (SELECT id 
                             FROM   departments); 