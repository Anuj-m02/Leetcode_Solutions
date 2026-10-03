# Write your MySQL query statement below

select f.name as person_name
from (
    select turn , 
        person_id as id , 
        person_name as name , 
        weight , 
        sum(weight) over (order by turn) as total_weight
    from Queue
) f

where f.total_weight <= 1000
order by f.total_weight desc
limit 1 ;


-- SELECT q1.person_name
-- FROM Queue q1
-- JOIN Queue q2 ON q1.turn >= q2.turn
-- GROUP BY q1.turn, q1.person_name
-- HAVING SUM(q2.weight) <= 1000
-- ORDER BY q1.turn DESC
-- LIMIT 1;