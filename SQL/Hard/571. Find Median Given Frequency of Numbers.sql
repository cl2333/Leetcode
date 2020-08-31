SELECT Avg(1.0 * number) AS median 
FROM   (SELECT *, 
               Sum(frequency) 
                 OVER ( 
                   ORDER BY number) AS cum_sum, 
               ( Sum(frequency) 
                   OVER () ) / 2.0  AS mid 
        FROM   numbers) temp 
WHERE  mid BETWEEN cum_sum - frequency AND cum_sum 