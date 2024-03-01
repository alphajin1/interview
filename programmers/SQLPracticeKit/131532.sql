
select
    year,
    month,
    gender,
    count(distinct user_id) users
from
(
    select
        year(b.sales_date) year,
        month(b.sales_date) month,
        a.gender,
        a.user_id
    from user_info a join online_sale b
    on a.user_id = b.user_id
) c
where gender is not null
group by year, month, gender
order by year, month, gender

-- 년, 월, 성별 별 상품 구매 회원 수 구하기
