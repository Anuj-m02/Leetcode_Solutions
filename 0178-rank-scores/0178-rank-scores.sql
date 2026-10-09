# Write your MySQL query statement below

-- select s.score , count(s.score) as 'rank' from scores s ,
-- (select distinct score from scores ) s2
-- where s.score <= s2.score
-- group by s.id
-- order by s.score desc ;


select score , dense_rank() over (order by score desc) as "rank"
from Scores;