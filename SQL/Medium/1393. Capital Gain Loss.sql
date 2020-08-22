# Write your MySQL query statement below 
SELECT stock_name, 
       Sum(CASE 
             WHEN operation = 'Sell' THEN price 
             ELSE -price 
           end) AS capital_gain_loss 
FROM   stocks 
GROUP  BY stock_name 