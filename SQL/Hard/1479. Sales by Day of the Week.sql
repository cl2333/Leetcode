# Write your MySQL query statement below 
SELECT category, 
       Sum(IF(day = 'Monday', quantity, 0))    AS 'Monday', 
       Sum(IF(day = 'Tuesday', quantity, 0))   AS 'Tuesday', 
       Sum(IF(day = 'Wednesday', quantity, 0)) AS 'Wednesday', 
       Sum(IF(day = 'Thursday', quantity, 0))  AS 'Thursday', 
       Sum(IF(day = 'Friday', quantity, 0))    AS 'Friday', 
       Sum(IF(day = 'Saturday', quantity, 0))  AS 'Saturday', 
       Sum(IF(day = 'Sunday', quantity, 0))    AS 'Sunday' 
FROM   (SELECT item_category       AS category, 
               Dayname(order_date) AS day, 
               Sum(quantity)       AS quantity 
        FROM   orders o 
               RIGHT JOIN items i 
                       ON o.item_id = i.item_id 
        GROUP  BY item_category, 
                  Dayname(order_date)) tmp 
GROUP  BY category 
ORDER  BY category 