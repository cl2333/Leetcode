# write your mysql query statement below
SELECT username, 
       activity, 
       startdate, 
       enddate 
FROM   ( 
                SELECT   username, 
                         activity, 
                         startdate, 
                         enddate, 
                         Row_number() OVER (partition BY username ORDER BY startdate DESC) AS ranking,
                         Count(*) OVER (partition BY username)                             AS total_counts
                FROM     useractivity ) tmp 
WHERE  ranking = 2 
OR     total_counts = 1