# OrderCloud.PriceScheduleApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**priceschedules_get**](PriceScheduleApi.md#priceschedules_get) | **GET** /priceschedules | 
[**priceschedules_post**](PriceScheduleApi.md#priceschedules_post) | **POST** /priceschedules | 
[**priceschedules_price_schedule_id_delete**](PriceScheduleApi.md#priceschedules_price_schedule_id_delete) | **DELETE** /priceschedules/{priceScheduleID} | 
[**priceschedules_price_schedule_id_get**](PriceScheduleApi.md#priceschedules_price_schedule_id_get) | **GET** /priceschedules/{priceScheduleID} | 
[**priceschedules_price_schedule_id_patch**](PriceScheduleApi.md#priceschedules_price_schedule_id_patch) | **PATCH** /priceschedules/{priceScheduleID} | 
[**priceschedules_price_schedule_id_price_breaks_delete**](PriceScheduleApi.md#priceschedules_price_schedule_id_price_breaks_delete) | **DELETE** /priceschedules/{priceScheduleID}/PriceBreaks | 
[**priceschedules_price_schedule_id_price_breaks_post**](PriceScheduleApi.md#priceschedules_price_schedule_id_price_breaks_post) | **POST** /priceschedules/{priceScheduleID}/PriceBreaks | 
[**priceschedules_price_schedule_id_put**](PriceScheduleApi.md#priceschedules_price_schedule_id_put) | **PUT** /priceschedules/{priceScheduleID} | 


# **priceschedules_get**
> ListPriceSchedule priceschedules_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
PriceScheduleApi = OrderCloud.PriceScheduleApi
search = 'search_example' # str | Search of the price schedule. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the price schedule. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the price schedule. (optional)
page = 56 # int | Page of the price schedule. (optional)
page_size = 56 # int | Page size of the price schedule. (optional)

try: 
    response = PriceScheduleApi.priceschedules_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling PriceScheduleApi->priceschedules_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search of the price schedule. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the price schedule. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the price schedule. | [optional] 
 **page** | **int**| Page of the price schedule. | [optional] 
 **page_size** | **int**| Page size of the price schedule. | [optional] 

### Return type

[**ListPriceSchedule**](ListPriceSchedule.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **priceschedules_post**
> PriceSchedule priceschedules_post(price_schedule)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
PriceScheduleApi = OrderCloud.PriceScheduleApi
price_schedule = OrderCloud.PriceSchedule() # PriceSchedule | 

try: 
    response = PriceScheduleApi.priceschedules_post(price_schedule)
    print(response)
except ApiException as e:
    print("Exception when calling PriceScheduleApi->priceschedules_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_schedule** | [**PriceSchedule**](PriceSchedule.md)|  | 

### Return type

[**PriceSchedule**](PriceSchedule.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **priceschedules_price_schedule_id_delete**
> priceschedules_price_schedule_id_delete(price_schedule_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
PriceScheduleApi = OrderCloud.PriceScheduleApi
price_schedule_id = 'price_schedule_id_example' # str | ID of the price schedule.

try: 
    PriceScheduleApi.priceschedules_price_schedule_id_delete(price_schedule_id)
except ApiException as e:
    print("Exception when calling PriceScheduleApi->priceschedules_price_schedule_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_schedule_id** | **str**| ID of the price schedule. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **priceschedules_price_schedule_id_get**
> PriceSchedule priceschedules_price_schedule_id_get(price_schedule_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
PriceScheduleApi = OrderCloud.PriceScheduleApi
price_schedule_id = 'price_schedule_id_example' # str | ID of the price schedule.

try: 
    response = PriceScheduleApi.priceschedules_price_schedule_id_get(price_schedule_id)
    print(response)
except ApiException as e:
    print("Exception when calling PriceScheduleApi->priceschedules_price_schedule_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_schedule_id** | **str**| ID of the price schedule. | 

### Return type

[**PriceSchedule**](PriceSchedule.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **priceschedules_price_schedule_id_patch**
> PriceSchedule priceschedules_price_schedule_id_patch(price_schedule_id, price_schedule)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
PriceScheduleApi = OrderCloud.PriceScheduleApi
price_schedule_id = 'price_schedule_id_example' # str | ID of the price schedule.
price_schedule = OrderCloud.PriceSchedule() # PriceSchedule | 

try: 
    response = PriceScheduleApi.priceschedules_price_schedule_id_patch(price_schedule_id, price_schedule)
    print(response)
except ApiException as e:
    print("Exception when calling PriceScheduleApi->priceschedules_price_schedule_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_schedule_id** | **str**| ID of the price schedule. | 
 **price_schedule** | [**PriceSchedule**](PriceSchedule.md)|  | 

### Return type

[**PriceSchedule**](PriceSchedule.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **priceschedules_price_schedule_id_price_breaks_delete**
> priceschedules_price_schedule_id_price_breaks_delete(price_schedule_id, quantity)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
PriceScheduleApi = OrderCloud.PriceScheduleApi
price_schedule_id = 'price_schedule_id_example' # str | ID of the price schedule.
quantity = 56 # int | Quantity of the price schedule.

try: 
    PriceScheduleApi.priceschedules_price_schedule_id_price_breaks_delete(price_schedule_id, quantity)
except ApiException as e:
    print("Exception when calling PriceScheduleApi->priceschedules_price_schedule_id_price_breaks_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_schedule_id** | **str**| ID of the price schedule. | 
 **quantity** | **int**| Quantity of the price schedule. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **priceschedules_price_schedule_id_price_breaks_post**
> PriceSchedule priceschedules_price_schedule_id_price_breaks_post(price_schedule_id, price_break)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
PriceScheduleApi = OrderCloud.PriceScheduleApi
price_schedule_id = 'price_schedule_id_example' # str | ID of the price schedule.
price_break = OrderCloud.PriceBreak() # PriceBreak | 

try: 
    response = PriceScheduleApi.priceschedules_price_schedule_id_price_breaks_post(price_schedule_id, price_break)
    print(response)
except ApiException as e:
    print("Exception when calling PriceScheduleApi->priceschedules_price_schedule_id_price_breaks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_schedule_id** | **str**| ID of the price schedule. | 
 **price_break** | [**PriceBreak**](PriceBreak.md)|  | 

### Return type

[**PriceSchedule**](PriceSchedule.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **priceschedules_price_schedule_id_put**
> PriceSchedule priceschedules_price_schedule_id_put(price_schedule_id, price_schedule)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
PriceScheduleApi = OrderCloud.PriceScheduleApi
price_schedule_id = 'price_schedule_id_example' # str | ID of the price schedule.
price_schedule = OrderCloud.PriceSchedule() # PriceSchedule | 

try: 
    response = PriceScheduleApi.priceschedules_price_schedule_id_put(price_schedule_id, price_schedule)
    print(response)
except ApiException as e:
    print("Exception when calling PriceScheduleApi->priceschedules_price_schedule_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_schedule_id** | **str**| ID of the price schedule. | 
 **price_schedule** | [**PriceSchedule**](PriceSchedule.md)|  | 

### Return type

[**PriceSchedule**](PriceSchedule.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

