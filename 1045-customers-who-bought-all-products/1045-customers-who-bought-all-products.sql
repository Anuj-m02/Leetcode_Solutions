-- # Write your MySQL query statement below

-- select c.customer_id 
-- from Customer c
-- group by c.customer_id
-- having count(distinct product_key) = select(count(*) from Product) ;

SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product);