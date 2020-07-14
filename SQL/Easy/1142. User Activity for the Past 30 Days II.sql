-- -- /* Write your T-SQL query statement below */ 
SELECT Cast(Avg(sessions) AS DECIMAL(8, 2)) AS average_sessions_per_user 
FROM   (SELECT user_id, 
               Count(session_id) AS sessions 
        FROM   activity 
        WHERE  activity_type = 'open_session' 
               AND Datediff(day, activity_date, '2019-07-27') < 30 
        GROUP  BY user_id) tmp 


-- seems sql server would only round avg() to integer
-- if we want to use sql server

-- -- /* Write your T-SQL query statement below */ 
SELECT Isnull(Round(Sum(sessions) * 1.00 / Count(user_id), 2), 0.00) AS 
       average_sessions_per_user 
FROM   (SELECT user_id, 
               Count(DISTINCT session_id) AS sessions 
        FROM   activity 
        WHERE  Datediff(day, activity_date, '2019-07-27') < 30 
        GROUP  BY user_id) tmp 