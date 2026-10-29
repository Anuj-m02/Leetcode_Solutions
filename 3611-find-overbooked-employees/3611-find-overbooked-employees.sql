# Write your MySQL query statement below

with weeklyMeetings as (

    select employee_id , 
    yearweek(meeting_date , 3) as week_no ,
    sum(duration_hours) as total_hours

    from meetings
    group by 
        employee_id , yearweek(meeting_date , 3)
    having total_hours > 20

)

select e.employee_id , e.employee_name , e.department , 
count(wm.week_no) as meeting_heavy_weeks

from employees e
join weeklyMeetings wm on e.employee_id = wm.employee_id

group by e.employee_id , e.employee_name , e.department
having count(wm.week_no) >= 2
order by meeting_heavy_weeks desc , e.employee_name asc ;