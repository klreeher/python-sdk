# OrderCloud.IncrementorApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](IncrementorApi.md#create) | **POST** /incrementors | 
[**delete**](IncrementorApi.md#delete) | **DELETE** /incrementors/{incrementorID} | 
[**get**](IncrementorApi.md#get) | **GET** /incrementors/{incrementorID} | 
[**list**](IncrementorApi.md#list) | **GET** /incrementors | 
[**patch**](IncrementorApi.md#patch) | **PATCH** /incrementors/{incrementorID} | 
[**save**](IncrementorApi.md#save) | **PUT** /incrementors/{incrementorID} | 


# **create**
> Incrementor create(incrementor)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
IncrementorApi = OrderCloud.IncrementorApi
incrementor = OrderCloud.Incrementor() # Incrementor | 

try: 
    response = IncrementorApi.create(incrementor)
    print(response)
except ApiException as e:
    print("Exception when calling IncrementorApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incrementor** | [**Incrementor**](Incrementor.md)|  | 

### Return type

[**Incrementor**](Incrementor.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(incrementor_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
IncrementorApi = OrderCloud.IncrementorApi
incrementor_id = 'incrementor_id_example' # str | ID of the incrementor.

try: 
    IncrementorApi.delete(incrementor_id)
except ApiException as e:
    print("Exception when calling IncrementorApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incrementor_id** | **str**| ID of the incrementor. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Incrementor get(incrementor_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
IncrementorApi = OrderCloud.IncrementorApi
incrementor_id = 'incrementor_id_example' # str | ID of the incrementor.

try: 
    response = IncrementorApi.get(incrementor_id)
    print(response)
except ApiException as e:
    print("Exception when calling IncrementorApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incrementor_id** | **str**| ID of the incrementor. | 

### Return type

[**Incrementor**](Incrementor.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ListIncrementor list(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
IncrementorApi = OrderCloud.IncrementorApi
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = IncrementorApi.list(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling IncrementorApi->list: %s\n" % e)
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

[**ListIncrementor**](ListIncrementor.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch**
> Incrementor patch(incrementor_id, partial_incrementor)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
IncrementorApi = OrderCloud.IncrementorApi
incrementor_id = 'incrementor_id_example' # str | ID of the incrementor.
partial_incrementor = OrderCloud.Incrementor() # Incrementor | 

try: 
    response = IncrementorApi.patch(incrementor_id, partial_incrementor)
    print(response)
except ApiException as e:
    print("Exception when calling IncrementorApi->patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incrementor_id** | **str**| ID of the incrementor. | 
 **partial_incrementor** | [**Incrementor**](Incrementor.md)|  | 

### Return type

[**Incrementor**](Incrementor.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save**
> Incrementor save(incrementor_id, incrementor)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
IncrementorApi = OrderCloud.IncrementorApi
incrementor_id = 'incrementor_id_example' # str | ID of the incrementor.
incrementor = OrderCloud.Incrementor() # Incrementor | 

try: 
    response = IncrementorApi.save(incrementor_id, incrementor)
    print(response)
except ApiException as e:
    print("Exception when calling IncrementorApi->save: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incrementor_id** | **str**| ID of the incrementor. | 
 **incrementor** | [**Incrementor**](Incrementor.md)|  | 

### Return type

[**Incrementor**](Incrementor.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

