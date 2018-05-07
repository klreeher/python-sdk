# OrderCloud.SupplierUserGroupApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](SupplierUserGroupApi.md#create) | **POST** /suppliers/{supplierID}/usergroups | 
[**delete**](SupplierUserGroupApi.md#delete) | **DELETE** /suppliers/{supplierID}/usergroups/{userGroupID} | 
[**delete_user_assignment**](SupplierUserGroupApi.md#delete_user_assignment) | **DELETE** /suppliers/{supplierID}/usergroups/{userGroupID}/assignments/{userID} | 
[**get**](SupplierUserGroupApi.md#get) | **GET** /suppliers/{supplierID}/usergroups/{userGroupID} | 
[**list**](SupplierUserGroupApi.md#list) | **GET** /suppliers/{supplierID}/usergroups | 
[**list_user_assignments**](SupplierUserGroupApi.md#list_user_assignments) | **GET** /suppliers/{supplierID}/usergroups/assignments | 
[**patch**](SupplierUserGroupApi.md#patch) | **PATCH** /suppliers/{supplierID}/usergroups/{userGroupID} | 
[**save**](SupplierUserGroupApi.md#save) | **PUT** /suppliers/{supplierID}/usergroups/{userGroupID} | 
[**save_user_assignment**](SupplierUserGroupApi.md#save_user_assignment) | **POST** /suppliers/{supplierID}/usergroups/assignments | 


# **create**
> UserGroup create(supplier_id, user_group)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SupplierUserGroupApi = OrderCloud.SupplierUserGroupApi
supplier_id = 'supplier_id_example' # str | ID of the supplier.
user_group = OrderCloud.UserGroup() # UserGroup | 

try: 
    response = SupplierUserGroupApi.create(supplier_id, user_group)
    print(response)
except ApiException as e:
    print("Exception when calling SupplierUserGroupApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | **str**| ID of the supplier. | 
 **user_group** | [**UserGroup**](UserGroup.md)|  | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(supplier_id, user_group_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SupplierUserGroupApi = OrderCloud.SupplierUserGroupApi
supplier_id = 'supplier_id_example' # str | ID of the supplier.
user_group_id = 'user_group_id_example' # str | ID of the user group.

try: 
    SupplierUserGroupApi.delete(supplier_id, user_group_id)
except ApiException as e:
    print("Exception when calling SupplierUserGroupApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | **str**| ID of the supplier. | 
 **user_group_id** | **str**| ID of the user group. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_assignment**
> delete_user_assignment(supplier_id, user_group_id, user_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SupplierUserGroupApi = OrderCloud.SupplierUserGroupApi
supplier_id = 'supplier_id_example' # str | ID of the supplier.
user_group_id = 'user_group_id_example' # str | ID of the user group.
user_id = 'user_id_example' # str | ID of the user.

try: 
    SupplierUserGroupApi.delete_user_assignment(supplier_id, user_group_id, user_id)
except ApiException as e:
    print("Exception when calling SupplierUserGroupApi->delete_user_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | **str**| ID of the supplier. | 
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

# **get**
> UserGroup get(supplier_id, user_group_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SupplierUserGroupApi = OrderCloud.SupplierUserGroupApi
supplier_id = 'supplier_id_example' # str | ID of the supplier.
user_group_id = 'user_group_id_example' # str | ID of the user group.

try: 
    response = SupplierUserGroupApi.get(supplier_id, user_group_id)
    print(response)
except ApiException as e:
    print("Exception when calling SupplierUserGroupApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | **str**| ID of the supplier. | 
 **user_group_id** | **str**| ID of the user group. | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ListUserGroup list(supplier_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SupplierUserGroupApi = OrderCloud.SupplierUserGroupApi
supplier_id = 'supplier_id_example' # str | ID of the supplier.
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = SupplierUserGroupApi.list(supplier_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling SupplierUserGroupApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | **str**| ID of the supplier. | 
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

# **list_user_assignments**
> ListUserGroupAssignment list_user_assignments(supplier_id, user_group_id=user_group_id, user_id=user_id, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SupplierUserGroupApi = OrderCloud.SupplierUserGroupApi
supplier_id = 'supplier_id_example' # str | ID of the supplier.
user_group_id = 'user_group_id_example' # str | ID of the user group. (optional)
user_id = 'user_id_example' # str | ID of the user. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)

try: 
    response = SupplierUserGroupApi.list_user_assignments(supplier_id, user_group_id=user_group_id, user_id=user_id, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling SupplierUserGroupApi->list_user_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | **str**| ID of the supplier. | 
 **user_group_id** | **str**| ID of the user group. | [optional] 
 **user_id** | **str**| ID of the user. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 

### Return type

[**ListUserGroupAssignment**](ListUserGroupAssignment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch**
> UserGroup patch(supplier_id, user_group_id, partial_user_group)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SupplierUserGroupApi = OrderCloud.SupplierUserGroupApi
supplier_id = 'supplier_id_example' # str | ID of the supplier.
user_group_id = 'user_group_id_example' # str | ID of the user group.
partial_user_group = OrderCloud.UserGroup() # UserGroup | 

try: 
    response = SupplierUserGroupApi.patch(supplier_id, user_group_id, partial_user_group)
    print(response)
except ApiException as e:
    print("Exception when calling SupplierUserGroupApi->patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | **str**| ID of the supplier. | 
 **user_group_id** | **str**| ID of the user group. | 
 **partial_user_group** | [**UserGroup**](UserGroup.md)|  | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save**
> UserGroup save(supplier_id, user_group_id, user_group)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SupplierUserGroupApi = OrderCloud.SupplierUserGroupApi
supplier_id = 'supplier_id_example' # str | ID of the supplier.
user_group_id = 'user_group_id_example' # str | ID of the user group.
user_group = OrderCloud.UserGroup() # UserGroup | 

try: 
    response = SupplierUserGroupApi.save(supplier_id, user_group_id, user_group)
    print(response)
except ApiException as e:
    print("Exception when calling SupplierUserGroupApi->save: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | **str**| ID of the supplier. | 
 **user_group_id** | **str**| ID of the user group. | 
 **user_group** | [**UserGroup**](UserGroup.md)|  | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_user_assignment**
> save_user_assignment(supplier_id, user_group_assignment)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SupplierUserGroupApi = OrderCloud.SupplierUserGroupApi
supplier_id = 'supplier_id_example' # str | ID of the supplier.
user_group_assignment = OrderCloud.UserGroupAssignment() # UserGroupAssignment | 

try: 
    SupplierUserGroupApi.save_user_assignment(supplier_id, user_group_assignment)
except ApiException as e:
    print("Exception when calling SupplierUserGroupApi->save_user_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | **str**| ID of the supplier. | 
 **user_group_assignment** | [**UserGroupAssignment**](UserGroupAssignment.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

