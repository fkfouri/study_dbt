{{ config(materialized='table') }}

with source as (
    select * from {{ ref('raw_adid_data') }}
)

select adid, latitude, longitude, city, TO_DATE(eventdate, 'MM/DD/YYYY') eventdate, cohort from source