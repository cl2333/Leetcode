# Write your MySQL query statement below 
SELECT col_1    AS id, 
       Count(*) AS num 
FROM   ((SELECT requester_id AS col_1, 
                accepter_id  AS col_2 
         FROM   request_accepted) 
        UNION 
        (SELECT accepter_id  AS col_1, 
                requester_id AS col_2 
         FROM   request_accepted))tmp 
GROUP  BY col_1 
ORDER  BY Count(*) DESC 
LIMIT  1 