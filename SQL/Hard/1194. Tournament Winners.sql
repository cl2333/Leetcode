# write your mysql query statement below WITH result AS 
( 
         SELECT   group_id, 
                  player_id, 
                  row_number() OVER (partition BY group_id ORDER BY sum(score) DESC) AS ranking 
         FROM     ( 
                  ( 
                         SELECT first_player AS player, 
                                first_score  AS score 
                         FROM   matches) 
           UNION ALL 
                     ( 
                            SELECT second_player AS player, 
                                   second_score  AS score 
                            FROM   matches)) m 
        JOIN      players p 
        ON        m.player = p.player_id 
        GROUP BY  group_id, 
                  player_id 
        ORDER BY  group_id, 
                  player_id)SELECT group_id, 
       player_id 
FROM   result 
WHERE  ranking = 1