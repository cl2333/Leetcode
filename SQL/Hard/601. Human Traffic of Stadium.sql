# write your mysql query statement belowSELECT id, 
       visit_date, 
       people 
FROM   ( 
              SELECT id, 
                     visit_date, 
                     people, 
                     Count(*) OVER (partition BY id-rn) AS consecutive_days 
              FROM   ( 
                            SELECT id, 
                                   visit_date, 
                                   people, 
                                   Row_number() OVER () AS rn 
                            FROM   stadium 
                            WHERE  people >= 100 ) tmp1 ) tmp2 
WHERE  consecutive_days >=3


SELECT id, 
       visit_date, 
       people 
FROM  (SELECT id, 
              visit_date, 
              people, 
              Lag(people, 1) 
                OVER () AS prev_1, 
              Lag(people, 2) 
                OVER () AS prev_2, 
              Lead(people, 1) 
                OVER () AS last_1, 
              Lead(people, 2) 
                OVER () AS last_2 
       FROM   stadium) tmp1 
WHERE  ( people >= 100 
         AND prev_1 >= 100 
         AND prev_2 >= 100 ) 
        OR ( people >= 100 
             AND last_1 >= 100 
             AND last_2 >= 100 ) 
        OR ( people >= 100 
             AND prev_1 >= 100 
             AND last_1 >= 100 ) 