# write your mysql query statement belowSELECT   event_date                                                             AS install_dt,
         Count(*)                                                               AS installs, 
         round(sum(IF(Datediff(next_date, event_date) = 1, 1,0 )) / count(*),2) AS day1_retention 
FROM     ( 
                  SELECT   player_id, 
                           event_date, 
                           row_number() OVER (partition BY player_id ORDER BY event_date)                                AS ranking,
                           COALESCE (lead(event_date, 1) OVER (partition BY player_id ORDER BY event_date), event_date ) AS next_date
                  FROM     activity ) tmp1 
WHERE    ranking = 1 
GROUP BY install_dt 
ORDER BY install_dt


WITH init 
     AS (SELECT player_id, 
                First_value(event_date) 
                  OVER ( 
                    partition BY player_id 
                    ORDER BY event_date) AS initial, 
                event_date 
         FROM   activity) 
SELECT initial                                              AS install_dt, 
       Count(DISTINCT player_id)                            AS installs, 
       Round(Sum(CASE 
                   WHEN Dateadd(dd, 1, initial) = event_date THEN 1.0 
                   ELSE 0 
                 END) / Count(DISTINCT player_id) * 1.0, 2) AS Day1_retention 
FROM   init 
GROUP  BY initial 