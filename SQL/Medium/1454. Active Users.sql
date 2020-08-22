# write your mysql query statement belowSELECT DISTINCT l.id, 
                NAME 
FROM            ( 
                         SELECT   id, 
                                  login_date, 
                                  Lag(login_date,4) OVER (partition BY id ORDER BY login_date) AS prev5
                         FROM     ( 
                                                  SELECT DISTINCT id, 
                                                                  login_date 
                                                  FROM            logins ) distinct_logins) l 
JOIN            accounts a 
ON              l.id = a.id 
WHERE           Datediff(login_date, prev5) = 4 
ORDER BY        id