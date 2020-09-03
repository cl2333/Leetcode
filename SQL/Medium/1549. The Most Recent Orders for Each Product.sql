# write your mysql query statement below

SELECT   product_name, 
         o.product_id, 
         order_id, 
         order_date 
FROM     ( 
                  SELECT   order_id, 
                           order_date, 
                           product_id, 
                           Rank() OVER (partition BY product_id ORDER BY order_date DESC) AS ranking
                  FROM     orders ) o 
JOIN     products p 
ON       o.product_id = p.product_id 
WHERE    ranking = 1 
ORDER BY product_name, 
         o.product_id, 
         order_id