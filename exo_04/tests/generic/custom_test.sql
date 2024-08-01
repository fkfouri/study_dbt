{% test custom_test(model, column_name) %}

-- Se o retorno for nulo, o teste passa
-- Se o retorno resultar em uma ou mais linhas, o teste falha
select * 
from {{ model }}
where {{ column_name }} is null

{% endtest %}