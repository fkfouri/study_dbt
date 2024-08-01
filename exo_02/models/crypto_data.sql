-- crypto_data: Update the materialization to ensure the best strategy is selected

{{ config(materialized='incremental') }}

with source as (
    select * from {{ ref('raw_crypto_data') }}
)
select currency, TO_DATE(detail_date, 'MM/DD/YY') detail_date, closing_price close, "24_hour_open" as open, "24h_high_usd" high, "24h_low_usd" low
from source

{% if is_incremental() %}

where detail_date > (select max(detail_date) from source)

{% endif %}
