# OrderCloud.ImpersonationConfigApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ImpersonationConfigApi.md#create) | **POST** /impersonationconfig | 
[**delete**](ImpersonationConfigApi.md#delete) | **DELETE** /impersonationconfig/{impersonationConfigID} | 
[**get**](ImpersonationConfigApi.md#get) | **GET** /impersonationconfig/{impersonationConfigID} | 
[**list**](ImpersonationConfigApi.md#list) | **GET** /impersonationconfig | 
[**patch**](ImpersonationConfigApi.md#patch) | **PATCH** /impersonationconfig/{impersonationConfigID} | 
[**save**](ImpersonationConfigApi.md#save) | **PUT** /impersonationconfig/{impersonationConfigID} | 


# **create**
> ImpersonationConfig create(impersonation_config)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ImpersonationConfigApi = OrderCloud.ImpersonationConfigApi
impersonation_config = OrderCloud.ImpersonationConfig() # ImpersonationConfig | 

try: 
    response = ImpersonationConfigApi.create(impersonation_config)
    print(response)
except ApiException as e:
    print("Exception when calling ImpersonationConfigApi->create: %s\n" % e)
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

# **delete**
> delete(impersonation_config_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ImpersonationConfigApi = OrderCloud.ImpersonationConfigApi
impersonation_config_id = 'impersonation_config_id_example' # str | ID of the impersonation config.

try: 
    ImpersonationConfigApi.delete(impersonation_config_id)
except ApiException as e:
    print("Exception when calling ImpersonationConfigApi->delete: %s\n" % e)
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

# **get**
> ImpersonationConfig get(impersonation_config_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ImpersonationConfigApi = OrderCloud.ImpersonationConfigApi
impersonation_config_id = 'impersonation_config_id_example' # str | ID of the impersonation config.

try: 
    response = ImpersonationConfigApi.get(impersonation_config_id)
    print(response)
except ApiException as e:
    print("Exception when calling ImpersonationConfigApi->get: %s\n" % e)
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

# **list**
> ListImpersonationConfig list(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ImpersonationConfigApi = OrderCloud.ImpersonationConfigApi
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = ImpersonationConfigApi.list(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling ImpersonationConfigApi->list: %s\n" % e)
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

[**ListImpersonationConfig**](ListImpersonationConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch**
> ImpersonationConfig patch(impersonation_config_id, partial_impersonation_config)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ImpersonationConfigApi = OrderCloud.ImpersonationConfigApi
impersonation_config_id = 'impersonation_config_id_example' # str | ID of the impersonation config.
partial_impersonation_config = OrderCloud.ImpersonationConfig() # ImpersonationConfig | 

try: 
    response = ImpersonationConfigApi.patch(impersonation_config_id, partial_impersonation_config)
    print(response)
except ApiException as e:
    print("Exception when calling ImpersonationConfigApi->patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **impersonation_config_id** | **str**| ID of the impersonation config. | 
 **partial_impersonation_config** | [**ImpersonationConfig**](ImpersonationConfig.md)|  | 

### Return type

[**ImpersonationConfig**](ImpersonationConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save**
> ImpersonationConfig save(impersonation_config_id, impersonation_config)



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
    response = ImpersonationConfigApi.save(impersonation_config_id, impersonation_config)
    print(response)
except ApiException as e:
    print("Exception when calling ImpersonationConfigApi->save: %s\n" % e)
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

