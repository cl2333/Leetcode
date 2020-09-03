# write your mysql query statement below
SELECT round(sum(IF(Datediff(later_date, event_date)=1, 1, 0))/count(*),2) AS fraction 
FROM   ( 
                SELECT   player_id, 
                         event_date, 
                         lead(event_date,1) OVER (partition BY player_id ORDER BY event_date ) AS later_date,
                         row_number() OVER (partition BY player_id ORDER BY event_date )       AS ranking
                FROM     activity ) tmp 
WHERE  ranking = 1