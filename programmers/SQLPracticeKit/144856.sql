with x as (
    select
        a.book_id,
        a.author_id,
        a.category,
        sum(a.price * coalesce(b.sales, 0)) as total_sales
    from book a left join book_sales b on a.book_id = b.book_id
    where year(b.sales_date) = 2022
    and month(b.sales_date) = 1
    group by a.book_id, a.category, a.author_id
)

select
    a.author_id, a.author_name, b.category, b.total_sales
from author a left join x b on a.author_id = b.
order by a.author_id, b.category
