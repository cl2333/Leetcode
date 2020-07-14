select w2.id
from weather w1, weather w2
where DATEDIFF(day, w1.RecordDate, w2.RecordDate) = 1
and w1.temperature < w2.temperature;