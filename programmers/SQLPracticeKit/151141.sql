select
    history_id, round(duration * daily_fee * (100 - ifnull(y.discount_rate, 0)) / 100) fee
from
(
    select
        a.history_id,
        b.car_type,
        b.daily_fee,
        datediff(a.end_date, a.start_date) + 1 as duration,
    CASE
      WHEN DATEDIFF(end_date, start_date) + 1 >= 90 THEN '90일 이상'
      WHEN DATEDIFF(end_date, start_date) + 1 >= 30 THEN '30일 이상'
      WHEN DATEDIFF(end_date, start_date) + 1 >= 7 THEN '7일 이상'
      ELSE 'NONE' END AS duration_type
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY a
    join CAR_RENTAL_COMPANY_CAR b on a.car_id = b.car_id
    where b.car_type = '트럭'
) x
left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN y
    on x.duration_type = y.duration_type and x.car_type = y.car_type
order by fee desc, history_id desc

-- 자동차 대여 기록 별 대여 금액 구하기
