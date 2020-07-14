SELECT team_id, 
       team_name, 
       Sum(points) AS num_points 
FROM   (SELECT t.team_id   AS team_id, 
               t.team_name AS team_name, 
               CASE 
                 WHEN ( m.host_goals > m.guest_goals 
                        AND m.host_team = t.team_id ) 
                       OR ( m.host_goals < m.guest_goals 
                            AND m.guest_goals = t.team_id ) THEN 3 
                 WHEN ( m.host_goals = m.guest_goals 
                        AND m.host_team = t.team_id ) 
                       OR ( m.host_goals = m.guest_goals 
                            AND m.guest_team = t.team_id ) THEN 1 
                 ELSE 0 
               END         AS points 
        FROM   teams t, 
               matches m) tmp 
GROUP  BY team_id, 
          team_name 
ORDER  BY num_points DESC, 
          team_name ASC 


--- because 40 Chicago FC does not have records in matches table, 
--- but it needs to appear in the final table, 
--- we should use FROM   teams t, matches m directly instead of 
--- teams t join matches m on t.team_id = m.guest_team or t.team_id = m.host_team
--- otherwise 40 Chicago FC will not appear in the result table


SELECT t.team_id, 
       team_name, 
       Ifnull(Sum(points), 0) AS num_points 
FROM   teams AS t 
       LEFT JOIN (SELECT host_team AS team_id, 
                         Sum(CASE 
                               WHEN host_goals > guest_goals THEN 3 
                               WHEN host_goals = guest_goals THEN 1 
                               ELSE 0 
                             END)  AS points 
                  FROM   matches 
                  GROUP  BY 1 
                  UNION ALL 
                  SELECT guest_team AS team_id, 
                         Sum(CASE 
                               WHEN host_goals < guest_goals THEN 3 
                               WHEN host_goals = guest_goals THEN 1 
                               ELSE 0 
                             END)   AS points 
                  FROM   matches 
                  GROUP  BY 1) tmp 
              ON t.team_id = tmp.team_id 
GROUP  BY 1 
ORDER  BY num_points DESC, 
          t.team_id; 