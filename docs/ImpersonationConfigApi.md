# OrderCloud.ImpersonationConfigApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**impersonationconfig_get**](ImpersonationConfigApi.md#impersonationconfig_get) | **GET** /impersonationconfig | 
[**impersonationconfig_impersonation_config_id_delete**](ImpersonationConfigApi.md#impersonationconfig_impersonation_config_id_delete) | **DELETE** /impersonationconfig/{impersonationConfigID} | 
[**impersonationconfig_impersonation_config_id_get**](ImpersonationConfigApi.md#impersonationconfig_impersonation_config_id_get) | **GET** /impersonationconfig/{impersonationConfigID} | 
[**impersonationconfig_impersonation_config_id_patch**](ImpersonationConfigApi.md#impersonationconfig_impersonation_config_id_patch) | **PATCH** /impersonationconfig/{impersonationConfigID} | 
[**impersonationconfig_impersonation_config_id_put**](ImpersonationConfigApi.md#impersonationconfig_impersonation_config_id_put) | **PUT** /impersonationconfig/{impersonationConfigID} | 
[**impersonationconfig_post**](ImpersonationConfigApi.md#impersonationconfig_post) | **POST** /impersonationconfig | 


# **impersonationconfig_get**
> ListImpersonationConfig impersonationconfig_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ImpersonationConfigApi = OrderCloud.ImpersonationConfigApi
search = 'search_example' # str | Search of the impersonation config. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the impersonation config. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the impersonation config. (optional)
page = 56 # int | Page of the impersonation config. (optional)
page_size = 56 # int | Page size of the impersonation config. (optional)

try: 
    response = ImpersonationConfigApi.impersonationconfig_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling ImpersonationConfigApi->impersonationconfig_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search of the impersonation config. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the impersonation config. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the impersonation config. | [optional] 
 **page** | **int**| Page of the impersonation config. | [optional] 
 **page_size** | **int**| Page size of the impersonation config. | [optional] 

### Return type

[**ListImpersonationConfig**](ListImpersonationConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **impersonationconfig_impersonation_config_id_delete**
> impersonationconfig_impersonation_config_id_delete(impersonation_config_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ImpersonationConfigApi = OrderCloud.ImpersonationConfigApi
impersonation_config_id = 'impersonation_config_id_example' # str | ID of the impersonation config.

try: 
    ImpersonationConfigApi.impersonationconfig_impersonation_config_id_delete(impersonation_config_id)
except ApiException as e:
    print("Exception when calling ImpersonationConfigApi->impersonationconfig_impersonation_config_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **impersonation_config_id** | **str**| ID of the impersonation config. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **impersonationconfig_impersonation_config_id_get**
> ImpersonationConfig impersonationconfig_impersonation_config_id_get(impersonation_config_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ImpersonationConfigApi = OrderCloud.ImpersonationConfigApi
impersonation_config_id = 'impersonation_config_id_example' # str | ID of the impersonation config.

try: 
    response = ImpersonationConfigApi.impersonationconfig_impersonation_config_id_get(impersonation_config_id)
    print(response)
except ApiException as e:
    print("Exception when calling ImpersonationConfigApi->impersonationconfig_impersonation_config_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **impersonation_config_id** | **str**| ID of the impersonation config. | 

### Return type

[**ImpersonationConfig**](ImpersonationConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **impersonationconfig_impersonation_config_id_patch**
> ImpersonationConfig impersonationconfig_impersonation_config_id_patch(impersonation_config_id, impersonation_config)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ImpersonationConfigApi = OrderCloud.ImpersonationConfigApi
impersonation_config_id = 'impersonation_config_id_example' # str | ID of the impersonation config.
impersonation_config = OrderCloud.ImpersonationConfig() # ImpersonationConfig | 

try: 
    response = ImpersonationConfigApi.impersonationconfig_impersonation_config_id_patch(impersonation_config_id, impersonation_config)
    print(response)
except ApiException as e:
    print("Exception when calling ImpersonationConfigApi->impersonationconfig_impersonation_config_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **impersonation_config_id** | **str**| ID of the impersonation config. | 
 **impersonation_config** | [**ImpersonationConfig**](ImpersonationConfig.md)|  | 

### Return type

[**ImpersonationConfig**](ImpersonationConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **impersonationconfig_impersonation_config_id_put**
> ImpersonationConfig impersonationconfig_impersonation_config_id_put(impersonation_config_id, impersonation_config)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ImpersonationConfigApi = OrderCloud.ImpersonationConfigApi
impersonation_config_id = 'impersonation_config_id_example' # str | ID of the impersonation config.
impersonation_config = OrderCloud.ImpersonationConfig() # ImpersonationConfig | 

try: 
    response = ImpersonationConfigApi.impersonationconfig_impersonation_config_id_put(impersonation_config_id, impersonation_config)
    print(response)
except ApiException as e:
    print("Exception when calling ImpersonationConfigApi->impersonationconfig_impersonation_config_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **impersonation_config_id** | **str**| ID of the impersonation config. | 
 **impersonation_config** | [**ImpersonationConfig**](ImpersonationConfig.md)|  | 

### Return type

[**ImpersonationConfig**](ImpersonationConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **impersonationconfig_post**
> ImpersonationConfig impersonationconfig_post(impersonation_config)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ImpersonationConfigApi = OrderCloud.ImpersonationConfigApi
impersonation_config = OrderCloud.ImpersonationConfig() # ImpersonationConfig | 

try: 
    response = ImpersonationConfigApi.impersonationconfig_post(impersonation_config)
    print(response)
except ApiException as e:
    print("Exception when calling ImpersonationConfigApi->impersonationconfig_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **impersonation_config** | [**ImpersonationConfig**](ImpersonationConfig.md)|  | 

### Return type

[**ImpersonationConfig**](ImpersonationConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

