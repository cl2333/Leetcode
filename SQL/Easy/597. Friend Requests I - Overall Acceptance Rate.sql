-- Write your MySQL query statement below 
SELECT Ifnull(Round((SELECT Count(DISTINCT requester_id, accepter_id) 
                     FROM   request_accepted) / (SELECT 
                           Count(DISTINCT sender_id, send_to_id) 
                                                 FROM   friend_request), 2), 
       0.00) AS 
       accept_rate 