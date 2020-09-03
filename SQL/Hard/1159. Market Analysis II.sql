# write your mysql query statement below
SELECT u.user_id AS seller_id,IF(favorite_brand = item_brand, 'yes','no') as 2nd_item_fav_brand 
FROM users u LEFT JOIN 
( 
       SELECT seller_id, 
              item_id 
       FROM   ( 
                       SELECT   seller_id, 
                                item_id, 
                                row_number() OVER (partition BY seller_id ORDER BY order_date) AS ranking
                       FROM     orders ) tmp 
       WHERE  ranking = 2) o ON u.user_id = o.seller_id LEFT JOIN items i ON o.item_id = i.item_id