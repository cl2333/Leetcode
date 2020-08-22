# Write your MySQL query statement below 
SELECT u.product_id                              AS product_id, 
       Round(Sum(price * units) / Sum(units), 2) AS average_price 
FROM   unitssold u 
       JOIN prices p 
         ON p.product_id = u.product_id 
            AND p.start_date <= u.purchase_date 
            AND p.end_date >= u.purchase_date 
GROUP  BY u.product_id 