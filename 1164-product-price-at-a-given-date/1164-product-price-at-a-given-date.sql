# Write your MySQL query statement below

-- select distinct product_id , 
--     if (change_date < 2019-08-16 , new_price , 10) as price

-- from (
--     select product_id , new_price
--     from Products
--     where change_date < 2019-08-16 
-- ) ;


#products with atleast once changte on or before 2019/08/16

select product_id ,  new_price as price
from Products
where (product_id , change_date) in (
    select product_id , max(change_date)
    from Products
    where change_date <= '2019-08-16'
    group by product_id 
)

Union all

select distinct product_id , 10 as price
from Products
group by product_id
having min(change_date) > '2019-08-16' ;