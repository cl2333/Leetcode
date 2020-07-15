-- Write your MySQL query statement below  
SELECT Round(Avg(day_remove_rate), 2) AS average_daily_percent 
FROM   (SELECT Ifnull(remove_count, 0) * 100 / total_count AS day_remove_rate 
        FROM   (SELECT Count(DISTINCT post_id) AS total_count, 
                       action_date 
                FROM   actions 
                WHERE  extra = 'spam' 
                GROUP  BY action_date) t 
               LEFT JOIN (SELECT Count(DISTINCT removals.post_id) AS 
                                 remove_count, 
                                 actions.action_date              AS date 
                          FROM   removals 
                                 LEFT JOIN actions 
                                        ON removals.post_id = actions.post_id 
                          WHERE  extra = 'spam' 
                          GROUP  BY actions.action_date) r 
                      ON t.action_date = r.date) tmp 

-- Be careful about distinct, because post_id may be duplicate 
-- a simpler version

# Write your MySQL query statement below  
SELECT Round(Avg(day_remove_rate), 2) AS average_daily_percent 
FROM   (SELECT Ifnull(remove_count, 0) * 100 / total_count AS day_remove_rate 
        FROM   (SELECT Count(DISTINCT a.post_id) AS total_count, 
                       Count(DISTINCT r.post_id) AS remove_count, 
                       action_date 
                FROM   actions a 
                       LEFT JOIN removals r 
                              ON a.post_id = r.post_id 
                WHERE  extra = 'spam' 
                GROUP  BY action_date) rate_by_date) tmp 