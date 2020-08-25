# write your mysql query statement below
SELECT   player_id, 
         event_date, 
         sum(games_played) OVER (partition BY player_id ORDER BY event_date ASC rows BETWEEN UNBOUNDED PRECEDING AND      CURRENT row) AS games_played_so_far
FROM     activity 
ORDER BY player_id, 
         event_date