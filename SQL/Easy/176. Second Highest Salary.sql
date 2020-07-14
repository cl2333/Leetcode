# Write your MySQL query statement below 
-- except for the highest salary, find the next highest salary
-- (the other way is to use dense_rank())
SELECT Max(salary) AS SecondHighestSalary 
FROM   employee 
WHERE  salary NOT IN (SELECT Max(salary) 
                      FROM   employee) 