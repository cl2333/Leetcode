# Write your MySQL query statement below 
SELECT user_id         AS buyer_id, 
       join_date, 
       Count(order_id) AS orders_in_2019 
FROM   users u 
       LEFT JOIN (SELECT order_id, 
                         buyer_id 
                  FROM   orders 
                  WHERE  Year(order_date) = 2019) o 
              ON u.user_id = o.buyer_id 
GROUP  BY user_id, 
          join_date 