# OrderCloud.AddressApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buyers_buyer_id_addresses_address_id_assignments_delete**](AddressApi.md#buyers_buyer_id_addresses_address_id_assignments_delete) | **DELETE** /buyers/{buyerID}/addresses/{addressID}/assignments | 
[**buyers_buyer_id_addresses_address_id_delete**](AddressApi.md#buyers_buyer_id_addresses_address_id_delete) | **DELETE** /buyers/{buyerID}/addresses/{addressID} | 
[**buyers_buyer_id_addresses_address_id_get**](AddressApi.md#buyers_buyer_id_addresses_address_id_get) | **GET** /buyers/{buyerID}/addresses/{addressID} | 
[**buyers_buyer_id_addresses_address_id_patch**](AddressApi.md#buyers_buyer_id_addresses_address_id_patch) | **PATCH** /buyers/{buyerID}/addresses/{addressID} | 
[**buyers_buyer_id_addresses_address_id_put**](AddressApi.md#buyers_buyer_id_addresses_address_id_put) | **PUT** /buyers/{buyerID}/addresses/{addressID} | 
[**buyers_buyer_id_addresses_assignments_get**](AddressApi.md#buyers_buyer_id_addresses_assignments_get) | **GET** /buyers/{buyerID}/addresses/assignments | 
[**buyers_buyer_id_addresses_assignments_post**](AddressApi.md#buyers_buyer_id_addresses_assignments_post) | **POST** /buyers/{buyerID}/addresses/assignments | 
[**buyers_buyer_id_addresses_get**](AddressApi.md#buyers_buyer_id_addresses_get) | **GET** /buyers/{buyerID}/addresses | 
[**buyers_buyer_id_addresses_post**](AddressApi.md#buyers_buyer_id_addresses_post) | **POST** /buyers/{buyerID}/addresses | 


# **buyers_buyer_id_addresses_address_id_assignments_delete**
> buyers_buyer_id_addresses_address_id_assignments_delete(buyer_id, address_id, user_id=user_id, user_group_id=user_group_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AddressApi = OrderCloud.AddressApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
address_id = 'address_id_example' # str | ID of the address.
user_id = 'user_id_example' # str | ID of the user. (optional)
user_group_id = 'user_group_id_example' # str | ID of the user group. (optional)

try: 
    AddressApi.buyers_buyer_id_addresses_address_id_assignments_delete(buyer_id, address_id, user_id=user_id, user_group_id=user_group_id)
except ApiException as e:
    print("Exception when calling AddressApi->buyers_buyer_id_addresses_address_id_assignments_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **address_id** | **str**| ID of the address. | 
 **user_id** | **str**| ID of the user. | [optional] 
 **user_group_id** | **str**| ID of the user group. | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_addresses_address_id_delete**
> buyers_buyer_id_addresses_address_id_delete(buyer_id, address_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AddressApi = OrderCloud.AddressApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
address_id = 'address_id_example' # str | ID of the address.

try: 
    AddressApi.buyers_buyer_id_addresses_address_id_delete(buyer_id, address_id)
except ApiException as e:
    print("Exception when calling AddressApi->buyers_buyer_id_addresses_address_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **address_id** | **str**| ID of the address. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_addresses_address_id_get**
> Address buyers_buyer_id_addresses_address_id_get(buyer_id, address_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AddressApi = OrderCloud.AddressApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
address_id = 'address_id_example' # str | ID of the address.

try: 
    response = AddressApi.buyers_buyer_id_addresses_address_id_get(buyer_id, address_id)
    print(response)
except ApiException as e:
    print("Exception when calling AddressApi->buyers_buyer_id_addresses_address_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **address_id** | **str**| ID of the address. | 

### Return type

[**Address**](Address.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_addresses_address_id_patch**
> Address buyers_buyer_id_addresses_address_id_patch(buyer_id, address_id, address)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AddressApi = OrderCloud.AddressApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
address_id = 'address_id_example' # str | ID of the address.
address = OrderCloud.Address() # Address | 

try: 
    response = AddressApi.buyers_buyer_id_addresses_address_id_patch(buyer_id, address_id, address)
    print(response)
except ApiException as e:
    print("Exception when calling AddressApi->buyers_buyer_id_addresses_address_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **address_id** | **str**| ID of the address. | 
 **address** | [**Address**](Address.md)|  | 

### Return type

[**Address**](Address.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_addresses_address_id_put**
> Address buyers_buyer_id_addresses_address_id_put(buyer_id, address_id, address)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AddressApi = OrderCloud.AddressApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
address_id = 'address_id_example' # str | ID of the address.
address = OrderCloud.Address() # Address | 

try: 
    response = AddressApi.buyers_buyer_id_addresses_address_id_put(buyer_id, address_id, address)
    print(response)
except ApiException as e:
    print("Exception when calling AddressApi->buyers_buyer_id_addresses_address_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **address_id** | **str**| ID of the address. | 
 **address** | [**Address**](Address.md)|  | 

### Return type

[**Address**](Address.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_addresses_assignments_get**
> ListAddressAssignment buyers_buyer_id_addresses_assignments_get(buyer_id, address_id=address_id, user_id=user_id, user_group_id=user_group_id, level=level, is_shipping=is_shipping, is_billing=is_billing, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AddressApi = OrderCloud.AddressApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
address_id = 'address_id_example' # str | ID of the address. (optional)
user_id = 'user_id_example' # str | ID of the user. (optional)
user_group_id = 'user_group_id_example' # str | ID of the user group. (optional)
level = 'level_example' # str | Level of the address. (optional)
is_shipping = true # bool | Is shipping of the address. (optional)
is_billing = true # bool | Is billing of the address. (optional)
page = 56 # int | Page of the address. (optional)
page_size = 56 # int | Page size of the address. (optional)

try: 
    response = AddressApi.buyers_buyer_id_addresses_assignments_get(buyer_id, address_id=address_id, user_id=user_id, user_group_id=user_group_id, level=level, is_shipping=is_shipping, is_billing=is_billing, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling AddressApi->buyers_buyer_id_addresses_assignments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **address_id** | **str**| ID of the address. | [optional] 
 **user_id** | **str**| ID of the user. | [optional] 
 **user_group_id** | **str**| ID of the user group. | [optional] 
 **level** | **str**| Level of the address. | [optional] 
 **is_shipping** | **bool**| Is shipping of the address. | [optional] 
 **is_billing** | **bool**| Is billing of the address. | [optional] 
 **page** | **int**| Page of the address. | [optional] 
 **page_size** | **int**| Page size of the address. | [optional] 

### Return type

[**ListAddressAssignment**](ListAddressAssignment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_addresses_assignments_post**
> buyers_buyer_id_addresses_assignments_post(buyer_id, assignment)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AddressApi = OrderCloud.AddressApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
assignment = OrderCloud.AddressAssignment() # AddressAssignment | 

try: 
    AddressApi.buyers_buyer_id_addresses_assignments_post(buyer_id, assignment)
except ApiException as e:
    print("Exception when calling AddressApi->buyers_buyer_id_addresses_assignments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **assignment** | [**AddressAssignment**](AddressAssignment.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_addresses_get**
> ListAddress buyers_buyer_id_addresses_get(buyer_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AddressApi = OrderCloud.AddressApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
search = 'search_example' # str | Search of the address. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the address. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the address. (optional)
page = 56 # int | Page of the address. (optional)
page_size = 56 # int | Page size of the address. (optional)

try: 
    response = AddressApi.buyers_buyer_id_addresses_get(buyer_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling AddressApi->buyers_buyer_id_addresses_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **search** | **str**| Search of the address. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the address. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the address. | [optional] 
 **page** | **int**| Page of the address. | [optional] 
 **page_size** | **int**| Page size of the address. | [optional] 

### Return type

[**ListAddress**](ListAddress.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_addresses_post**
> Address buyers_buyer_id_addresses_post(buyer_id, address)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AddressApi = OrderCloud.AddressApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
address = OrderCloud.Address() # Address | 

try: 
    response = AddressApi.buyers_buyer_id_addresses_post(buyer_id, address)
    print(response)
except ApiException as e:
    print("Exception when calling AddressApi->buyers_buyer_id_addresses_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **address** | [**Address**](Address.md)|  | 

### Return type

[**Address**](Address.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

