# Write your MySQL query statement below

select round(count(a.player_id) / (select count(distinct player_id) from Activity) , 2)
as fraction

from
(select
player_id , min(event_date) as first_login
from Activity
group by player_id) f

join Activity a
on f.player_id = a.player_id
and a.event_date = date_add(f.first_login , Interval 1 day) ; 