# OrderCloud.LineItemApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orders_direction_order_id_lineitems_get**](LineItemApi.md#orders_direction_order_id_lineitems_get) | **GET** /orders/{direction}/{orderID}/lineitems | 
[**orders_direction_order_id_lineitems_line_item_id_delete**](LineItemApi.md#orders_direction_order_id_lineitems_line_item_id_delete) | **DELETE** /orders/{direction}/{orderID}/lineitems/{lineItemID} | 
[**orders_direction_order_id_lineitems_line_item_id_get**](LineItemApi.md#orders_direction_order_id_lineitems_line_item_id_get) | **GET** /orders/{direction}/{orderID}/lineitems/{lineItemID} | 
[**orders_direction_order_id_lineitems_line_item_id_patch**](LineItemApi.md#orders_direction_order_id_lineitems_line_item_id_patch) | **PATCH** /orders/{direction}/{orderID}/lineitems/{lineItemID} | 
[**orders_direction_order_id_lineitems_line_item_id_put**](LineItemApi.md#orders_direction_order_id_lineitems_line_item_id_put) | **PUT** /orders/{direction}/{orderID}/lineitems/{lineItemID} | 
[**orders_direction_order_id_lineitems_line_item_id_shipto_patch**](LineItemApi.md#orders_direction_order_id_lineitems_line_item_id_shipto_patch) | **PATCH** /orders/{direction}/{orderID}/lineitems/{lineItemID}/shipto | 
[**orders_direction_order_id_lineitems_line_item_id_shipto_put**](LineItemApi.md#orders_direction_order_id_lineitems_line_item_id_shipto_put) | **PUT** /orders/{direction}/{orderID}/lineitems/{lineItemID}/shipto | 
[**orders_direction_order_id_lineitems_post**](LineItemApi.md#orders_direction_order_id_lineitems_post) | **POST** /orders/{direction}/{orderID}/lineitems | 


# **orders_direction_order_id_lineitems_get**
> ListLineItem orders_direction_order_id_lineitems_get(direction, order_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
LineItemApi = OrderCloud.LineItemApi
direction = 'direction_example' # str | Direction of the line item. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
search = 'search_example' # str | Search of the line item. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the line item. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the line item. (optional)
page = 56 # int | Page of the line item. (optional)
page_size = 56 # int | Page size of the line item. (optional)

try: 
    response = LineItemApi.orders_direction_order_id_lineitems_get(direction, order_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling LineItemApi->orders_direction_order_id_lineitems_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the line item. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **search** | **str**| Search of the line item. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the line item. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the line item. | [optional] 
 **page** | **int**| Page of the line item. | [optional] 
 **page_size** | **int**| Page size of the line item. | [optional] 

### Return type

[**ListLineItem**](ListLineItem.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_direction_order_id_lineitems_line_item_id_delete**
> orders_direction_order_id_lineitems_line_item_id_delete(direction, order_id, line_item_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
LineItemApi = OrderCloud.LineItemApi
direction = 'direction_example' # str | Direction of the line item. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
line_item_id = 'line_item_id_example' # str | ID of the line item.

try: 
    LineItemApi.orders_direction_order_id_lineitems_line_item_id_delete(direction, order_id, line_item_id)
except ApiException as e:
    print("Exception when calling LineItemApi->orders_direction_order_id_lineitems_line_item_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the line item. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **line_item_id** | **str**| ID of the line item. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_direction_order_id_lineitems_line_item_id_get**
> LineItem orders_direction_order_id_lineitems_line_item_id_get(direction, order_id, line_item_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
LineItemApi = OrderCloud.LineItemApi
direction = 'direction_example' # str | Direction of the line item. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
line_item_id = 'line_item_id_example' # str | ID of the line item.

try: 
    response = LineItemApi.orders_direction_order_id_lineitems_line_item_id_get(direction, order_id, line_item_id)
    print(response)
except ApiException as e:
    print("Exception when calling LineItemApi->orders_direction_order_id_lineitems_line_item_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the line item. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **line_item_id** | **str**| ID of the line item. | 

### Return type

[**LineItem**](LineItem.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_direction_order_id_lineitems_line_item_id_patch**
> LineItem orders_direction_order_id_lineitems_line_item_id_patch(direction, order_id, line_item_id, partial_line_item)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
LineItemApi = OrderCloud.LineItemApi
direction = 'direction_example' # str | Direction of the line item. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
line_item_id = 'line_item_id_example' # str | ID of the line item.
partial_line_item = OrderCloud.LineItem() # LineItem | 

try: 
    response = LineItemApi.orders_direction_order_id_lineitems_line_item_id_patch(direction, order_id, line_item_id, partial_line_item)
    print(response)
except ApiException as e:
    print("Exception when calling LineItemApi->orders_direction_order_id_lineitems_line_item_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the line item. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **line_item_id** | **str**| ID of the line item. | 
 **partial_line_item** | [**LineItem**](LineItem.md)|  | 

### Return type

[**LineItem**](LineItem.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_direction_order_id_lineitems_line_item_id_put**
> LineItem orders_direction_order_id_lineitems_line_item_id_put(direction, order_id, line_item_id, line_item)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
LineItemApi = OrderCloud.LineItemApi
direction = 'direction_example' # str | Direction of the line item. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
line_item_id = 'line_item_id_example' # str | ID of the line item.
line_item = OrderCloud.LineItem() # LineItem | 

try: 
    response = LineItemApi.orders_direction_order_id_lineitems_line_item_id_put(direction, order_id, line_item_id, line_item)
    print(response)
except ApiException as e:
    print("Exception when calling LineItemApi->orders_direction_order_id_lineitems_line_item_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the line item. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **line_item_id** | **str**| ID of the line item. | 
 **line_item** | [**LineItem**](LineItem.md)|  | 

### Return type

[**LineItem**](LineItem.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_direction_order_id_lineitems_line_item_id_shipto_patch**
> LineItem orders_direction_order_id_lineitems_line_item_id_shipto_patch(direction, order_id, line_item_id, partial_address)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
LineItemApi = OrderCloud.LineItemApi
direction = 'direction_example' # str | Direction of the line item. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
line_item_id = 'line_item_id_example' # str | ID of the line item.
partial_address = OrderCloud.Address() # Address | 

try: 
    response = LineItemApi.orders_direction_order_id_lineitems_line_item_id_shipto_patch(direction, order_id, line_item_id, partial_address)
    print(response)
except ApiException as e:
    print("Exception when calling LineItemApi->orders_direction_order_id_lineitems_line_item_id_shipto_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the line item. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **line_item_id** | **str**| ID of the line item. | 
 **partial_address** | [**Address**](Address.md)|  | 

### Return type

[**LineItem**](LineItem.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_direction_order_id_lineitems_line_item_id_shipto_put**
> LineItem orders_direction_order_id_lineitems_line_item_id_shipto_put(direction, order_id, line_item_id, address)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
LineItemApi = OrderCloud.LineItemApi
direction = 'direction_example' # str | Direction of the line item. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
line_item_id = 'line_item_id_example' # str | ID of the line item.
address = OrderCloud.Address() # Address | 

try: 
    response = LineItemApi.orders_direction_order_id_lineitems_line_item_id_shipto_put(direction, order_id, line_item_id, address)
    print(response)
except ApiException as e:
    print("Exception when calling LineItemApi->orders_direction_order_id_lineitems_line_item_id_shipto_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the line item. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **line_item_id** | **str**| ID of the line item. | 
 **address** | [**Address**](Address.md)|  | 

### Return type

[**LineItem**](LineItem.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_direction_order_id_lineitems_post**
> LineItem orders_direction_order_id_lineitems_post(direction, order_id, line_item)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
LineItemApi = OrderCloud.LineItemApi
direction = 'direction_example' # str | Direction of the line item. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
line_item = OrderCloud.LineItem() # LineItem | 

try: 
    response = LineItemApi.orders_direction_order_id_lineitems_post(direction, order_id, line_item)
    print(response)
except ApiException as e:
    print("Exception when calling LineItemApi->orders_direction_order_id_lineitems_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the line item. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **line_item** | [**LineItem**](LineItem.md)|  | 

### Return type

[**LineItem**](LineItem.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

