# write your mysql query statement below

SELECT   NAME AS customer_name, 
         c.customer_id, 
         order_id, 
         order_date 
FROM     customers c 
JOIN 
         ( 
                  SELECT   order_id, 
                           order_date, 
                           customer_id, 
                           Row_number() OVER (partition BY customer_id ORDER BY order_date DESC) AS ranking
                  FROM     orders ) o 
ON       c.customer_id = o.customer_id 
WHERE    ranking <=3 
ORDER BY customer_name, 
         customer_id, 
         order_date DESC