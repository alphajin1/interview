select
b.category, b.max_price, a.product_name
from food_product a join
    (
        SELECT
        category, max(PRICE) max_price
        FROM FOOD_PRODUCT
        where category in ('과자', '국', '김치', '식용유')
        GROUP BY category
    ) b
on a.category = b.category and a.price = b.max_price
order by b.max_price desc


-- 식품분류별 가장 비싼 식품의 정보 조회하기
