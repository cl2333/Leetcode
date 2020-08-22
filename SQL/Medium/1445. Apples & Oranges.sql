# Write your MySQL query statement below 
SELECT sale_date, 
       Sum(CASE 
             WHEN fruit = 'apples' THEN sale_amount 
             ELSE -sale_amount 
           end) AS diff 
FROM   (SELECT sale_date, 
               fruit, 
               Sum(sold_num) AS sale_amount 
        FROM   sales 
        GROUP  BY sale_date, 
                  fruit) tmp 
GROUP  BY sale_date 