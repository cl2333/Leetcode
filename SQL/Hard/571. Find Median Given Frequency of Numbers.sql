select avg(1.0*Number) as median

from 
(
select *, sum(frequency) over (order by Number) as cum_sum
        , (sum(Frequency) over ())/2.0  as mid
from Numbers
    ) temp
    
where mid between cum_sum - frequency and cum_sum