# Write your MySQL query statement below

-- select Visits.customer_id , Count(Visits.visit_id) as count_no_trans
-- from Visits 
-- left join Transactions
-- on Transactions.visit_id = visits.visit_id
-- where Transactions.transaction_id is null
-- group by Visits.customer_id ;

SELECT 
    customer_id, 
    COUNT(visit_id) AS count_no_trans
FROM Visits
WHERE visit_id NOT IN (
    SELECT DISTINCT visit_id 
    FROM Transactions
)
GROUP BY customer_id;