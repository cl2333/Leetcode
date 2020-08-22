# write your mysql query statement below
SELECT student_id, 
       course_id, 
       grade 
FROM   ( 
                SELECT   student_id, 
                         course_id, 
                         grade, 
                         Rank() OVER (partition BY student_id ORDER BY grade DESC, course_id ASC) AS ranking
                FROM     enrollments) tmp 
WHERE  ranking = 1