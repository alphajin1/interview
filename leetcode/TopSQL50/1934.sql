with x as (
    select
        user_id,
        sum(
            case
                when action = 'confirmed' then 1
                else 0
            end
        ) cf_count,
        count(*) tot_count
    from Confirmations
    group by user_id
)

select
    a.user_id,
    ROUND(IFNULL(cf_count / tot_count, 0), 2) confirmation_rate
    from Signups a left join x
        on a.user_id = x.user_id
-- TODO 02-26
-- TODO 02-27
-- TODO 03-01
-- https://leetcode.com/problems/confirmation-rate/description/?envType=study-plan-v2&envId=top-sql-50