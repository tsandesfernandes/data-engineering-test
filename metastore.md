


Alguns pontos a serem considerados:
* Donos das tabelas
* Acesso e permissão das squads 

<h2>Metadados das tabelas</h2> 

*Tabela consumer*

|Coluna|Valor|
| --- | --- |
|customer_id|string|
|language|string|
|created_at|string|
|active|long|
|customer_name|string|
|customer_phone_area|long|
|customer_phone_number|long|


*Tabela restaurant*

|Coluna|Valor|
| --- | --- |
|id|string|
|created_at|string|
|enabled|long|
|price_range|long|
|average_ticket|double|
|takeout_time|long|
|delivery_time|long|
|minimum_order_value|double|
|merchant_zip_code|long|
|merchant_city|string|
|merchant_state|string|
|merchant_country|string|


*Tabela order*

|Coluna|Valor|
| --- | --- |
|cpf|integer|
|customer_id|string|
|customer_name|string|
|delivery_address_city|string|
|delivery_address_country|string|
|delivery_address_district|string|
|delivery_address_external_id|integer|
|delivery_address_latitude|float|
|delivery_address_longitude|float|
|delivery_address_state|string|
|delivery_address_zip_code|integer|
|items|string|
|merchant_id|string|
|merchant_latitude|string|
|merchant_longitude|string|
|merchant_timezone|string|
|order_created_at|string|
|order_id|string|
|order_scheduled|boolean|
|order_scheduled_date|string|
|order_total_amount|double|
|origin_platform|string|

*Tabela orderEvents*

|Coluna|Valor|
| --- | --- |
|created_at|timestamp|
|order_id|string|
|status_id|string|
|value|string|
