# Write your MySQL query statement below

select employee_id
from Employees e
where employee_id not in (select employee_id from Salaries)

Union

select employee_id
from Salaries
where employee_id not in (select employee_id from Employees)

order by employee_id asc;