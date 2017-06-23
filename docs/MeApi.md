# OrderCloud.MeApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**me_addresses_address_id_delete**](MeApi.md#me_addresses_address_id_delete) | **DELETE** /me/addresses/{addressID} | 
[**me_addresses_address_id_get**](MeApi.md#me_addresses_address_id_get) | **GET** /me/addresses/{addressID} | 
[**me_addresses_address_id_patch**](MeApi.md#me_addresses_address_id_patch) | **PATCH** /me/addresses/{addressID} | 
[**me_addresses_address_id_put**](MeApi.md#me_addresses_address_id_put) | **PUT** /me/addresses/{addressID} | 
[**me_addresses_get**](MeApi.md#me_addresses_get) | **GET** /me/addresses | 
[**me_addresses_post**](MeApi.md#me_addresses_post) | **POST** /me/addresses | 
[**me_catalogs_catalog_id_get**](MeApi.md#me_catalogs_catalog_id_get) | **GET** /me/catalogs/{catalogID} | 
[**me_catalogs_get**](MeApi.md#me_catalogs_get) | **GET** /me/catalogs | 
[**me_categories_get**](MeApi.md#me_categories_get) | **GET** /me/categories | 
[**me_costcenters_get**](MeApi.md#me_costcenters_get) | **GET** /me/costcenters | 
[**me_creditcards_creditcard_id_delete**](MeApi.md#me_creditcards_creditcard_id_delete) | **DELETE** /me/creditcards/{creditcardID} | 
[**me_creditcards_creditcard_id_get**](MeApi.md#me_creditcards_creditcard_id_get) | **GET** /me/creditcards/{creditcardID} | 
[**me_creditcards_creditcard_id_patch**](MeApi.md#me_creditcards_creditcard_id_patch) | **PATCH** /me/creditcards/{creditcardID} | 
[**me_creditcards_creditcard_id_put**](MeApi.md#me_creditcards_creditcard_id_put) | **PUT** /me/creditcards/{creditcardID} | 
[**me_creditcards_get**](MeApi.md#me_creditcards_get) | **GET** /me/creditcards | 
[**me_creditcards_post**](MeApi.md#me_creditcards_post) | **POST** /me/creditcards | 
[**me_get**](MeApi.md#me_get) | **GET** /me | 
[**me_orders_approvable_get**](MeApi.md#me_orders_approvable_get) | **GET** /me/orders/approvable | 
[**me_orders_get**](MeApi.md#me_orders_get) | **GET** /me/orders | 
[**me_orders_put**](MeApi.md#me_orders_put) | **PUT** /me/orders | 
[**me_password_post**](MeApi.md#me_password_post) | **POST** /me/password | 
[**me_patch**](MeApi.md#me_patch) | **PATCH** /me | 
[**me_products_get**](MeApi.md#me_products_get) | **GET** /me/products | 
[**me_products_product_id_get**](MeApi.md#me_products_product_id_get) | **GET** /me/products/{productID} | 
[**me_products_product_id_specs_get**](MeApi.md#me_products_product_id_specs_get) | **GET** /me/products/{productID}/specs | 
[**me_products_product_id_specs_spec_id_get**](MeApi.md#me_products_product_id_specs_spec_id_get) | **GET** /me/products/{productID}/specs/{specID} | 
[**me_promotions_get**](MeApi.md#me_promotions_get) | **GET** /me/promotions | 
[**me_promotions_promotion_id_get**](MeApi.md#me_promotions_promotion_id_get) | **GET** /me/promotions/{promotionID} | 
[**me_put**](MeApi.md#me_put) | **PUT** /me | 
[**me_register_put**](MeApi.md#me_register_put) | **PUT** /me/register | 
[**me_shipments_get**](MeApi.md#me_shipments_get) | **GET** /me/shipments | 
[**me_shipments_shipment_id_get**](MeApi.md#me_shipments_shipment_id_get) | **GET** /me/shipments/{shipmentID} | 
[**me_shipments_shipment_id_items_get**](MeApi.md#me_shipments_shipment_id_items_get) | **GET** /me/shipments/{shipmentID}/items | 
[**me_spending_accounts_get**](MeApi.md#me_spending_accounts_get) | **GET** /me/spendingAccounts | 
[**me_spendingaccounts_spending_account_id_get**](MeApi.md#me_spendingaccounts_spending_account_id_get) | **GET** /me/spendingaccounts/{spendingAccountID} | 
[**me_usergroups_get**](MeApi.md#me_usergroups_get) | **GET** /me/usergroups | 


# **me_addresses_address_id_delete**
> me_addresses_address_id_delete(address_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
address_id = 'address_id_example' # str | ID of the address.

try: 
    MeApi.me_addresses_address_id_delete(address_id)
except ApiException as e:
    print("Exception when calling MeApi->me_addresses_address_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_id** | **str**| ID of the address. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_addresses_address_id_get**
> BuyerAddress me_addresses_address_id_get(address_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
address_id = 'address_id_example' # str | ID of the address.

try: 
    response = MeApi.me_addresses_address_id_get(address_id)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->me_addresses_address_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_id** | **str**| ID of the address. | 

### Return type

[**BuyerAddress**](BuyerAddress.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_addresses_address_id_patch**
> me_addresses_address_id_patch(address_id, address)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
address_id = 'address_id_example' # str | ID of the address.
address = OrderCloud.Address() # Address | 

try: 
    MeApi.me_addresses_address_id_patch(address_id, address)
except ApiException as e:
    print("Exception when calling MeApi->me_addresses_address_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_id** | **str**| ID of the address. | 
 **address** | [**Address**](Address.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_addresses_address_id_put**
> BuyerAddress me_addresses_address_id_put(address_id, address)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
address_id = 'address_id_example' # str | ID of the address.
address = OrderCloud.BuyerAddress() # BuyerAddress | 

try: 
    response = MeApi.me_addresses_address_id_put(address_id, address)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->me_addresses_address_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_id** | **str**| ID of the address. | 
 **address** | [**BuyerAddress**](BuyerAddress.md)|  | 

### Return type

[**BuyerAddress**](BuyerAddress.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_addresses_get**
> ListBuyerAddress me_addresses_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
search = 'search_example' # str | Search of the address. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the address. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the address. (optional)
page = 56 # int | Page of the address. (optional)
page_size = 56 # int | Page size of the address. (optional)

try: 
    response = MeApi.me_addresses_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->me_addresses_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search of the address. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the address. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the address. | [optional] 
 **page** | **int**| Page of the address. | [optional] 
 **page_size** | **int**| Page size of the address. | [optional] 

### Return type

[**ListBuyerAddress**](ListBuyerAddress.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_addresses_post**
> BuyerAddress me_addresses_post(address)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
address = OrderCloud.BuyerAddress() # BuyerAddress | 

try: 
    response = MeApi.me_addresses_post(address)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->me_addresses_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | [**BuyerAddress**](BuyerAddress.md)|  | 

### Return type

[**BuyerAddress**](BuyerAddress.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_catalogs_catalog_id_get**
> Catalog me_catalogs_catalog_id_get(catalog_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
catalog_id = 'catalog_id_example' # str | ID of the catalog.

try: 
    response = MeApi.me_catalogs_catalog_id_get(catalog_id)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->me_catalogs_catalog_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | 

### Return type

[**Catalog**](Catalog.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_catalogs_get**
> ListCatalog me_catalogs_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
search = 'search_example' # str | Search of the catalog. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the catalog. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the catalog. (optional)
page = 56 # int | Page of the catalog. (optional)
page_size = 56 # int | Page size of the catalog. (optional)

try: 
    response = MeApi.me_catalogs_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->me_catalogs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search of the catalog. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the catalog. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the catalog. | [optional] 
 **page** | **int**| Page of the catalog. | [optional] 
 **page_size** | **int**| Page size of the catalog. | [optional] 

### Return type

[**ListCatalog**](ListCatalog.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_categories_get**
> ListCategory me_categories_get(depth=depth, catalog_id=catalog_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
depth = 'depth_example' # str | Depth of the category. (optional)
catalog_id = 'catalog_id_example' # str | ID of the catalog. (optional)
search = 'search_example' # str | Search of the category. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the category. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the category. (optional)
page = 56 # int | Page of the category. (optional)
page_size = 56 # int | Page size of the category. (optional)

try: 
    response = MeApi.me_categories_get(depth=depth, catalog_id=catalog_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->me_categories_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **depth** | **str**| Depth of the category. | [optional] 
 **catalog_id** | **str**| ID of the catalog. | [optional] 
 **search** | **str**| Search of the category. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the category. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the category. | [optional] 
 **page** | **int**| Page of the category. | [optional] 
 **page_size** | **int**| Page size of the category. | [optional] 

### Return type

[**ListCategory**](ListCategory.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_costcenters_get**
> ListCostCenter me_costcenters_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
search = 'search_example' # str | Search of the cost center. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the cost center. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the cost center. (optional)
page = 56 # int | Page of the cost center. (optional)
page_size = 56 # int | Page size of the cost center. (optional)

try: 
    response = MeApi.me_costcenters_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->me_costcenters_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search of the cost center. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the cost center. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the cost center. | [optional] 
 **page** | **int**| Page of the cost center. | [optional] 
 **page_size** | **int**| Page size of the cost center. | [optional] 

### Return type

[**ListCostCenter**](ListCostCenter.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_creditcards_creditcard_id_delete**
> me_creditcards_creditcard_id_delete(creditcard_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
creditcard_id = 'creditcard_id_example' # str | ID of the creditcard.

try: 
    MeApi.me_creditcards_creditcard_id_delete(creditcard_id)
except ApiException as e:
    print("Exception when calling MeApi->me_creditcards_creditcard_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creditcard_id** | **str**| ID of the creditcard. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_creditcards_creditcard_id_get**
> BuyerCreditCard me_creditcards_creditcard_id_get(creditcard_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
creditcard_id = 'creditcard_id_example' # str | ID of the creditcard.

try: 
    response = MeApi.me_creditcards_creditcard_id_get(creditcard_id)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->me_creditcards_creditcard_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creditcard_id** | **str**| ID of the creditcard. | 

### Return type

[**BuyerCreditCard**](BuyerCreditCard.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_creditcards_creditcard_id_patch**
> me_creditcards_creditcard_id_patch(creditcard_id, credit_card)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
creditcard_id = 'creditcard_id_example' # str | ID of the creditcard.
credit_card = OrderCloud.CreditCard() # CreditCard | 

try: 
    MeApi.me_creditcards_creditcard_id_patch(creditcard_id, credit_card)
except ApiException as e:
    print("Exception when calling MeApi->me_creditcards_creditcard_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creditcard_id** | **str**| ID of the creditcard. | 
 **credit_card** | [**CreditCard**](CreditCard.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_creditcards_creditcard_id_put**
> BuyerCreditCard me_creditcards_creditcard_id_put(creditcard_id, credit_card)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
creditcard_id = 'creditcard_id_example' # str | ID of the creditcard.
credit_card = OrderCloud.BuyerCreditCard() # BuyerCreditCard | 

try: 
    response = MeApi.me_creditcards_creditcard_id_put(creditcard_id, credit_card)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->me_creditcards_creditcard_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creditcard_id** | **str**| ID of the creditcard. | 
 **credit_card** | [**BuyerCreditCard**](BuyerCreditCard.md)|  | 

### Return type

[**BuyerCreditCard**](BuyerCreditCard.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_creditcards_get**
> ListBuyerCreditCard me_creditcards_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
search = 'search_example' # str | Search of the credit card. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the credit card. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the credit card. (optional)
page = 56 # int | Page of the credit card. (optional)
page_size = 56 # int | Page size of the credit card. (optional)

try: 
    response = MeApi.me_creditcards_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->me_creditcards_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search of the credit card. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the credit card. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the credit card. | [optional] 
 **page** | **int**| Page of the credit card. | [optional] 
 **page_size** | **int**| Page size of the credit card. | [optional] 

### Return type

[**ListBuyerCreditCard**](ListBuyerCreditCard.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_creditcards_post**
> BuyerCreditCard me_creditcards_post(credit_card)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
credit_card = OrderCloud.BuyerCreditCard() # BuyerCreditCard | 

try: 
    response = MeApi.me_creditcards_post(credit_card)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->me_creditcards_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_card** | [**BuyerCreditCard**](BuyerCreditCard.md)|  | 

### Return type

[**BuyerCreditCard**](BuyerCreditCard.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_get**
> MeUser me_get()



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi

try: 
    response = MeApi.me_get()
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->me_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MeUser**](MeUser.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_orders_approvable_get**
> ListOrder me_orders_approvable_get(_from=_from, to=to, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
_from = '_from_example' # str | Lower bound of date range that the order was created (if outgoing) or submitted (if incoming). (optional)
to = 'to_example' # str | Upper bound of date range that the order was created (if outgoing) or submitted (if incoming). (optional)
search = 'search_example' # str | Search of the order. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the order. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the order. (optional)
page = 56 # int | Page of the order. (optional)
page_size = 56 # int | Page size of the order. (optional)

try: 
    response = MeApi.me_orders_approvable_get(_from=_from, to=to, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->me_orders_approvable_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**| Lower bound of date range that the order was created (if outgoing) or submitted (if incoming). | [optional] 
 **to** | **str**| Upper bound of date range that the order was created (if outgoing) or submitted (if incoming). | [optional] 
 **search** | **str**| Search of the order. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the order. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the order. | [optional] 
 **page** | **int**| Page of the order. | [optional] 
 **page_size** | **int**| Page size of the order. | [optional] 

### Return type

[**ListOrder**](ListOrder.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_orders_get**
> ListOrder me_orders_get(_from=_from, to=to, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
_from = '_from_example' # str | Lower bound of date range that the order was created (if outgoing) or submitted (if incoming). (optional)
to = 'to_example' # str | Upper bound of date range that the order was created (if outgoing) or submitted (if incoming). (optional)
search = 'search_example' # str | Search of the order. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the order. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the order. (optional)
page = 56 # int | Page of the order. (optional)
page_size = 56 # int | Page size of the order. (optional)

try: 
    response = MeApi.me_orders_get(_from=_from, to=to, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->me_orders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**| Lower bound of date range that the order was created (if outgoing) or submitted (if incoming). | [optional] 
 **to** | **str**| Upper bound of date range that the order was created (if outgoing) or submitted (if incoming). | [optional] 
 **search** | **str**| Search of the order. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the order. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the order. | [optional] 
 **page** | **int**| Page of the order. | [optional] 
 **page_size** | **int**| Page size of the order. | [optional] 

### Return type

[**ListOrder**](ListOrder.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_orders_put**
> me_orders_put(anon_user_token)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
anon_user_token = 'anon_user_token_example' # str | Anon user token of the me.

try: 
    MeApi.me_orders_put(anon_user_token)
except ApiException as e:
    print("Exception when calling MeApi->me_orders_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anon_user_token** | **str**| Anon user token of the me. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_password_post**
> me_password_post(reset)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
reset = OrderCloud.TokenPasswordReset() # TokenPasswordReset | 

try: 
    MeApi.me_password_post(reset)
except ApiException as e:
    print("Exception when calling MeApi->me_password_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reset** | [**TokenPasswordReset**](TokenPasswordReset.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_patch**
> MeUser me_patch(user)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
user = OrderCloud.User() # User | 

try: 
    response = MeApi.me_patch(user)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->me_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)|  | 

### Return type

[**MeUser**](MeUser.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_products_get**
> ListBuyerProduct me_products_get(catalog_id=catalog_id, category_id=category_id, depth=depth, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
catalog_id = 'catalog_id_example' # str | ID of the catalog. (optional)
category_id = 'category_id_example' # str | ID of the category. (optional)
depth = 'depth_example' # str | Depth of the product. (optional)
search = 'search_example' # str | Search of the product. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the product. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the product. (optional)
page = 56 # int | Page of the product. (optional)
page_size = 56 # int | Page size of the product. (optional)

try: 
    response = MeApi.me_products_get(catalog_id=catalog_id, category_id=category_id, depth=depth, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->me_products_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | [optional] 
 **category_id** | **str**| ID of the category. | [optional] 
 **depth** | **str**| Depth of the product. | [optional] 
 **search** | **str**| Search of the product. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the product. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the product. | [optional] 
 **page** | **int**| Page of the product. | [optional] 
 **page_size** | **int**| Page size of the product. | [optional] 

### Return type

[**ListBuyerProduct**](ListBuyerProduct.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_products_product_id_get**
> BuyerProduct me_products_product_id_get(product_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
product_id = 'product_id_example' # str | ID of the product.

try: 
    response = MeApi.me_products_product_id_get(product_id)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->me_products_product_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of the product. | 

### Return type

[**BuyerProduct**](BuyerProduct.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_products_product_id_specs_get**
> ListBuyerSpec me_products_product_id_specs_get(product_id, catalog_id=catalog_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
product_id = 'product_id_example' # str | ID of the product.
catalog_id = 'catalog_id_example' # str | ID of the catalog. (optional)
search = 'search_example' # str | Search of the product. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the product. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the product. (optional)
page = 56 # int | Page of the product. (optional)
page_size = 56 # int | Page size of the product. (optional)

try: 
    response = MeApi.me_products_product_id_specs_get(product_id, catalog_id=catalog_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->me_products_product_id_specs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of the product. | 
 **catalog_id** | **str**| ID of the catalog. | [optional] 
 **search** | **str**| Search of the product. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the product. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the product. | [optional] 
 **page** | **int**| Page of the product. | [optional] 
 **page_size** | **int**| Page size of the product. | [optional] 

### Return type

[**ListBuyerSpec**](ListBuyerSpec.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_products_product_id_specs_spec_id_get**
> BuyerSpec me_products_product_id_specs_spec_id_get(product_id, spec_id, catalog_id=catalog_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
product_id = 'product_id_example' # str | ID of the product.
spec_id = 'spec_id_example' # str | ID of the spec.
catalog_id = 'catalog_id_example' # str | ID of the catalog. (optional)

try: 
    response = MeApi.me_products_product_id_specs_spec_id_get(product_id, spec_id, catalog_id=catalog_id)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->me_products_product_id_specs_spec_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of the product. | 
 **spec_id** | **str**| ID of the spec. | 
 **catalog_id** | **str**| ID of the catalog. | [optional] 

### Return type

[**BuyerSpec**](BuyerSpec.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_promotions_get**
> ListPromotion me_promotions_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
search = 'search_example' # str | Search of the promotion. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the promotion. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the promotion. (optional)
page = 56 # int | Page of the promotion. (optional)
page_size = 56 # int | Page size of the promotion. (optional)

try: 
    response = MeApi.me_promotions_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->me_promotions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search of the promotion. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the promotion. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the promotion. | [optional] 
 **page** | **int**| Page of the promotion. | [optional] 
 **page_size** | **int**| Page size of the promotion. | [optional] 

### Return type

[**ListPromotion**](ListPromotion.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_promotions_promotion_id_get**
> Promotion me_promotions_promotion_id_get(promotion_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
promotion_id = 'promotion_id_example' # str | ID of the promotion.

try: 
    response = MeApi.me_promotions_promotion_id_get(promotion_id)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->me_promotions_promotion_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **promotion_id** | **str**| ID of the promotion. | 

### Return type

[**Promotion**](Promotion.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_put**
> MeUser me_put(user)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
user = OrderCloud.User() # User | 

try: 
    response = MeApi.me_put(user)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->me_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)|  | 

### Return type

[**MeUser**](MeUser.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_register_put**
> object me_register_put(anon_user_token, user)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
anon_user_token = 'anon_user_token_example' # str | Anon user token of the me.
user = OrderCloud.User() # User | 

try: 
    response = MeApi.me_register_put(anon_user_token, user)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->me_register_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anon_user_token** | **str**| Anon user token of the me. | 
 **user** | [**User**](User.md)|  | 

### Return type

**object**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_shipments_get**
> ListBuyerShipment me_shipments_get(order_id=order_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
order_id = 'order_id_example' # str | ID of the order. (optional)
search = 'search_example' # str | Search of the shipment. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the shipment. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the shipment. (optional)
page = 56 # int | Page of the shipment. (optional)
page_size = 56 # int | Page size of the shipment. (optional)

try: 
    response = MeApi.me_shipments_get(order_id=order_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->me_shipments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| ID of the order. | [optional] 
 **search** | **str**| Search of the shipment. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the shipment. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the shipment. | [optional] 
 **page** | **int**| Page of the shipment. | [optional] 
 **page_size** | **int**| Page size of the shipment. | [optional] 

### Return type

[**ListBuyerShipment**](ListBuyerShipment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_shipments_shipment_id_get**
> BuyerShipment me_shipments_shipment_id_get(shipment_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
shipment_id = 'shipment_id_example' # str | ID of the shipment.

try: 
    response = MeApi.me_shipments_shipment_id_get(shipment_id)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->me_shipments_shipment_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| ID of the shipment. | 

### Return type

[**BuyerShipment**](BuyerShipment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_shipments_shipment_id_items_get**
> ListShipmentItem me_shipments_shipment_id_items_get(shipment_id, order_id=order_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
shipment_id = 'shipment_id_example' # str | ID of the shipment.
order_id = 'order_id_example' # str | ID of the order. (optional)
search = 'search_example' # str | Search of the shipment. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the shipment. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the shipment. (optional)
page = 56 # int | Page of the shipment. (optional)
page_size = 56 # int | Page size of the shipment. (optional)

try: 
    response = MeApi.me_shipments_shipment_id_items_get(shipment_id, order_id=order_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->me_shipments_shipment_id_items_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| ID of the shipment. | 
 **order_id** | **str**| ID of the order. | [optional] 
 **search** | **str**| Search of the shipment. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the shipment. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the shipment. | [optional] 
 **page** | **int**| Page of the shipment. | [optional] 
 **page_size** | **int**| Page size of the shipment. | [optional] 

### Return type

[**ListShipmentItem**](ListShipmentItem.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_spending_accounts_get**
> ListSpendingAccount me_spending_accounts_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
search = 'search_example' # str | Search of the spending account. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the spending account. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the spending account. (optional)
page = 56 # int | Page of the spending account. (optional)
page_size = 56 # int | Page size of the spending account. (optional)

try: 
    response = MeApi.me_spending_accounts_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->me_spending_accounts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search of the spending account. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the spending account. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the spending account. | [optional] 
 **page** | **int**| Page of the spending account. | [optional] 
 **page_size** | **int**| Page size of the spending account. | [optional] 

### Return type

[**ListSpendingAccount**](ListSpendingAccount.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_spendingaccounts_spending_account_id_get**
> SpendingAccount me_spendingaccounts_spending_account_id_get(spending_account_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
spending_account_id = 'spending_account_id_example' # str | ID of the spending account.

try: 
    response = MeApi.me_spendingaccounts_spending_account_id_get(spending_account_id)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->me_spendingaccounts_spending_account_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spending_account_id** | **str**| ID of the spending account. | 

### Return type

[**SpendingAccount**](SpendingAccount.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_usergroups_get**
> ListUserGroup me_usergroups_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
search = 'search_example' # str | Search of the user group. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the user group. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the user group. (optional)
page = 56 # int | Page of the user group. (optional)
page_size = 56 # int | Page size of the user group. (optional)

try: 
    response = MeApi.me_usergroups_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->me_usergroups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search of the user group. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the user group. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the user group. | [optional] 
 **page** | **int**| Page of the user group. | [optional] 
 **page_size** | **int**| Page size of the user group. | [optional] 

### Return type

[**ListUserGroup**](ListUserGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

