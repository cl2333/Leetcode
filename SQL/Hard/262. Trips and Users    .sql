-- /* Write your T-SQL query statement below */
select c.Request_at as Day,round(cancel_count/total_count,2) as "Cancellation Rate"
from 
(
select sum(case when status = 'completed' then 0 else 1 end) as cancel_count, Request_at
from trips   
where Client_Id not in (select Users_Id from users where banned = 'Yes')
and Driver_Id not in (select Users_Id from users where banned = 'Yes')
and Request_at between '2013-10-01' and '2013-10-03'

group by Request_at
    
) c 
join 
(
select count(*) as total_count, Request_at
from trips   
where Client_Id not in (select Users_Id from users where banned = 'Yes')
and Driver_Id not in (select Users_Id from users where banned = 'Yes')
and Request_at between '2013-10-01' and '2013-10-03'
group by Request_at
   
) t 
on c.Request_at = t.Request_at ;


    
-- simpler answer

with t as (select users_id
           from users
           where banned='Yes')
           
select request_at Day, round((sum(if(status<>'completed',1,0))/(count(*))),2) 'Cancellation Rate'
from trips
where client_id not in (select * from t) and driver_id not in (select * from t) and request_at between '2013-10-01' and '2013-10-03'
group by request_at