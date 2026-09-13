# Write your MySQL query statement below

-- select eu.unique_id , e.name 
-- from Employees e
-- left join EmployeeUNI eu on e.id = eu.id ;

select 
(select eu.unique_id 
from EmployeeUNI eu
where eu.id = e.id) as unique_id , e.name
from employees e;