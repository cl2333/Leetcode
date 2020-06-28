-- /* Write your T-SQL query statement below */ 
SELECT c.request_at                         AS Day, 
       Round(cancel_count / total_count, 2) AS "Cancellation Rate" 
FROM   (SELECT Sum(CASE 
                     WHEN status = 'completed' THEN 0 
                     ELSE 1 
                   END) AS cancel_count, 
               request_at 
        FROM   trips 
        WHERE  client_id NOT IN (SELECT users_id 
                                 FROM   users 
                                 WHERE  banned = 'Yes') 
               AND driver_id NOT IN (SELECT users_id 
                                     FROM   users 
                                     WHERE  banned = 'Yes') 
               AND request_at BETWEEN '2013-10-01' AND '2013-10-03' 
        GROUP  BY request_at) c 
       JOIN (SELECT Count(*) AS total_count, 
                    request_at 
             FROM   trips 
             WHERE  client_id NOT IN (SELECT users_id 
                                      FROM   users 
                                      WHERE  banned = 'Yes') 
                    AND driver_id NOT IN (SELECT users_id 
                                          FROM   users 
                                          WHERE  banned = 'Yes') 
                    AND request_at BETWEEN '2013-10-01' AND '2013-10-03' 
             GROUP  BY request_at) t 
         ON c.request_at = t.request_at; 


    
-- simpler answer 
WITH t AS 
( 
       SELECT users_id 
       FROM   users 
       WHERE  banned='Yes') 
SELECT   request_at day, 
         round((sum(IF(status<>'completed',1,0))/(count(*))),2) 'Cancellation Rate' 
FROM     trips 
WHERE    client_id NOT IN 
         ( 
                SELECT * 
                FROM   t) 
AND      driver_id NOT IN 
         ( 
                SELECT * 
                FROM   t) 
AND      request_at BETWEEN '2013-10-01' AND      '2013-10-03' 
GROUP BY request_at