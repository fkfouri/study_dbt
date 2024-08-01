-- credit_card_count: Breakdown of the count of fares paid by credit card.
-- quantidade de corridas pagas com cartão de crédito

{{ config(materialized='table') }}

select payment, count(payment) as count
from {{ ref('taxi_trips') }}
where payment = 'credit card'
group by payment