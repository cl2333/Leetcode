# write your mysql query statement below
SELECT   project_id, 
         employee_id 
FROM     ( 
                  SELECT   p.employee_id AS employee_id, 
                           NAME, 
                           project_id, 
                           Rank() OVER (partition BY project_id ORDER BY experience_years DESC) AS ranking
                  FROM     project p 
                  JOIN     employee e 
                  ON       p.employee_id = e.employee_id) tmp 
WHERE    ranking = 1 
ORDER BY project_id, 
         employee_id