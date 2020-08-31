/* Write your T-SQL query statement below */ 
SELECT Date_format(trans_date, '%Y-%m')       AS month, 
       country, 
       Count(*)                               AS trans_count, 
       SUM(IF(state = 'approved', 1, 0))      AS approved_count, 
       SUM(amount)                            AS trans_total_amount, 
       SUM(IF(state = 'approved', amount, 0)) AS approved_total_amount 
FROM   transactions 
GROUP  BY Date_format(trans_date, '%Y-%m'), 
          country 