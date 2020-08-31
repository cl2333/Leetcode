# Write your MySQL query statement below 
SELECT product_name, 
       year, 
       price 
FROM   sales s 
       JOIN product p 
         ON s.product_id = p.product_id 
ORDER  BY year 