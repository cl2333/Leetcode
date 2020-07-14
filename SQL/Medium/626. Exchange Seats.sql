SELECT 
  id, 
  COALESCE (
    CASE WHEN id % 2 = 1 THEN Lead(student, 1) OVER(
      ORDER BY 
        id
    ) ELSE Lag(student, 1) OVER(
      ORDER BY 
        id
    ) END, 
    student
  ) AS student 
FROM 
  seat;
