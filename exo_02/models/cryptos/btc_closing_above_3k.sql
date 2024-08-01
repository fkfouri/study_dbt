
{{ config(materialized='table') }}

select *
from {{ ref('btc') }}
where close > 3000
