# write your mysql query statement below

SELECT student_id, 
       student_name 
FROM   student 
WHERE  student_id NOT IN 
                          ( 
                          SELECT DISTINCT student_id 
                          FROM            ( 
                                                   SELECT   student_id, 
                                                            Rank() OVER (partition BY exam_id ORDER BY score DESC) AS rank_desc,
                                                            Rank() OVER (partition BY exam_id ORDER BY score ASC)  AS rank_asc
                                                   FROM     exam ) tmp1 
                          WHERE           rank_desc = 1 
                          OR              rank_asc = 1 ) 
AND    student_id IN 
                      ( 
                      SELECT DISTINCT student_id 
                      FROM            exam)