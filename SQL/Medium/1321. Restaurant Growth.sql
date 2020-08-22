# write your mysql query statement below
SELECT   visited_on, 
         sum(amount) OVER (ORDER BY visited_on ASC rows BETWEEN 6 PRECEDING AND      CURRENT row )         AS amount,
         round(avg(amount) OVER (ORDER BY visited_on ASC rows BETWEEN 6 PRECEDING AND      CURRENT row),2) AS average_amount
FROM     ( 
                  SELECT   visited_on, 
                           sum(amount) AS amount 
                  FROM     customer 
                  GROUP BY visited_on ) tmp limit 6, 
         100