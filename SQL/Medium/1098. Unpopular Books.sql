SELECT book_id, 
       NAME 
FROM   (SELECT b.book_id           AS book_id, 
               b.NAME              AS NAME, 
               ISNULL(Sum (IIF (dispatch_date BETWEEN 
                                '2018-06-23' AND '2019-06-23', 
                           quantity, 
                           0)), 0) AS sales 
        FROM   books b 
               LEFT JOIN orders o 
                      ON b.book_id = o.book_id 
        WHERE  available_from < '2019-05-23' 
        GROUP  BY b.book_id, 
                  b.NAME) tmp 
WHERE  sales < 10 
ORDER  BY book_id ASC; 