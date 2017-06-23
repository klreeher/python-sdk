# OrderCloud.SecurityProfileApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**securityprofiles_assignments_get**](SecurityProfileApi.md#securityprofiles_assignments_get) | **GET** /securityprofiles/assignments | 
[**securityprofiles_assignments_post**](SecurityProfileApi.md#securityprofiles_assignments_post) | **POST** /securityprofiles/assignments | 
[**securityprofiles_get**](SecurityProfileApi.md#securityprofiles_get) | **GET** /securityprofiles | 
[**securityprofiles_security_profile_id_assignments_delete**](SecurityProfileApi.md#securityprofiles_security_profile_id_assignments_delete) | **DELETE** /securityprofiles/{securityProfileID}/assignments | 
[**securityprofiles_security_profile_id_get**](SecurityProfileApi.md#securityprofiles_security_profile_id_get) | **GET** /securityprofiles/{securityProfileID} | 


# **securityprofiles_assignments_get**
> ListSecurityProfileAssignment securityprofiles_assignments_get(buyer_id=buyer_id, supplier_id=supplier_id, security_profile_id=security_profile_id, user_id=user_id, user_group_id=user_group_id, commerce_role=commerce_role, level=level, page=page, page_size=page_size)



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
commerce_role = 'commerce_role_example' # str | Commerce role of the security profile. (optional)
level = 'level_example' # str | Level of the security profile. (optional)
page = 56 # int | Page of the security profile. (optional)
page_size = 56 # int | Page size of the security profile. (optional)

try: 
    response = SecurityProfileApi.securityprofiles_assignments_get(buyer_id=buyer_id, supplier_id=supplier_id, security_profile_id=security_profile_id, user_id=user_id, user_group_id=user_group_id, commerce_role=commerce_role, level=level, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling SecurityProfileApi->securityprofiles_assignments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | [optional] 
 **supplier_id** | **str**| ID of the supplier. | [optional] 
 **security_profile_id** | **str**| ID of the security profile. | [optional] 
 **user_id** | **str**| ID of the user. | [optional] 
 **user_group_id** | **str**| ID of the user group. | [optional] 
 **commerce_role** | **str**| Commerce role of the security profile. | [optional] 
 **level** | **str**| Level of the security profile. | [optional] 
 **page** | **int**| Page of the security profile. | [optional] 
 **page_size** | **int**| Page size of the security profile. | [optional] 

### Return type

[**ListSecurityProfileAssignment**](ListSecurityProfileAssignment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **securityprofiles_assignments_post**
> securityprofiles_assignments_post(assignment)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SecurityProfileApi = OrderCloud.SecurityProfileApi
assignment = OrderCloud.SecurityProfileAssignment() # SecurityProfileAssignment | 

try: 
    SecurityProfileApi.securityprofiles_assignments_post(assignment)
except ApiException as e:
    print("Exception when calling SecurityProfileApi->securityprofiles_assignments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment** | [**SecurityProfileAssignment**](SecurityProfileAssignment.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **securityprofiles_get**
> ListSecurityProfile securityprofiles_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SecurityProfileApi = OrderCloud.SecurityProfileApi
search = 'search_example' # str | Search of the security profile. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the security profile. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the security profile. (optional)
page = 56 # int | Page of the security profile. (optional)
page_size = 56 # int | Page size of the security profile. (optional)

try: 
    response = SecurityProfileApi.securityprofiles_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling SecurityProfileApi->securityprofiles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search of the security profile. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the security profile. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the security profile. | [optional] 
 **page** | **int**| Page of the security profile. | [optional] 
 **page_size** | **int**| Page size of the security profile. | [optional] 

### Return type

[**ListSecurityProfile**](ListSecurityProfile.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **securityprofiles_security_profile_id_assignments_delete**
> securityprofiles_security_profile_id_assignments_delete(security_profile_id, buyer_id=buyer_id, user_id=user_id, user_group_id=user_group_id)



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
    SecurityProfileApi.securityprofiles_security_profile_id_assignments_delete(security_profile_id, buyer_id=buyer_id, user_id=user_id, user_group_id=user_group_id)
except ApiException as e:
    print("Exception when calling SecurityProfileApi->securityprofiles_security_profile_id_assignments_delete: %s\n" % e)
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

# **securityprofiles_security_profile_id_get**
> SecurityProfile securityprofiles_security_profile_id_get(security_profile_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SecurityProfileApi = OrderCloud.SecurityProfileApi
security_profile_id = 'security_profile_id_example' # str | ID of the security profile.

try: 
    response = SecurityProfileApi.securityprofiles_security_profile_id_get(security_profile_id)
    print(response)
except ApiException as e:
    print("Exception when calling SecurityProfileApi->securityprofiles_security_profile_id_get: %s\n" % e)
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

