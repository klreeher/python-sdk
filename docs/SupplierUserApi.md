# OrderCloud.SupplierUserApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](SupplierUserApi.md#create) | **POST** /suppliers/{supplierID}/users | 
[**delete**](SupplierUserApi.md#delete) | **DELETE** /suppliers/{supplierID}/users/{userID} | 
[**get**](SupplierUserApi.md#get) | **GET** /suppliers/{supplierID}/users/{userID} | 
[**get_access_token**](SupplierUserApi.md#get_access_token) | **POST** /suppliers/{supplierID}/users/{userID}/accesstoken | 
[**list**](SupplierUserApi.md#list) | **GET** /suppliers/{supplierID}/users | 
[**patch**](SupplierUserApi.md#patch) | **PATCH** /suppliers/{supplierID}/users/{userID} | 
[**save**](SupplierUserApi.md#save) | **PUT** /suppliers/{supplierID}/users/{userID} | 


# **create**
> User create(supplier_id, user)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SupplierUserApi = OrderCloud.SupplierUserApi
supplier_id = 'supplier_id_example' # str | ID of the supplier.
user = OrderCloud.User() # User | 

try: 
    response = SupplierUserApi.create(supplier_id, user)
    print(response)
except ApiException as e:
    print("Exception when calling SupplierUserApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | **str**| ID of the supplier. | 
 **user** | [**User**](User.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(supplier_id, user_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SupplierUserApi = OrderCloud.SupplierUserApi
supplier_id = 'supplier_id_example' # str | ID of the supplier.
user_id = 'user_id_example' # str | ID of the user.

try: 
    SupplierUserApi.delete(supplier_id, user_id)
except ApiException as e:
    print("Exception when calling SupplierUserApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | **str**| ID of the supplier. | 
 **user_id** | **str**| ID of the user. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> User get(supplier_id, user_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SupplierUserApi = OrderCloud.SupplierUserApi
supplier_id = 'supplier_id_example' # str | ID of the supplier.
user_id = 'user_id_example' # str | ID of the user.

try: 
    response = SupplierUserApi.get(supplier_id, user_id)
    print(response)
except ApiException as e:
    print("Exception when calling SupplierUserApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | **str**| ID of the supplier. | 
 **user_id** | **str**| ID of the user. | 

### Return type

[**User**](User.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_token**
> AccessToken get_access_token(supplier_id, user_id, impersonate_token_request)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SupplierUserApi = OrderCloud.SupplierUserApi
supplier_id = 'supplier_id_example' # str | ID of the supplier.
user_id = 'user_id_example' # str | ID of the user.
impersonate_token_request = OrderCloud.ImpersonateTokenRequest() # ImpersonateTokenRequest | 

try: 
    response = SupplierUserApi.get_access_token(supplier_id, user_id, impersonate_token_request)
    print(response)
except ApiException as e:
    print("Exception when calling SupplierUserApi->get_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | **str**| ID of the supplier. | 
 **user_id** | **str**| ID of the user. | 
 **impersonate_token_request** | [**ImpersonateTokenRequest**](ImpersonateTokenRequest.md)|  | 

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ListUser list(supplier_id, user_group_id=user_group_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SupplierUserApi = OrderCloud.SupplierUserApi
supplier_id = 'supplier_id_example' # str | ID of the supplier.
user_group_id = 'user_group_id_example' # str | ID of the user group. (optional)
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = SupplierUserApi.list(supplier_id, user_group_id=user_group_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling SupplierUserApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | **str**| ID of the supplier. | 
 **user_group_id** | **str**| ID of the user group. | [optional] 
 **search** | **str**| Word or phrase to search for. | [optional] 
 **search_on** | **str**| Comma-delimited list of fields to search on. | [optional] 
 **sort_by** | **str**| Comma-delimited list of fields to sort by. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 
 **filters** | [**dict(str, str)**](str.md)| Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or &#39;xp.???&#39; | [optional] 

### Return type

[**ListUser**](ListUser.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch**
> User patch(supplier_id, user_id, partial_user)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SupplierUserApi = OrderCloud.SupplierUserApi
supplier_id = 'supplier_id_example' # str | ID of the supplier.
user_id = 'user_id_example' # str | ID of the user.
partial_user = OrderCloud.User() # User | 

try: 
    response = SupplierUserApi.patch(supplier_id, user_id, partial_user)
    print(response)
except ApiException as e:
    print("Exception when calling SupplierUserApi->patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | **str**| ID of the supplier. | 
 **user_id** | **str**| ID of the user. | 
 **partial_user** | [**User**](User.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save**
> User save(supplier_id, user_id, user)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SupplierUserApi = OrderCloud.SupplierUserApi
supplier_id = 'supplier_id_example' # str | ID of the supplier.
user_id = 'user_id_example' # str | ID of the user.
user = OrderCloud.User() # User | 

try: 
    response = SupplierUserApi.save(supplier_id, user_id, user)
    print(response)
except ApiException as e:
    print("Exception when calling SupplierUserApi->save: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | **str**| ID of the supplier. | 
 **user_id** | **str**| ID of the user. | 
 **user** | [**User**](User.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

