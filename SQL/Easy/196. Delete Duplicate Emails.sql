-- Write your MySQL query statement below
DELETE FROM Person WHERE 
id in (select id 
from (
select id, ROW_NUMBER() OVER (partition by email order by id asc) as ranking
from person
) t where t.ranking > 1
      );

-- simpler version
With cte as
(
Select pp.id as id
from person p
join person pp
on p.email = pp.email and p.id<pp.id)

Delete from
Person
where ID IN (Select id from cte)