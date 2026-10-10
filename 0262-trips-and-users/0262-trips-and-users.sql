-- # Write your MySQL query statement below

-- select request_at as Day
-- , round(sum(case when status = 'ca'))

SELECT 
    request_at AS Day
    ,ROUND(SUM(CASE WHEN status='cancelled_by_driver' OR status='cancelled_by_client' THEN 1 ELSE 0 END) / COUNT(request_at),2) 
    AS "Cancellation Rate" /*use quote as in output we need to show like this*/
FROM  Trips t
JOIN Users c
    ON t.client_id=c.users_id /*include clients who are banned*/
    AND c.banned='No'
JOIN Users u
    ON t.driver_id=u.users_id/*include drivers who are banned*/
    AND u.banned='No'
WHERE request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY request_at
