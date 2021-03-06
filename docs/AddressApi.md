# OrderCloud.AddressApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](AddressApi.md#create) | **POST** /buyers/{buyerID}/addresses | 
[**delete**](AddressApi.md#delete) | **DELETE** /buyers/{buyerID}/addresses/{addressID} | 
[**delete_assignment**](AddressApi.md#delete_assignment) | **DELETE** /buyers/{buyerID}/addresses/{addressID}/assignments | 
[**get**](AddressApi.md#get) | **GET** /buyers/{buyerID}/addresses/{addressID} | 
[**list**](AddressApi.md#list) | **GET** /buyers/{buyerID}/addresses | 
[**list_assignments**](AddressApi.md#list_assignments) | **GET** /buyers/{buyerID}/addresses/assignments | 
[**patch**](AddressApi.md#patch) | **PATCH** /buyers/{buyerID}/addresses/{addressID} | 
[**save**](AddressApi.md#save) | **PUT** /buyers/{buyerID}/addresses/{addressID} | 
[**save_assignment**](AddressApi.md#save_assignment) | **POST** /buyers/{buyerID}/addresses/assignments | 


# **create**
> Address create(buyer_id, address)



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
    response = AddressApi.create(buyer_id, address)
    print(response)
except ApiException as e:
    print("Exception when calling AddressApi->create: %s\n" % e)
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

# **delete**
> delete(buyer_id, address_id)



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
    AddressApi.delete(buyer_id, address_id)
except ApiException as e:
    print("Exception when calling AddressApi->delete: %s\n" % e)
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

# **delete_assignment**
> delete_assignment(buyer_id, address_id, user_id=user_id, user_group_id=user_group_id)



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
    AddressApi.delete_assignment(buyer_id, address_id, user_id=user_id, user_group_id=user_group_id)
except ApiException as e:
    print("Exception when calling AddressApi->delete_assignment: %s\n" % e)
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

# **get**
> Address get(buyer_id, address_id)



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
    response = AddressApi.get(buyer_id, address_id)
    print(response)
except ApiException as e:
    print("Exception when calling AddressApi->get: %s\n" % e)
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

# **list**
> ListAddress list(buyer_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AddressApi = OrderCloud.AddressApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = AddressApi.list(buyer_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling AddressApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **search** | **str**| Word or phrase to search for. | [optional] 
 **search_on** | **str**| Comma-delimited list of fields to search on. | [optional] 
 **sort_by** | **str**| Comma-delimited list of fields to sort by. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 
 **filters** | [**dict(str, str)**](str.md)| Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or &#39;xp.???&#39; | [optional] 

### Return type

[**ListAddress**](ListAddress.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assignments**
> ListAddressAssignment list_assignments(buyer_id, address_id=address_id, user_id=user_id, user_group_id=user_group_id, level=level, is_shipping=is_shipping, is_billing=is_billing, page=page, page_size=page_size)



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
level = 'level_example' # str | Level of the address assignment. Possible values: User, Group, Company. (optional)
is_shipping = true # bool | Is shipping of the address assignment. (optional)
is_billing = true # bool | Is billing of the address assignment. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)

try: 
    response = AddressApi.list_assignments(buyer_id, address_id=address_id, user_id=user_id, user_group_id=user_group_id, level=level, is_shipping=is_shipping, is_billing=is_billing, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling AddressApi->list_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **address_id** | **str**| ID of the address. | [optional] 
 **user_id** | **str**| ID of the user. | [optional] 
 **user_group_id** | **str**| ID of the user group. | [optional] 
 **level** | **str**| Level of the address assignment. Possible values: User, Group, Company. | [optional] 
 **is_shipping** | **bool**| Is shipping of the address assignment. | [optional] 
 **is_billing** | **bool**| Is billing of the address assignment. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 

### Return type

[**ListAddressAssignment**](ListAddressAssignment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch**
> Address patch(buyer_id, address_id, partial_address)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AddressApi = OrderCloud.AddressApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
address_id = 'address_id_example' # str | ID of the address.
partial_address = OrderCloud.Address() # Address | 

try: 
    response = AddressApi.patch(buyer_id, address_id, partial_address)
    print(response)
except ApiException as e:
    print("Exception when calling AddressApi->patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **address_id** | **str**| ID of the address. | 
 **partial_address** | [**Address**](Address.md)|  | 

### Return type

[**Address**](Address.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save**
> Address save(buyer_id, address_id, address)



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
    response = AddressApi.save(buyer_id, address_id, address)
    print(response)
except ApiException as e:
    print("Exception when calling AddressApi->save: %s\n" % e)
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

# **save_assignment**
> save_assignment(buyer_id, address_assignment)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AddressApi = OrderCloud.AddressApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
address_assignment = OrderCloud.AddressAssignment() # AddressAssignment | 

try: 
    AddressApi.save_assignment(buyer_id, address_assignment)
except ApiException as e:
    print("Exception when calling AddressApi->save_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **address_assignment** | [**AddressAssignment**](AddressAssignment.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

