# OrderCloud.SecurityProfileApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_assignment**](SecurityProfileApi.md#delete_assignment) | **DELETE** /securityprofiles/{securityProfileID}/assignments | 
[**get**](SecurityProfileApi.md#get) | **GET** /securityprofiles/{securityProfileID} | 
[**list**](SecurityProfileApi.md#list) | **GET** /securityprofiles | 
[**list_assignments**](SecurityProfileApi.md#list_assignments) | **GET** /securityprofiles/assignments | 
[**save_assignment**](SecurityProfileApi.md#save_assignment) | **POST** /securityprofiles/assignments | 


# **delete_assignment**
> delete_assignment(security_profile_id, buyer_id=buyer_id, user_id=user_id, user_group_id=user_group_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SecurityProfileApi = OrderCloud.SecurityProfileApi
security_profile_id = 'security_profile_id_example' # str | ID of the security profile.
buyer_id = 'buyer_id_example' # str | ID of the buyer. (optional)
user_id = 'user_id_example' # str | ID of the user. (optional)
user_group_id = 'user_group_id_example' # str | ID of the user group. (optional)

try: 
    SecurityProfileApi.delete_assignment(security_profile_id, buyer_id=buyer_id, user_id=user_id, user_group_id=user_group_id)
except ApiException as e:
    print("Exception when calling SecurityProfileApi->delete_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **security_profile_id** | **str**| ID of the security profile. | 
 **buyer_id** | **str**| ID of the buyer. | [optional] 
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
> SecurityProfile get(security_profile_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SecurityProfileApi = OrderCloud.SecurityProfileApi
security_profile_id = 'security_profile_id_example' # str | ID of the security profile.

try: 
    response = SecurityProfileApi.get(security_profile_id)
    print(response)
except ApiException as e:
    print("Exception when calling SecurityProfileApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **security_profile_id** | **str**| ID of the security profile. | 

### Return type

[**SecurityProfile**](SecurityProfile.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ListSecurityProfile list(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SecurityProfileApi = OrderCloud.SecurityProfileApi
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = SecurityProfileApi.list(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling SecurityProfileApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Word or phrase to search for. | [optional] 
 **search_on** | **str**| Comma-delimited list of fields to search on. | [optional] 
 **sort_by** | **str**| Comma-delimited list of fields to sort by. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 
 **filters** | [**dict(str, str)**](str.md)| Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or &#39;xp.???&#39; | [optional] 

### Return type

[**ListSecurityProfile**](ListSecurityProfile.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assignments**
> ListSecurityProfileAssignment list_assignments(buyer_id=buyer_id, supplier_id=supplier_id, security_profile_id=security_profile_id, user_id=user_id, user_group_id=user_group_id, commerce_role=commerce_role, level=level, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SecurityProfileApi = OrderCloud.SecurityProfileApi
buyer_id = 'buyer_id_example' # str | ID of the buyer. (optional)
supplier_id = 'supplier_id_example' # str | ID of the supplier. (optional)
security_profile_id = 'security_profile_id_example' # str | ID of the security profile. (optional)
user_id = 'user_id_example' # str | ID of the user. (optional)
user_group_id = 'user_group_id_example' # str | ID of the user group. (optional)
commerce_role = 'commerce_role_example' # str | Commerce role of the security profile assignment. Possible values: Buyer, Seller, Supplier. (optional)
level = 'level_example' # str | Level of the security profile assignment. Possible values: User, Group, Company. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)

try: 
    response = SecurityProfileApi.list_assignments(buyer_id=buyer_id, supplier_id=supplier_id, security_profile_id=security_profile_id, user_id=user_id, user_group_id=user_group_id, commerce_role=commerce_role, level=level, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling SecurityProfileApi->list_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | [optional] 
 **supplier_id** | **str**| ID of the supplier. | [optional] 
 **security_profile_id** | **str**| ID of the security profile. | [optional] 
 **user_id** | **str**| ID of the user. | [optional] 
 **user_group_id** | **str**| ID of the user group. | [optional] 
 **commerce_role** | **str**| Commerce role of the security profile assignment. Possible values: Buyer, Seller, Supplier. | [optional] 
 **level** | **str**| Level of the security profile assignment. Possible values: User, Group, Company. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 

### Return type

[**ListSecurityProfileAssignment**](ListSecurityProfileAssignment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_assignment**
> save_assignment(security_profile_assignment)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SecurityProfileApi = OrderCloud.SecurityProfileApi
security_profile_assignment = OrderCloud.SecurityProfileAssignment() # SecurityProfileAssignment | 

try: 
    SecurityProfileApi.save_assignment(security_profile_assignment)
except ApiException as e:
    print("Exception when calling SecurityProfileApi->save_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **security_profile_assignment** | [**SecurityProfileAssignment**](SecurityProfileAssignment.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

