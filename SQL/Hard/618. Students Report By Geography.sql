SELECT Min(america) AS America, 
       Min(asia)    AS Asia, 
       Min(europe)  AS Europe 
FROM   (SELECT Row_number () 
                 OVER ( 
                   partition BY continent 
                   ORDER BY NAME ASC) AS row_num, 
               CASE 
                 WHEN continent = 'America' THEN NAME 
               END                    AS America, 
               CASE 
                 WHEN continent = 'Europe' THEN NAME 
               END                    AS Europe, 
               CASE 
                 WHEN continent = 'Asia' THEN NAME 
               END                    AS Asia 
        FROM   student) tmp 
GROUP  BY row_num 