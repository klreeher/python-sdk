# OrderCloud.MeApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_address**](MeApi.md#create_address) | **POST** /me/addresses | 
[**create_credit_card**](MeApi.md#create_credit_card) | **POST** /me/creditcards | 
[**delete_address**](MeApi.md#delete_address) | **DELETE** /me/addresses/{addressID} | 
[**delete_credit_card**](MeApi.md#delete_credit_card) | **DELETE** /me/creditcards/{creditcardID} | 
[**get**](MeApi.md#get) | **GET** /me | 
[**get_address**](MeApi.md#get_address) | **GET** /me/addresses/{addressID} | 
[**get_credit_card**](MeApi.md#get_credit_card) | **GET** /me/creditcards/{creditcardID} | 
[**get_product**](MeApi.md#get_product) | **GET** /me/catalogs/{catalogID}/products/{productID} | 
[**get_promotion**](MeApi.md#get_promotion) | **GET** /me/promotions/{promotionID} | 
[**get_shipment**](MeApi.md#get_shipment) | **GET** /me/shipments/{shipmentID} | 
[**get_spec**](MeApi.md#get_spec) | **GET** /me/catalogs/{catalogID}/products/{productID}/specs/{specID} | 
[**get_spending_account**](MeApi.md#get_spending_account) | **GET** /me/spendingaccounts/{spendingAccountID} | 
[**list_addresses**](MeApi.md#list_addresses) | **GET** /me/addresses | 
[**list_approvable_orders**](MeApi.md#list_approvable_orders) | **GET** /me/orders/approvable | 
[**list_categories**](MeApi.md#list_categories) | **GET** /me/categories | 
[**list_cost_centers**](MeApi.md#list_cost_centers) | **GET** /me/costcenters | 
[**list_credit_cards**](MeApi.md#list_credit_cards) | **GET** /me/creditcards | 
[**list_orders**](MeApi.md#list_orders) | **GET** /me/orders | 
[**list_products**](MeApi.md#list_products) | **GET** /me/products | 
[**list_promotions**](MeApi.md#list_promotions) | **GET** /me/promotions | 
[**list_shipments**](MeApi.md#list_shipments) | **GET** /me/shipments | 
[**list_specs**](MeApi.md#list_specs) | **GET** /me/catalogs/{catalogID}/products/{productID}/specs | 
[**list_spending_accounts**](MeApi.md#list_spending_accounts) | **GET** /me/spendingAccounts | 
[**list_user_groups**](MeApi.md#list_user_groups) | **GET** /me/usergroups | 
[**patch**](MeApi.md#patch) | **PATCH** /me | 
[**patch_address**](MeApi.md#patch_address) | **PATCH** /me/addresses/{addressID} | 
[**patch_credit_card**](MeApi.md#patch_credit_card) | **PATCH** /me/creditcards/{creditcardID} | 
[**register**](MeApi.md#register) | **PUT** /me/register | 
[**reset_password_by_token**](MeApi.md#reset_password_by_token) | **POST** /me/password | 
[**transfer_anon_user_order**](MeApi.md#transfer_anon_user_order) | **PUT** /me/orders | 
[**update**](MeApi.md#update) | **PUT** /me | 
[**update_address**](MeApi.md#update_address) | **PUT** /me/addresses/{addressID} | 
[**update_credit_card**](MeApi.md#update_credit_card) | **PUT** /me/creditcards/{creditcardID} | 


# **create_address**
> BuyerAddress create_address(address)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
address = OrderCloud.BuyerAddress() # BuyerAddress | 

try: 
    response = MeApi.create_address(address)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->create_address: %s\n" % e)
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

# **create_credit_card**
> BuyerCreditCard create_credit_card(credit_card)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
credit_card = OrderCloud.BuyerCreditCard() # BuyerCreditCard | 

try: 
    response = MeApi.create_credit_card(credit_card)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->create_credit_card: %s\n" % e)
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

# **delete_address**
> delete_address(address_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
address_id = 'address_id_example' # str | ID of the address.

try: 
    MeApi.delete_address(address_id)
except ApiException as e:
    print("Exception when calling MeApi->delete_address: %s\n" % e)
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

# **delete_credit_card**
> delete_credit_card(creditcard_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
creditcard_id = 'creditcard_id_example' # str | ID of the creditcard.

try: 
    MeApi.delete_credit_card(creditcard_id)
except ApiException as e:
    print("Exception when calling MeApi->delete_credit_card: %s\n" % e)
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

# **get**
> User get()



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi

try: 
    response = MeApi.get()
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_address**
> BuyerAddress get_address(address_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
address_id = 'address_id_example' # str | ID of the address.

try: 
    response = MeApi.get_address(address_id)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->get_address: %s\n" % e)
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

# **get_credit_card**
> BuyerCreditCard get_credit_card(creditcard_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
creditcard_id = 'creditcard_id_example' # str | ID of the creditcard.

try: 
    response = MeApi.get_credit_card(creditcard_id)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->get_credit_card: %s\n" % e)
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

# **get_product**
> BuyerProduct get_product(catalog_id, product_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
catalog_id = 'catalog_id_example' # str | ID of the catalog.
product_id = 'product_id_example' # str | ID of the product.

try: 
    response = MeApi.get_product(catalog_id, product_id)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->get_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | 
 **product_id** | **str**| ID of the product. | 

### Return type

[**BuyerProduct**](BuyerProduct.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_promotion**
> Promotion get_promotion(promotion_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
promotion_id = 'promotion_id_example' # str | ID of the promotion.

try: 
    response = MeApi.get_promotion(promotion_id)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->get_promotion: %s\n" % e)
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

# **get_shipment**
> BuyerShipment get_shipment(shipment_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
shipment_id = 'shipment_id_example' # str | ID of the shipment.

try: 
    response = MeApi.get_shipment(shipment_id)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->get_shipment: %s\n" % e)
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

# **get_spec**
> BuyerSpec get_spec(catalog_id, product_id, spec_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
catalog_id = 'catalog_id_example' # str | ID of the catalog.
product_id = 'product_id_example' # str | ID of the product.
spec_id = 'spec_id_example' # str | ID of the spec.

try: 
    response = MeApi.get_spec(catalog_id, product_id, spec_id)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->get_spec: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | 
 **product_id** | **str**| ID of the product. | 
 **spec_id** | **str**| ID of the spec. | 

### Return type

[**BuyerSpec**](BuyerSpec.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spending_account**
> SpendingAccount get_spending_account(spending_account_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
spending_account_id = 'spending_account_id_example' # str | ID of the spending account.

try: 
    response = MeApi.get_spending_account(spending_account_id)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->get_spending_account: %s\n" % e)
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

# **list_addresses**
> ListBuyerAddress list_addresses(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = MeApi.list_addresses(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->list_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Word or phrase to search for. | [optional] 
 **search_on** | **str**| Comma-delimited list of fields to search on. | [optional] 
 **sort_by** | **str**| Comma-delimited list of fields to sort by. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 
 **filters** | [**dict(str, str)**](str.md)| Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or &#39;xp.???&#39; | [optional] 

### Return type

[**ListBuyerAddress**](ListBuyerAddress.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_approvable_orders**
> ListOrder list_approvable_orders(_from=_from, to=to, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
_from = '_from_example' # str | Lower bound of date range that the order was created (if outgoing) or submitted (if incoming). (optional)
to = 'to_example' # str | Upper bound of date range that the order was created (if outgoing) or submitted (if incoming). (optional)
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = MeApi.list_approvable_orders(_from=_from, to=to, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->list_approvable_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**| Lower bound of date range that the order was created (if outgoing) or submitted (if incoming). | [optional] 
 **to** | **str**| Upper bound of date range that the order was created (if outgoing) or submitted (if incoming). | [optional] 
 **search** | **str**| Word or phrase to search for. | [optional] 
 **search_on** | **str**| Comma-delimited list of fields to search on. | [optional] 
 **sort_by** | **str**| Comma-delimited list of fields to sort by. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 
 **filters** | [**dict(str, str)**](str.md)| Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or &#39;xp.???&#39; | [optional] 

### Return type

[**ListOrder**](ListOrder.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_categories**
> ListCategory list_categories(depth=depth, catalog_id=catalog_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
depth = 'depth_example' # str | Depth of the category. (optional)
catalog_id = 'catalog_id_example' # str | ID of the catalog. (optional)
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = MeApi.list_categories(depth=depth, catalog_id=catalog_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->list_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **depth** | **str**| Depth of the category. | [optional] 
 **catalog_id** | **str**| ID of the catalog. | [optional] 
 **search** | **str**| Word or phrase to search for. | [optional] 
 **search_on** | **str**| Comma-delimited list of fields to search on. | [optional] 
 **sort_by** | **str**| Comma-delimited list of fields to sort by. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 
 **filters** | [**dict(str, str)**](str.md)| Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or &#39;xp.???&#39; | [optional] 

### Return type

[**ListCategory**](ListCategory.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cost_centers**
> ListCostCenter list_cost_centers(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = MeApi.list_cost_centers(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->list_cost_centers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Word or phrase to search for. | [optional] 
 **search_on** | **str**| Comma-delimited list of fields to search on. | [optional] 
 **sort_by** | **str**| Comma-delimited list of fields to sort by. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 
 **filters** | [**dict(str, str)**](str.md)| Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or &#39;xp.???&#39; | [optional] 

### Return type

[**ListCostCenter**](ListCostCenter.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_credit_cards**
> ListBuyerCreditCard list_credit_cards(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = MeApi.list_credit_cards(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->list_credit_cards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Word or phrase to search for. | [optional] 
 **search_on** | **str**| Comma-delimited list of fields to search on. | [optional] 
 **sort_by** | **str**| Comma-delimited list of fields to sort by. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 
 **filters** | [**dict(str, str)**](str.md)| Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or &#39;xp.???&#39; | [optional] 

### Return type

[**ListBuyerCreditCard**](ListBuyerCreditCard.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_orders**
> ListOrder list_orders(_from=_from, to=to, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
_from = '_from_example' # str | Lower bound of date range that the order was created (if outgoing) or submitted (if incoming). (optional)
to = 'to_example' # str | Upper bound of date range that the order was created (if outgoing) or submitted (if incoming). (optional)
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = MeApi.list_orders(_from=_from, to=to, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->list_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**| Lower bound of date range that the order was created (if outgoing) or submitted (if incoming). | [optional] 
 **to** | **str**| Upper bound of date range that the order was created (if outgoing) or submitted (if incoming). | [optional] 
 **search** | **str**| Word or phrase to search for. | [optional] 
 **search_on** | **str**| Comma-delimited list of fields to search on. | [optional] 
 **sort_by** | **str**| Comma-delimited list of fields to sort by. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 
 **filters** | [**dict(str, str)**](str.md)| Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or &#39;xp.???&#39; | [optional] 

### Return type

[**ListOrder**](ListOrder.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_products**
> ListBuyerProduct list_products(catalog_id=catalog_id, category_id=category_id, depth=depth, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



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
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = MeApi.list_products(catalog_id=catalog_id, category_id=category_id, depth=depth, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->list_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | [optional] 
 **category_id** | **str**| ID of the category. | [optional] 
 **depth** | **str**| Depth of the product. | [optional] 
 **search** | **str**| Word or phrase to search for. | [optional] 
 **search_on** | **str**| Comma-delimited list of fields to search on. | [optional] 
 **sort_by** | **str**| Comma-delimited list of fields to sort by. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 
 **filters** | [**dict(str, str)**](str.md)| Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or &#39;xp.???&#39; | [optional] 

### Return type

[**ListBuyerProduct**](ListBuyerProduct.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_promotions**
> ListPromotion list_promotions(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = MeApi.list_promotions(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->list_promotions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Word or phrase to search for. | [optional] 
 **search_on** | **str**| Comma-delimited list of fields to search on. | [optional] 
 **sort_by** | **str**| Comma-delimited list of fields to sort by. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 
 **filters** | [**dict(str, str)**](str.md)| Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or &#39;xp.???&#39; | [optional] 

### Return type

[**ListPromotion**](ListPromotion.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_shipments**
> ListBuyerShipment list_shipments(order_id=order_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
order_id = 'order_id_example' # str | ID of the order. (optional)
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = MeApi.list_shipments(order_id=order_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->list_shipments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| ID of the order. | [optional] 
 **search** | **str**| Word or phrase to search for. | [optional] 
 **search_on** | **str**| Comma-delimited list of fields to search on. | [optional] 
 **sort_by** | **str**| Comma-delimited list of fields to sort by. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 
 **filters** | [**dict(str, str)**](str.md)| Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or &#39;xp.???&#39; | [optional] 

### Return type

[**ListBuyerShipment**](ListBuyerShipment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_specs**
> ListBuyerSpec list_specs(catalog_id, product_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
catalog_id = 'catalog_id_example' # str | ID of the catalog.
product_id = 'product_id_example' # str | ID of the product.
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = MeApi.list_specs(catalog_id, product_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->list_specs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | 
 **product_id** | **str**| ID of the product. | 
 **search** | **str**| Word or phrase to search for. | [optional] 
 **search_on** | **str**| Comma-delimited list of fields to search on. | [optional] 
 **sort_by** | **str**| Comma-delimited list of fields to sort by. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 
 **filters** | [**dict(str, str)**](str.md)| Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or &#39;xp.???&#39; | [optional] 

### Return type

[**ListBuyerSpec**](ListBuyerSpec.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_spending_accounts**
> ListSpendingAccount list_spending_accounts(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = MeApi.list_spending_accounts(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->list_spending_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Word or phrase to search for. | [optional] 
 **search_on** | **str**| Comma-delimited list of fields to search on. | [optional] 
 **sort_by** | **str**| Comma-delimited list of fields to sort by. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 
 **filters** | [**dict(str, str)**](str.md)| Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or &#39;xp.???&#39; | [optional] 

### Return type

[**ListSpendingAccount**](ListSpendingAccount.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_groups**
> ListUserGroup list_user_groups(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = MeApi.list_user_groups(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->list_user_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Word or phrase to search for. | [optional] 
 **search_on** | **str**| Comma-delimited list of fields to search on. | [optional] 
 **sort_by** | **str**| Comma-delimited list of fields to sort by. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 
 **filters** | [**dict(str, str)**](str.md)| Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or &#39;xp.???&#39; | [optional] 

### Return type

[**ListUserGroup**](ListUserGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch**
> User patch(user)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
user = OrderCloud.User() # User | 

try: 
    response = MeApi.patch(user)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_address**
> patch_address(address_id, address)



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
    MeApi.patch_address(address_id, address)
except ApiException as e:
    print("Exception when calling MeApi->patch_address: %s\n" % e)
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

# **patch_credit_card**
> patch_credit_card(creditcard_id, credit_card)



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
    MeApi.patch_credit_card(creditcard_id, credit_card)
except ApiException as e:
    print("Exception when calling MeApi->patch_credit_card: %s\n" % e)
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

# **register**
> object register(anon_user_token, user)



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
    response = MeApi.register(anon_user_token, user)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->register: %s\n" % e)
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

# **reset_password_by_token**
> reset_password_by_token(reset)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
reset = OrderCloud.TokenPasswordReset() # TokenPasswordReset | 

try: 
    MeApi.reset_password_by_token(reset)
except ApiException as e:
    print("Exception when calling MeApi->reset_password_by_token: %s\n" % e)
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

# **transfer_anon_user_order**
> transfer_anon_user_order(anon_user_token)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
anon_user_token = 'anon_user_token_example' # str | Anon user token of the me.

try: 
    MeApi.transfer_anon_user_order(anon_user_token)
except ApiException as e:
    print("Exception when calling MeApi->transfer_anon_user_order: %s\n" % e)
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

# **update**
> User update(user)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MeApi = OrderCloud.MeApi
user = OrderCloud.User() # User | 

try: 
    response = MeApi.update(user)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_address**
> BuyerAddress update_address(address_id, address)



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
    response = MeApi.update_address(address_id, address)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->update_address: %s\n" % e)
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

# **update_credit_card**
> BuyerCreditCard update_credit_card(creditcard_id, credit_card)



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
    response = MeApi.update_credit_card(creditcard_id, credit_card)
    print(response)
except ApiException as e:
    print("Exception when calling MeApi->update_credit_card: %s\n" % e)
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

