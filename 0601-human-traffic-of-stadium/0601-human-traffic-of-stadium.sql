# Write your MySQL query statement below

select distinct s1.id , s1.visit_date , s1.people
from Stadium s1
join Stadium s2 on s1.people >= 100 and s2.people >= 100
join Stadium s3 on s3.people >= 100
where
(s2.id = s1.id+1 and s3.id = s1.id+2)
# (s1 , s2 , s3)
#(s2 , s1 , s3)
or (s1.id = s2.id+1 and s3.id = s1.id+1)
or (s2.id = s1.id-2 and s3.id = s1.id - 1)
# (s2 , s3 , s1)
order by s1.visit_date asc ;