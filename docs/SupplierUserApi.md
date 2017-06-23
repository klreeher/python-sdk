# OrderCloud.SupplierUserApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**suppliers_supplier_id_users_get**](SupplierUserApi.md#suppliers_supplier_id_users_get) | **GET** /suppliers/{supplierID}/users | 
[**suppliers_supplier_id_users_post**](SupplierUserApi.md#suppliers_supplier_id_users_post) | **POST** /suppliers/{supplierID}/users | 
[**suppliers_supplier_id_users_user_id_accesstoken_post**](SupplierUserApi.md#suppliers_supplier_id_users_user_id_accesstoken_post) | **POST** /suppliers/{supplierID}/users/{userID}/accesstoken | 
[**suppliers_supplier_id_users_user_id_delete**](SupplierUserApi.md#suppliers_supplier_id_users_user_id_delete) | **DELETE** /suppliers/{supplierID}/users/{userID} | 
[**suppliers_supplier_id_users_user_id_get**](SupplierUserApi.md#suppliers_supplier_id_users_user_id_get) | **GET** /suppliers/{supplierID}/users/{userID} | 
[**suppliers_supplier_id_users_user_id_patch**](SupplierUserApi.md#suppliers_supplier_id_users_user_id_patch) | **PATCH** /suppliers/{supplierID}/users/{userID} | 
[**suppliers_supplier_id_users_user_id_put**](SupplierUserApi.md#suppliers_supplier_id_users_user_id_put) | **PUT** /suppliers/{supplierID}/users/{userID} | 


# **suppliers_supplier_id_users_get**
> ListUser suppliers_supplier_id_users_get(supplier_id, user_group_id=user_group_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SupplierUserApi = OrderCloud.SupplierUserApi
supplier_id = 'supplier_id_example' # str | ID of the supplier.
user_group_id = 'user_group_id_example' # str | ID of the user group. (optional)
search = 'search_example' # str | Search of the supplier user. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the supplier user. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the supplier user. (optional)
page = 56 # int | Page of the supplier user. (optional)
page_size = 56 # int | Page size of the supplier user. (optional)

try: 
    response = SupplierUserApi.suppliers_supplier_id_users_get(supplier_id, user_group_id=user_group_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling SupplierUserApi->suppliers_supplier_id_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | **str**| ID of the supplier. | 
 **user_group_id** | **str**| ID of the user group. | [optional] 
 **search** | **str**| Search of the supplier user. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the supplier user. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the supplier user. | [optional] 
 **page** | **int**| Page of the supplier user. | [optional] 
 **page_size** | **int**| Page size of the supplier user. | [optional] 

### Return type

[**ListUser**](ListUser.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppliers_supplier_id_users_post**
> User suppliers_supplier_id_users_post(supplier_id, user)



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
    response = SupplierUserApi.suppliers_supplier_id_users_post(supplier_id, user)
    print(response)
except ApiException as e:
    print("Exception when calling SupplierUserApi->suppliers_supplier_id_users_post: %s\n" % e)
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

# **suppliers_supplier_id_users_user_id_accesstoken_post**
> AccessToken suppliers_supplier_id_users_user_id_accesstoken_post(supplier_id, user_id, token_request)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SupplierUserApi = OrderCloud.SupplierUserApi
supplier_id = 'supplier_id_example' # str | ID of the supplier.
user_id = 'user_id_example' # str | ID of the user.
token_request = OrderCloud.ImpersonateTokenRequest() # ImpersonateTokenRequest | 

try: 
    response = SupplierUserApi.suppliers_supplier_id_users_user_id_accesstoken_post(supplier_id, user_id, token_request)
    print(response)
except ApiException as e:
    print("Exception when calling SupplierUserApi->suppliers_supplier_id_users_user_id_accesstoken_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | **str**| ID of the supplier. | 
 **user_id** | **str**| ID of the user. | 
 **token_request** | [**ImpersonateTokenRequest**](ImpersonateTokenRequest.md)|  | 

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppliers_supplier_id_users_user_id_delete**
> suppliers_supplier_id_users_user_id_delete(supplier_id, user_id)



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
    SupplierUserApi.suppliers_supplier_id_users_user_id_delete(supplier_id, user_id)
except ApiException as e:
    print("Exception when calling SupplierUserApi->suppliers_supplier_id_users_user_id_delete: %s\n" % e)
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

# **suppliers_supplier_id_users_user_id_get**
> User suppliers_supplier_id_users_user_id_get(supplier_id, user_id)



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
    response = SupplierUserApi.suppliers_supplier_id_users_user_id_get(supplier_id, user_id)
    print(response)
except ApiException as e:
    print("Exception when calling SupplierUserApi->suppliers_supplier_id_users_user_id_get: %s\n" % e)
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

# **suppliers_supplier_id_users_user_id_patch**
> User suppliers_supplier_id_users_user_id_patch(supplier_id, user_id, user)



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
    response = SupplierUserApi.suppliers_supplier_id_users_user_id_patch(supplier_id, user_id, user)
    print(response)
except ApiException as e:
    print("Exception when calling SupplierUserApi->suppliers_supplier_id_users_user_id_patch: %s\n" % e)
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

# **suppliers_supplier_id_users_user_id_put**
> User suppliers_supplier_id_users_user_id_put(supplier_id, user_id, user)



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
    response = SupplierUserApi.suppliers_supplier_id_users_user_id_put(supplier_id, user_id, user)
    print(response)
except ApiException as e:
    print("Exception when calling SupplierUserApi->suppliers_supplier_id_users_user_id_put: %s\n" % e)
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

