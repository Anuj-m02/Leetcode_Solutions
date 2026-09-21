# Write your MySQL query statement below

-- select max(num) as num
-- from (
--     select num
--     from MyNumbers
--     group by num
--     having count(num) = 1
-- ) as single_numbers ;

SELECT (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
    ORDER BY num DESC
    LIMIT 1
) AS num;