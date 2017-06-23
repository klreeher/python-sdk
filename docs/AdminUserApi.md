# OrderCloud.AdminUserApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminusers_get**](AdminUserApi.md#adminusers_get) | **GET** /adminusers | 
[**adminusers_post**](AdminUserApi.md#adminusers_post) | **POST** /adminusers | 
[**adminusers_user_id_delete**](AdminUserApi.md#adminusers_user_id_delete) | **DELETE** /adminusers/{userID} | 
[**adminusers_user_id_get**](AdminUserApi.md#adminusers_user_id_get) | **GET** /adminusers/{userID} | 
[**adminusers_user_id_patch**](AdminUserApi.md#adminusers_user_id_patch) | **PATCH** /adminusers/{userID} | 
[**adminusers_user_id_put**](AdminUserApi.md#adminusers_user_id_put) | **PUT** /adminusers/{userID} | 


# **adminusers_get**
> ListUser adminusers_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AdminUserApi = OrderCloud.AdminUserApi
search = 'search_example' # str | Search of the admin user. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the admin user. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the admin user. (optional)
page = 56 # int | Page of the admin user. (optional)
page_size = 56 # int | Page size of the admin user. (optional)

try: 
    response = AdminUserApi.adminusers_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling AdminUserApi->adminusers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search of the admin user. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the admin user. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the admin user. | [optional] 
 **page** | **int**| Page of the admin user. | [optional] 
 **page_size** | **int**| Page size of the admin user. | [optional] 

### Return type

[**ListUser**](ListUser.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **adminusers_post**
> User adminusers_post(user)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AdminUserApi = OrderCloud.AdminUserApi
user = OrderCloud.User() # User | 

try: 
    response = AdminUserApi.adminusers_post(user)
    print(response)
except ApiException as e:
    print("Exception when calling AdminUserApi->adminusers_post: %s\n" % e)
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

# **adminusers_user_id_delete**
> adminusers_user_id_delete(user_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AdminUserApi = OrderCloud.AdminUserApi
user_id = 'user_id_example' # str | ID of the user.

try: 
    AdminUserApi.adminusers_user_id_delete(user_id)
except ApiException as e:
    print("Exception when calling AdminUserApi->adminusers_user_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of the user. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **adminusers_user_id_get**
> User adminusers_user_id_get(user_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AdminUserApi = OrderCloud.AdminUserApi
user_id = 'user_id_example' # str | ID of the user.

try: 
    response = AdminUserApi.adminusers_user_id_get(user_id)
    print(response)
except ApiException as e:
    print("Exception when calling AdminUserApi->adminusers_user_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of the user. | 

### Return type

[**User**](User.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **adminusers_user_id_patch**
> User adminusers_user_id_patch(user_id, user)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AdminUserApi = OrderCloud.AdminUserApi
user_id = 'user_id_example' # str | ID of the user.
user = OrderCloud.User() # User | 

try: 
    response = AdminUserApi.adminusers_user_id_patch(user_id, user)
    print(response)
except ApiException as e:
    print("Exception when calling AdminUserApi->adminusers_user_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **adminusers_user_id_put**
> User adminusers_user_id_put(user_id, user)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AdminUserApi = OrderCloud.AdminUserApi
user_id = 'user_id_example' # str | ID of the user.
user = OrderCloud.User() # User | 

try: 
    response = AdminUserApi.adminusers_user_id_put(user_id, user)
    print(response)
except ApiException as e:
    print("Exception when calling AdminUserApi->adminusers_user_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

