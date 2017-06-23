# OrderCloud.AdminUserGroupApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usergroups_assignments_get**](AdminUserGroupApi.md#usergroups_assignments_get) | **GET** /usergroups/assignments | 
[**usergroups_assignments_post**](AdminUserGroupApi.md#usergroups_assignments_post) | **POST** /usergroups/assignments | 
[**usergroups_get**](AdminUserGroupApi.md#usergroups_get) | **GET** /usergroups | 
[**usergroups_post**](AdminUserGroupApi.md#usergroups_post) | **POST** /usergroups | 
[**usergroups_user_group_id_assignments_user_id_delete**](AdminUserGroupApi.md#usergroups_user_group_id_assignments_user_id_delete) | **DELETE** /usergroups/{userGroupID}/assignments/{userID} | 
[**usergroups_user_group_id_delete**](AdminUserGroupApi.md#usergroups_user_group_id_delete) | **DELETE** /usergroups/{userGroupID} | 
[**usergroups_user_group_id_get**](AdminUserGroupApi.md#usergroups_user_group_id_get) | **GET** /usergroups/{userGroupID} | 
[**usergroups_user_group_id_patch**](AdminUserGroupApi.md#usergroups_user_group_id_patch) | **PATCH** /usergroups/{userGroupID} | 
[**usergroups_user_group_id_put**](AdminUserGroupApi.md#usergroups_user_group_id_put) | **PUT** /usergroups/{userGroupID} | 


# **usergroups_assignments_get**
> ListUserGroupAssignment usergroups_assignments_get(user_group_id=user_group_id, user_id=user_id, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AdminUserGroupApi = OrderCloud.AdminUserGroupApi
user_group_id = 'user_group_id_example' # str | ID of the user group. (optional)
user_id = 'user_id_example' # str | ID of the user. (optional)
page = 56 # int | Page of the admin user group. (optional)
page_size = 56 # int | Page size of the admin user group. (optional)

try: 
    response = AdminUserGroupApi.usergroups_assignments_get(user_group_id=user_group_id, user_id=user_id, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling AdminUserGroupApi->usergroups_assignments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**| ID of the user group. | [optional] 
 **user_id** | **str**| ID of the user. | [optional] 
 **page** | **int**| Page of the admin user group. | [optional] 
 **page_size** | **int**| Page size of the admin user group. | [optional] 

### Return type

[**ListUserGroupAssignment**](ListUserGroupAssignment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usergroups_assignments_post**
> usergroups_assignments_post(user_group_assignment)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AdminUserGroupApi = OrderCloud.AdminUserGroupApi
user_group_assignment = OrderCloud.UserGroupAssignment() # UserGroupAssignment | 

try: 
    AdminUserGroupApi.usergroups_assignments_post(user_group_assignment)
except ApiException as e:
    print("Exception when calling AdminUserGroupApi->usergroups_assignments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_assignment** | [**UserGroupAssignment**](UserGroupAssignment.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usergroups_get**
> ListUserGroup usergroups_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AdminUserGroupApi = OrderCloud.AdminUserGroupApi
search = 'search_example' # str | Search of the admin user group. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the admin user group. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the admin user group. (optional)
page = 56 # int | Page of the admin user group. (optional)
page_size = 56 # int | Page size of the admin user group. (optional)

try: 
    response = AdminUserGroupApi.usergroups_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling AdminUserGroupApi->usergroups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search of the admin user group. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the admin user group. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the admin user group. | [optional] 
 **page** | **int**| Page of the admin user group. | [optional] 
 **page_size** | **int**| Page size of the admin user group. | [optional] 

### Return type

[**ListUserGroup**](ListUserGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usergroups_post**
> UserGroup usergroups_post(group)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AdminUserGroupApi = OrderCloud.AdminUserGroupApi
group = OrderCloud.UserGroup() # UserGroup | 

try: 
    response = AdminUserGroupApi.usergroups_post(group)
    print(response)
except ApiException as e:
    print("Exception when calling AdminUserGroupApi->usergroups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | [**UserGroup**](UserGroup.md)|  | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usergroups_user_group_id_assignments_user_id_delete**
> usergroups_user_group_id_assignments_user_id_delete(user_group_id, user_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AdminUserGroupApi = OrderCloud.AdminUserGroupApi
user_group_id = 'user_group_id_example' # str | ID of the user group.
user_id = 'user_id_example' # str | ID of the user.

try: 
    AdminUserGroupApi.usergroups_user_group_id_assignments_user_id_delete(user_group_id, user_id)
except ApiException as e:
    print("Exception when calling AdminUserGroupApi->usergroups_user_group_id_assignments_user_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**| ID of the user group. | 
 **user_id** | **str**| ID of the user. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usergroups_user_group_id_delete**
> usergroups_user_group_id_delete(user_group_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AdminUserGroupApi = OrderCloud.AdminUserGroupApi
user_group_id = 'user_group_id_example' # str | ID of the user group.

try: 
    AdminUserGroupApi.usergroups_user_group_id_delete(user_group_id)
except ApiException as e:
    print("Exception when calling AdminUserGroupApi->usergroups_user_group_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**| ID of the user group. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usergroups_user_group_id_get**
> UserGroup usergroups_user_group_id_get(user_group_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AdminUserGroupApi = OrderCloud.AdminUserGroupApi
user_group_id = 'user_group_id_example' # str | ID of the user group.

try: 
    response = AdminUserGroupApi.usergroups_user_group_id_get(user_group_id)
    print(response)
except ApiException as e:
    print("Exception when calling AdminUserGroupApi->usergroups_user_group_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**| ID of the user group. | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usergroups_user_group_id_patch**
> UserGroup usergroups_user_group_id_patch(user_group_id, group)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AdminUserGroupApi = OrderCloud.AdminUserGroupApi
user_group_id = 'user_group_id_example' # str | ID of the user group.
group = OrderCloud.UserGroup() # UserGroup | 

try: 
    response = AdminUserGroupApi.usergroups_user_group_id_patch(user_group_id, group)
    print(response)
except ApiException as e:
    print("Exception when calling AdminUserGroupApi->usergroups_user_group_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**| ID of the user group. | 
 **group** | [**UserGroup**](UserGroup.md)|  | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usergroups_user_group_id_put**
> UserGroup usergroups_user_group_id_put(user_group_id, group)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
AdminUserGroupApi = OrderCloud.AdminUserGroupApi
user_group_id = 'user_group_id_example' # str | ID of the user group.
group = OrderCloud.UserGroup() # UserGroup | 

try: 
    response = AdminUserGroupApi.usergroups_user_group_id_put(user_group_id, group)
    print(response)
except ApiException as e:
    print("Exception when calling AdminUserGroupApi->usergroups_user_group_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**| ID of the user group. | 
 **group** | [**UserGroup**](UserGroup.md)|  | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

