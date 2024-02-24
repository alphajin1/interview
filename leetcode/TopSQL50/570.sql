select
    name
from (
    select
        a.id, a.name as name, count(*) as count
    from Employee a left join Employee b on a.id = b.managerId
    group by a.id, a.name
) c
where count >= 5

-- another solution
-- managerId 에 할당 하자.

SELECT e2.Name
FROM Employee e1
    JOIN Employee e2 ON e1.ManagerId = e2.Id
GROUP BY e1.ManagerId
HAVING count(e1.Id) >= 5;