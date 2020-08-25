# write your mysql query statement below
SELECT tmp.customer_id, 
       customer_name 
FROM   ( 
                       SELECT DISTINCT customer_id 
                       FROM            orders 
                       WHERE           customer_id NOT IN 
                                                           ( 
                                                           SELECT DISTINCT customer_id 
                                                           FROM            orders 
                                                           WHERE           product_name = 'C') 
                       AND             customer_id IN 
                                                       ( 
                                                       SELECT DISTINCT customer_id 
                                                       FROM            orders 
                                                       WHERE           product_name = 'A') 
                       AND             customer_id IN 
                                                       ( 
                                                       SELECT DISTINCT customer_id 
                                                       FROM            orders 
                                                       WHERE           product_name = 'B') ) tmp
JOIN   customers c 
ON     tmp.customer_id = c.customer_id #canUSE 
       case 
              when