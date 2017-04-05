# OrderCloud.ShipmentApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ShipmentApi.md#create) | **POST** /shipments | 
[**delete**](ShipmentApi.md#delete) | **DELETE** /shipments/{shipmentID} | 
[**delete_item**](ShipmentApi.md#delete_item) | **DELETE** /shipments/{shipmentID}/items/{orderID}/{lineItemID} | 
[**get**](ShipmentApi.md#get) | **GET** /shipments/{shipmentID} | 
[**get_item**](ShipmentApi.md#get_item) | **GET** /shipments/{shipmentID}/items/{orderID}/{lineItemID} | 
[**list**](ShipmentApi.md#list) | **GET** /shipments | 
[**list_items**](ShipmentApi.md#list_items) | **GET** /shipments/{shipmentID}/items | 
[**patch**](ShipmentApi.md#patch) | **PATCH** /shipments/{shipmentID} | 
[**save_item**](ShipmentApi.md#save_item) | **POST** /shipments/{shipmentID}/items | 
[**update**](ShipmentApi.md#update) | **PUT** /shipments/{shipmentID} | 


# **create**
> Shipment create(shipment)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ShipmentApi = OrderCloud.ShipmentApi
shipment = OrderCloud.Shipment() # Shipment | 

try: 
    response = ShipmentApi.create(shipment)
    print(response)
except ApiException as e:
    print("Exception when calling ShipmentApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment** | [**Shipment**](Shipment.md)|  | 

### Return type

[**Shipment**](Shipment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(shipment_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ShipmentApi = OrderCloud.ShipmentApi
shipment_id = 'shipment_id_example' # str | ID of the shipment.

try: 
    ShipmentApi.delete(shipment_id)
except ApiException as e:
    print("Exception when calling ShipmentApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| ID of the shipment. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item**
> delete_item(shipment_id, order_id, line_item_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ShipmentApi = OrderCloud.ShipmentApi
shipment_id = 'shipment_id_example' # str | ID of the shipment.
order_id = 'order_id_example' # str | ID of the order.
line_item_id = 'line_item_id_example' # str | ID of the line item.

try: 
    ShipmentApi.delete_item(shipment_id, order_id, line_item_id)
except ApiException as e:
    print("Exception when calling ShipmentApi->delete_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| ID of the shipment. | 
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

# **get**
> Shipment get(shipment_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ShipmentApi = OrderCloud.ShipmentApi
shipment_id = 'shipment_id_example' # str | ID of the shipment.

try: 
    response = ShipmentApi.get(shipment_id)
    print(response)
except ApiException as e:
    print("Exception when calling ShipmentApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| ID of the shipment. | 

### Return type

[**Shipment**](Shipment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item**
> ShipmentItem get_item(shipment_id, order_id, line_item_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ShipmentApi = OrderCloud.ShipmentApi
shipment_id = 'shipment_id_example' # str | ID of the shipment.
order_id = 'order_id_example' # str | ID of the order.
line_item_id = 'line_item_id_example' # str | ID of the line item.

try: 
    response = ShipmentApi.get_item(shipment_id, order_id, line_item_id)
    print(response)
except ApiException as e:
    print("Exception when calling ShipmentApi->get_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| ID of the shipment. | 
 **order_id** | **str**| ID of the order. | 
 **line_item_id** | **str**| ID of the line item. | 

### Return type

[**ShipmentItem**](ShipmentItem.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ListShipment list(order_id=order_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ShipmentApi = OrderCloud.ShipmentApi
order_id = 'order_id_example' # str | ID of the order. (optional)
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = ShipmentApi.list(order_id=order_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling ShipmentApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| ID of the order. | [optional] 
 **search** | **str**| Word or phrase to search for. | [optional] 
 **search_on** | **str**| Comma-delimited list of fields to search on. | [optional] 
 **sort_by** | **str**| Comma-delimited list of fields to sort by. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 
 **filters** | [**dict(str, str)**](str.md)| Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or &#39;xp.???&#39; | [optional] 

### Return type

[**ListShipment**](ListShipment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_items**
> ListShipmentItem list_items(shipment_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ShipmentApi = OrderCloud.ShipmentApi
shipment_id = 'shipment_id_example' # str | ID of the shipment.
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = ShipmentApi.list_items(shipment_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling ShipmentApi->list_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| ID of the shipment. | 
 **search** | **str**| Word or phrase to search for. | [optional] 
 **search_on** | **str**| Comma-delimited list of fields to search on. | [optional] 
 **sort_by** | **str**| Comma-delimited list of fields to sort by. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 
 **filters** | [**dict(str, str)**](str.md)| Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or &#39;xp.???&#39; | [optional] 

### Return type

[**ListShipmentItem**](ListShipmentItem.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch**
> Shipment patch(shipment_id, shipment)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ShipmentApi = OrderCloud.ShipmentApi
shipment_id = 'shipment_id_example' # str | ID of the shipment.
shipment = OrderCloud.Shipment() # Shipment | 

try: 
    response = ShipmentApi.patch(shipment_id, shipment)
    print(response)
except ApiException as e:
    print("Exception when calling ShipmentApi->patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| ID of the shipment. | 
 **shipment** | [**Shipment**](Shipment.md)|  | 

### Return type

[**Shipment**](Shipment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_item**
> ShipmentItem save_item(shipment_id, item)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ShipmentApi = OrderCloud.ShipmentApi
shipment_id = 'shipment_id_example' # str | ID of the shipment.
item = OrderCloud.ShipmentItem() # ShipmentItem | 

try: 
    response = ShipmentApi.save_item(shipment_id, item)
    print(response)
except ApiException as e:
    print("Exception when calling ShipmentApi->save_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| ID of the shipment. | 
 **item** | [**ShipmentItem**](ShipmentItem.md)|  | 

### Return type

[**ShipmentItem**](ShipmentItem.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Shipment update(shipment_id, shipment)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ShipmentApi = OrderCloud.ShipmentApi
shipment_id = 'shipment_id_example' # str | ID of the shipment.
shipment = OrderCloud.Shipment() # Shipment | 

try: 
    response = ShipmentApi.update(shipment_id, shipment)
    print(response)
except ApiException as e:
    print("Exception when calling ShipmentApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| ID of the shipment. | 
 **shipment** | [**Shipment**](Shipment.md)|  | 

### Return type

[**Shipment**](Shipment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

