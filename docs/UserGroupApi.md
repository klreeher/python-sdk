# OrderCloud.UserGroupApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buyers_buyer_id_usergroups_assignments_get**](UserGroupApi.md#buyers_buyer_id_usergroups_assignments_get) | **GET** /buyers/{buyerID}/usergroups/assignments | 
[**buyers_buyer_id_usergroups_assignments_post**](UserGroupApi.md#buyers_buyer_id_usergroups_assignments_post) | **POST** /buyers/{buyerID}/usergroups/assignments | 
[**buyers_buyer_id_usergroups_get**](UserGroupApi.md#buyers_buyer_id_usergroups_get) | **GET** /buyers/{buyerID}/usergroups | 
[**buyers_buyer_id_usergroups_post**](UserGroupApi.md#buyers_buyer_id_usergroups_post) | **POST** /buyers/{buyerID}/usergroups | 
[**buyers_buyer_id_usergroups_user_group_id_assignments_user_id_delete**](UserGroupApi.md#buyers_buyer_id_usergroups_user_group_id_assignments_user_id_delete) | **DELETE** /buyers/{buyerID}/usergroups/{userGroupID}/assignments/{userID} | 
[**buyers_buyer_id_usergroups_user_group_id_delete**](UserGroupApi.md#buyers_buyer_id_usergroups_user_group_id_delete) | **DELETE** /buyers/{buyerID}/usergroups/{userGroupID} | 
[**buyers_buyer_id_usergroups_user_group_id_get**](UserGroupApi.md#buyers_buyer_id_usergroups_user_group_id_get) | **GET** /buyers/{buyerID}/usergroups/{userGroupID} | 
[**buyers_buyer_id_usergroups_user_group_id_patch**](UserGroupApi.md#buyers_buyer_id_usergroups_user_group_id_patch) | **PATCH** /buyers/{buyerID}/usergroups/{userGroupID} | 
[**buyers_buyer_id_usergroups_user_group_id_put**](UserGroupApi.md#buyers_buyer_id_usergroups_user_group_id_put) | **PUT** /buyers/{buyerID}/usergroups/{userGroupID} | 


# **buyers_buyer_id_usergroups_assignments_get**
> ListUserGroupAssignment buyers_buyer_id_usergroups_assignments_get(buyer_id, user_group_id=user_group_id, user_id=user_id, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
UserGroupApi = OrderCloud.UserGroupApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
user_group_id = 'user_group_id_example' # str | ID of the user group. (optional)
user_id = 'user_id_example' # str | ID of the user. (optional)
page = 56 # int | Page of the user group. (optional)
page_size = 56 # int | Page size of the user group. (optional)

try: 
    response = UserGroupApi.buyers_buyer_id_usergroups_assignments_get(buyer_id, user_group_id=user_group_id, user_id=user_id, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling UserGroupApi->buyers_buyer_id_usergroups_assignments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **user_group_id** | **str**| ID of the user group. | [optional] 
 **user_id** | **str**| ID of the user. | [optional] 
 **page** | **int**| Page of the user group. | [optional] 
 **page_size** | **int**| Page size of the user group. | [optional] 

### Return type

[**ListUserGroupAssignment**](ListUserGroupAssignment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_usergroups_assignments_post**
> buyers_buyer_id_usergroups_assignments_post(buyer_id, user_group_assignment)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
UserGroupApi = OrderCloud.UserGroupApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
user_group_assignment = OrderCloud.UserGroupAssignment() # UserGroupAssignment | 

try: 
    UserGroupApi.buyers_buyer_id_usergroups_assignments_post(buyer_id, user_group_assignment)
except ApiException as e:
    print("Exception when calling UserGroupApi->buyers_buyer_id_usergroups_assignments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **user_group_assignment** | [**UserGroupAssignment**](UserGroupAssignment.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_usergroups_get**
> ListUserGroup buyers_buyer_id_usergroups_get(buyer_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
UserGroupApi = OrderCloud.UserGroupApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
search = 'search_example' # str | Search of the user group. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the user group. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the user group. (optional)
page = 56 # int | Page of the user group. (optional)
page_size = 56 # int | Page size of the user group. (optional)

try: 
    response = UserGroupApi.buyers_buyer_id_usergroups_get(buyer_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling UserGroupApi->buyers_buyer_id_usergroups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
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

# **buyers_buyer_id_usergroups_post**
> UserGroup buyers_buyer_id_usergroups_post(buyer_id, group)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
UserGroupApi = OrderCloud.UserGroupApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
group = OrderCloud.UserGroup() # UserGroup | 

try: 
    response = UserGroupApi.buyers_buyer_id_usergroups_post(buyer_id, group)
    print(response)
except ApiException as e:
    print("Exception when calling UserGroupApi->buyers_buyer_id_usergroups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **group** | [**UserGroup**](UserGroup.md)|  | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_usergroups_user_group_id_assignments_user_id_delete**
> buyers_buyer_id_usergroups_user_group_id_assignments_user_id_delete(buyer_id, user_group_id, user_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
UserGroupApi = OrderCloud.UserGroupApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
user_group_id = 'user_group_id_example' # str | ID of the user group.
user_id = 'user_id_example' # str | ID of the user.

try: 
    UserGroupApi.buyers_buyer_id_usergroups_user_group_id_assignments_user_id_delete(buyer_id, user_group_id, user_id)
except ApiException as e:
    print("Exception when calling UserGroupApi->buyers_buyer_id_usergroups_user_group_id_assignments_user_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
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

# **buyers_buyer_id_usergroups_user_group_id_delete**
> buyers_buyer_id_usergroups_user_group_id_delete(buyer_id, user_group_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
UserGroupApi = OrderCloud.UserGroupApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
user_group_id = 'user_group_id_example' # str | ID of the user group.

try: 
    UserGroupApi.buyers_buyer_id_usergroups_user_group_id_delete(buyer_id, user_group_id)
except ApiException as e:
    print("Exception when calling UserGroupApi->buyers_buyer_id_usergroups_user_group_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **user_group_id** | **str**| ID of the user group. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_usergroups_user_group_id_get**
> UserGroup buyers_buyer_id_usergroups_user_group_id_get(buyer_id, user_group_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
UserGroupApi = OrderCloud.UserGroupApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
user_group_id = 'user_group_id_example' # str | ID of the user group.

try: 
    response = UserGroupApi.buyers_buyer_id_usergroups_user_group_id_get(buyer_id, user_group_id)
    print(response)
except ApiException as e:
    print("Exception when calling UserGroupApi->buyers_buyer_id_usergroups_user_group_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **user_group_id** | **str**| ID of the user group. | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_usergroups_user_group_id_patch**
> UserGroup buyers_buyer_id_usergroups_user_group_id_patch(buyer_id, user_group_id, group)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
UserGroupApi = OrderCloud.UserGroupApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
user_group_id = 'user_group_id_example' # str | ID of the user group.
group = OrderCloud.UserGroup() # UserGroup | 

try: 
    response = UserGroupApi.buyers_buyer_id_usergroups_user_group_id_patch(buyer_id, user_group_id, group)
    print(response)
except ApiException as e:
    print("Exception when calling UserGroupApi->buyers_buyer_id_usergroups_user_group_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
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

# **buyers_buyer_id_usergroups_user_group_id_put**
> UserGroup buyers_buyer_id_usergroups_user_group_id_put(buyer_id, user_group_id, group)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
UserGroupApi = OrderCloud.UserGroupApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
user_group_id = 'user_group_id_example' # str | ID of the user group.
group = OrderCloud.UserGroup() # UserGroup | 

try: 
    response = UserGroupApi.buyers_buyer_id_usergroups_user_group_id_put(buyer_id, user_group_id, group)
    print(response)
except ApiException as e:
    print("Exception when calling UserGroupApi->buyers_buyer_id_usergroups_user_group_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
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

