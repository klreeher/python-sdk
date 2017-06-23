# OrderCloud.AdminAddressApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addresses_address_id_delete**](AdminAddressApi.md#addresses_address_id_delete) | **DELETE** /addresses/{addressID} | 
[**addresses_address_id_get**](AdminAddressApi.md#addresses_address_id_get) | **GET** /addresses/{addressID} | 
[**addresses_address_id_patch**](AdminAddressApi.md#addresses_address_id_patch) | **PATCH** /addresses/{addressID} | 
[**addresses_address_id_put**](AdminAddressApi.md#addresses_address_id_put) | **PUT** /addresses/{addressID} | 
[**addresses_get**](AdminAddressApi.md#addresses_get) | **GET** /addresses | 
[**addresses_post**](AdminAddressApi.md#addresses_post) | **POST** /addresses | 


# **addresses_address_id_delete**
> addresses_address_id_delete(address_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AdminAddressApi = OrderCloud.AdminAddressApi
address_id = 'address_id_example' # str | ID of the address.

try: 
    AdminAddressApi.addresses_address_id_delete(address_id)
except ApiException as e:
    print("Exception when calling AdminAddressApi->addresses_address_id_delete: %s\n" % e)
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

# **addresses_address_id_get**
> Address addresses_address_id_get(address_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AdminAddressApi = OrderCloud.AdminAddressApi
address_id = 'address_id_example' # str | ID of the address.

try: 
    response = AdminAddressApi.addresses_address_id_get(address_id)
    print(response)
except ApiException as e:
    print("Exception when calling AdminAddressApi->addresses_address_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_id** | **str**| ID of the address. | 

### Return type

[**Address**](Address.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addresses_address_id_patch**
> Address addresses_address_id_patch(address_id, address)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AdminAddressApi = OrderCloud.AdminAddressApi
address_id = 'address_id_example' # str | ID of the address.
address = OrderCloud.Address() # Address | 

try: 
    response = AdminAddressApi.addresses_address_id_patch(address_id, address)
    print(response)
except ApiException as e:
    print("Exception when calling AdminAddressApi->addresses_address_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **addresses_address_id_put**
> Address addresses_address_id_put(address_id, address)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AdminAddressApi = OrderCloud.AdminAddressApi
address_id = 'address_id_example' # str | ID of the address.
address = OrderCloud.Address() # Address | 

try: 
    response = AdminAddressApi.addresses_address_id_put(address_id, address)
    print(response)
except ApiException as e:
    print("Exception when calling AdminAddressApi->addresses_address_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **addresses_get**
> ListAddress addresses_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AdminAddressApi = OrderCloud.AdminAddressApi
search = 'search_example' # str | Search of the admin address. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the admin address. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the admin address. (optional)
page = 56 # int | Page of the admin address. (optional)
page_size = 56 # int | Page size of the admin address. (optional)

try: 
    response = AdminAddressApi.addresses_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling AdminAddressApi->addresses_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search of the admin address. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the admin address. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the admin address. | [optional] 
 **page** | **int**| Page of the admin address. | [optional] 
 **page_size** | **int**| Page size of the admin address. | [optional] 

### Return type

[**ListAddress**](ListAddress.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addresses_post**
> Address addresses_post(address)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AdminAddressApi = OrderCloud.AdminAddressApi
address = OrderCloud.Address() # Address | 

try: 
    response = AdminAddressApi.addresses_post(address)
    print(response)
except ApiException as e:
    print("Exception when calling AdminAddressApi->addresses_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | [**Address**](Address.md)|  | 

### Return type

[**Address**](Address.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

