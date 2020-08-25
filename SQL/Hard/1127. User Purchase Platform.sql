# write your mysql query statement below 

WITH cte AS 
( 
         SELECT   user_id, 
                  spend_date, 
                  sum(IF(platform = 'mobile',amount, 0))  AS mobile, 
                  sum(IF(platform = 'desktop',amount, 0)) AS desktop 
         FROM     spending 
         GROUP BY user_id, 
                  spend_date ) 

( 
         SELECT   spend_date, 
                  'mobile' AS platform, 
                  sum( 
                  CASE 
                           WHEN mobile > 0 
                           AND      desktop = 0 THEN mobile 
                           ELSE 0 
                  END) AS total_amount, 
                  sum( 
                  CASE 
                           WHEN mobile > 0 
                           AND      desktop = 0 THEN 1 
                           ELSE 0 
                  END) AS total_users 
         FROM     cte 
         GROUP BY spend_date) 
UNION ALL 
          ( 
                   SELECT   spend_date, 
                            'desktop' AS platform, 
                            sum( 
                            CASE 
                                     WHEN mobile = 0 
                                     AND      desktop > 0 THEN desktop 
                                     ELSE 0 
                            END) AS total_amount, 
                            sum( 
                            CASE 
                                     WHEN mobile = 0 
                                     AND      desktop > 0 THEN 1 
                                     ELSE 0 
                            END) AS total_users 
                   FROM     cte 
                   GROUP BY spend_date) 
 UNION ALL 
           ( 
                    SELECT   spend_date, 
                             'both' AS platform, 
                             sum( 
                             CASE 
                                      WHEN mobile > 0 
                                      AND      desktop > 0 THEN mobile + desktop 
                                      ELSE 0 
                             END) AS total_amount, 
                             sum( 
                             CASE 
                                      WHEN mobile > 0 
                                      AND      desktop > 0 THEN 1 
                                      ELSE 0 
                             END) AS total_users 
                    FROM     cte 
                    GROUP BY spend_date) 
 ORDER BY  spend_date