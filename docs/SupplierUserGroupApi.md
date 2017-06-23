# OrderCloud.SupplierUserGroupApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**suppliers_supplier_id_usergroups_assignments_get**](SupplierUserGroupApi.md#suppliers_supplier_id_usergroups_assignments_get) | **GET** /suppliers/{supplierID}/usergroups/assignments | 
[**suppliers_supplier_id_usergroups_assignments_post**](SupplierUserGroupApi.md#suppliers_supplier_id_usergroups_assignments_post) | **POST** /suppliers/{supplierID}/usergroups/assignments | 
[**suppliers_supplier_id_usergroups_get**](SupplierUserGroupApi.md#suppliers_supplier_id_usergroups_get) | **GET** /suppliers/{supplierID}/usergroups | 
[**suppliers_supplier_id_usergroups_post**](SupplierUserGroupApi.md#suppliers_supplier_id_usergroups_post) | **POST** /suppliers/{supplierID}/usergroups | 
[**suppliers_supplier_id_usergroups_user_group_id_assignments_user_id_delete**](SupplierUserGroupApi.md#suppliers_supplier_id_usergroups_user_group_id_assignments_user_id_delete) | **DELETE** /suppliers/{supplierID}/usergroups/{userGroupID}/assignments/{userID} | 
[**suppliers_supplier_id_usergroups_user_group_id_delete**](SupplierUserGroupApi.md#suppliers_supplier_id_usergroups_user_group_id_delete) | **DELETE** /suppliers/{supplierID}/usergroups/{userGroupID} | 
[**suppliers_supplier_id_usergroups_user_group_id_get**](SupplierUserGroupApi.md#suppliers_supplier_id_usergroups_user_group_id_get) | **GET** /suppliers/{supplierID}/usergroups/{userGroupID} | 
[**suppliers_supplier_id_usergroups_user_group_id_patch**](SupplierUserGroupApi.md#suppliers_supplier_id_usergroups_user_group_id_patch) | **PATCH** /suppliers/{supplierID}/usergroups/{userGroupID} | 
[**suppliers_supplier_id_usergroups_user_group_id_put**](SupplierUserGroupApi.md#suppliers_supplier_id_usergroups_user_group_id_put) | **PUT** /suppliers/{supplierID}/usergroups/{userGroupID} | 


# **suppliers_supplier_id_usergroups_assignments_get**
> ListUserGroupAssignment suppliers_supplier_id_usergroups_assignments_get(supplier_id, user_group_id=user_group_id, user_id=user_id, page=page, page_size=page_size)



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
page = 56 # int | Page of the supplier user group. (optional)
page_size = 56 # int | Page size of the supplier user group. (optional)

try: 
    response = SupplierUserGroupApi.suppliers_supplier_id_usergroups_assignments_get(supplier_id, user_group_id=user_group_id, user_id=user_id, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling SupplierUserGroupApi->suppliers_supplier_id_usergroups_assignments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | **str**| ID of the supplier. | 
 **user_group_id** | **str**| ID of the user group. | [optional] 
 **user_id** | **str**| ID of the user. | [optional] 
 **page** | **int**| Page of the supplier user group. | [optional] 
 **page_size** | **int**| Page size of the supplier user group. | [optional] 

### Return type

[**ListUserGroupAssignment**](ListUserGroupAssignment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppliers_supplier_id_usergroups_assignments_post**
> suppliers_supplier_id_usergroups_assignments_post(supplier_id, user_group_assignment)



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
    SupplierUserGroupApi.suppliers_supplier_id_usergroups_assignments_post(supplier_id, user_group_assignment)
except ApiException as e:
    print("Exception when calling SupplierUserGroupApi->suppliers_supplier_id_usergroups_assignments_post: %s\n" % e)
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

# **suppliers_supplier_id_usergroups_get**
> ListUserGroup suppliers_supplier_id_usergroups_get(supplier_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SupplierUserGroupApi = OrderCloud.SupplierUserGroupApi
supplier_id = 'supplier_id_example' # str | ID of the supplier.
search = 'search_example' # str | Search of the supplier user group. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the supplier user group. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the supplier user group. (optional)
page = 56 # int | Page of the supplier user group. (optional)
page_size = 56 # int | Page size of the supplier user group. (optional)

try: 
    response = SupplierUserGroupApi.suppliers_supplier_id_usergroups_get(supplier_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling SupplierUserGroupApi->suppliers_supplier_id_usergroups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | **str**| ID of the supplier. | 
 **search** | **str**| Search of the supplier user group. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the supplier user group. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the supplier user group. | [optional] 
 **page** | **int**| Page of the supplier user group. | [optional] 
 **page_size** | **int**| Page size of the supplier user group. | [optional] 

### Return type

[**ListUserGroup**](ListUserGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppliers_supplier_id_usergroups_post**
> UserGroup suppliers_supplier_id_usergroups_post(supplier_id, group)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SupplierUserGroupApi = OrderCloud.SupplierUserGroupApi
supplier_id = 'supplier_id_example' # str | ID of the supplier.
group = OrderCloud.UserGroup() # UserGroup | 

try: 
    response = SupplierUserGroupApi.suppliers_supplier_id_usergroups_post(supplier_id, group)
    print(response)
except ApiException as e:
    print("Exception when calling SupplierUserGroupApi->suppliers_supplier_id_usergroups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | **str**| ID of the supplier. | 
 **group** | [**UserGroup**](UserGroup.md)|  | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppliers_supplier_id_usergroups_user_group_id_assignments_user_id_delete**
> suppliers_supplier_id_usergroups_user_group_id_assignments_user_id_delete(supplier_id, user_group_id, user_id)



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
    SupplierUserGroupApi.suppliers_supplier_id_usergroups_user_group_id_assignments_user_id_delete(supplier_id, user_group_id, user_id)
except ApiException as e:
    print("Exception when calling SupplierUserGroupApi->suppliers_supplier_id_usergroups_user_group_id_assignments_user_id_delete: %s\n" % e)
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

# **suppliers_supplier_id_usergroups_user_group_id_delete**
> suppliers_supplier_id_usergroups_user_group_id_delete(supplier_id, user_group_id)



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
    SupplierUserGroupApi.suppliers_supplier_id_usergroups_user_group_id_delete(supplier_id, user_group_id)
except ApiException as e:
    print("Exception when calling SupplierUserGroupApi->suppliers_supplier_id_usergroups_user_group_id_delete: %s\n" % e)
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

# **suppliers_supplier_id_usergroups_user_group_id_get**
> UserGroup suppliers_supplier_id_usergroups_user_group_id_get(supplier_id, user_group_id)



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
    response = SupplierUserGroupApi.suppliers_supplier_id_usergroups_user_group_id_get(supplier_id, user_group_id)
    print(response)
except ApiException as e:
    print("Exception when calling SupplierUserGroupApi->suppliers_supplier_id_usergroups_user_group_id_get: %s\n" % e)
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

# **suppliers_supplier_id_usergroups_user_group_id_patch**
> UserGroup suppliers_supplier_id_usergroups_user_group_id_patch(supplier_id, user_group_id, group)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SupplierUserGroupApi = OrderCloud.SupplierUserGroupApi
supplier_id = 'supplier_id_example' # str | ID of the supplier.
user_group_id = 'user_group_id_example' # str | ID of the user group.
group = OrderCloud.UserGroup() # UserGroup | 

try: 
    response = SupplierUserGroupApi.suppliers_supplier_id_usergroups_user_group_id_patch(supplier_id, user_group_id, group)
    print(response)
except ApiException as e:
    print("Exception when calling SupplierUserGroupApi->suppliers_supplier_id_usergroups_user_group_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | **str**| ID of the supplier. | 
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

# **suppliers_supplier_id_usergroups_user_group_id_put**
> UserGroup suppliers_supplier_id_usergroups_user_group_id_put(supplier_id, user_group_id, group)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SupplierUserGroupApi = OrderCloud.SupplierUserGroupApi
supplier_id = 'supplier_id_example' # str | ID of the supplier.
user_group_id = 'user_group_id_example' # str | ID of the user group.
group = OrderCloud.UserGroup() # UserGroup | 

try: 
    response = SupplierUserGroupApi.suppliers_supplier_id_usergroups_user_group_id_put(supplier_id, user_group_id, group)
    print(response)
except ApiException as e:
    print("Exception when calling SupplierUserGroupApi->suppliers_supplier_id_usergroups_user_group_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | **str**| ID of the supplier. | 
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

