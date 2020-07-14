/* Write your T-SQL query statement below */ 
SELECT seat_id 
FROM   (SELECT seat_id, 
               free, 
               Lead(free, 1) 
                 OVER ( 
                   ORDER BY seat_id) AS latter, 
               Lag(free, 1) 
                 OVER ( 
                   ORDER BY seat_id) AS prev 
        FROM   cinema) tmp 
WHERE  ( free = 1 
         AND free = prev ) 
        OR ( free = 1 
             AND free = latter ); 