--  https://school.programmers.co.kr/learn/courses/30/lessons/151139
--  group by 대여 횟수가 많은 자동차들의 월별 대여 횟수 구하기

with a as (
    select
    month(start_date) as month, car_id
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where start_date >= '2022-08-01' and start_date < '2022-11-01'
), b as (
    select car_id, count(*) as total_count
    from a
    group by car_id
    having total_count >= 5
)


select
a.month, a.car_id, count(*) as records
from a join b
on a.car_id = b.car_id
group by month, car_id
order by a.month asc, a.car_id desc