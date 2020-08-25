# write your mysql query statement below
SELECT   'failed'       AS period_state, 
         Min(fail_date) AS start_date, 
         Max(fail_date) AS end_date 
FROM     ( 
                SELECT fail_date, 
                       date_sub(fail_date, interval ranking day) AS group_day 
                FROM   ( 
                              SELECT fail_date, 
                                     row_number() OVER () AS ranking 
                              FROM   failed 
                              WHERE  ( 
                                            fail_date BETWEEN '2019-01-01' AND    '2019-12-31') 
                              AND    ( 
                                            fail_date BETWEEN '2019-01-01' AND    '2019-12-31') ) tmp) s 
GROUP BY group_day 
UNION 
SELECT   'succeeded'       AS period_state, 
         min(success_date) AS start_date, 
         max(success_date) AS end_date 
FROM     ( 
                SELECT success_date, 
                       date_sub(success_date, interval ranking day) AS group_day 
                FROM   ( 
                              SELECT success_date, 
                                     row_number() OVER () AS ranking 
                              FROM   succeeded 
                              WHERE  ( 
                                            success_date BETWEEN '2019-01-01' AND    '2019-12-31') 
                              AND    ( 
                                            success_date BETWEEN '2019-01-01' AND    '2019-12-31') ) tmp) s 
GROUP BY group_day 
ORDER BY start_date