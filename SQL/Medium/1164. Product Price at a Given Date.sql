# write your mysql query statement below
SELECT product_id, 
       new_price AS price 
FROM   ( 
                SELECT   product_id, 
                         new_price, 
                         Rank() OVER (partition BY product_id ORDER BY change_date DESC) AS ranking
                FROM     ( 
                         ( 
                                SELECT product_id, 
                                       new_price, 
                                       change_date 
                                FROM   products 
                                WHERE  change_date <= '2019-08-16') 
                  UNION 
                        ( 
                                        SELECT DISTINCT product_id, 
                                                        10, 
                                                        '0000-00-00' 
                                        FROM            products)) tmp1 ) tmp2 
WHERE    ranking = 1 
ORDER BY price DESCSELECT DISTINCT p.product_id, 
                Ifnull(new.price,10) AS price 
FROM            products p 
LEFT JOIN 
                ( 
                       SELECT product_id, 
                              new_price AS price 
                       FROM   ( 
                                       SELECT   product_id, 
                                                new_price, 
                                                Rank() OVER (partition BY product_id ORDER BY change_date DESC) AS ranking
                                       FROM     products 
                                       WHERE    change_date <= '2019-08-16' ) tmp1 
                       WHERE  ranking = 1 ) NEW 
ON              p.product_id = new.product_id 
ORDER BY        price DESC