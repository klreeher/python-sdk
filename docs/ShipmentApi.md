# OrderCloud.ShipmentApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shipments_get**](ShipmentApi.md#shipments_get) | **GET** /shipments | 
[**shipments_post**](ShipmentApi.md#shipments_post) | **POST** /shipments | 
[**shipments_shipment_id_delete**](ShipmentApi.md#shipments_shipment_id_delete) | **DELETE** /shipments/{shipmentID} | 
[**shipments_shipment_id_get**](ShipmentApi.md#shipments_shipment_id_get) | **GET** /shipments/{shipmentID} | 
[**shipments_shipment_id_items_get**](ShipmentApi.md#shipments_shipment_id_items_get) | **GET** /shipments/{shipmentID}/items | 
[**shipments_shipment_id_items_order_id_line_item_id_delete**](ShipmentApi.md#shipments_shipment_id_items_order_id_line_item_id_delete) | **DELETE** /shipments/{shipmentID}/items/{orderID}/{lineItemID} | 
[**shipments_shipment_id_items_order_id_line_item_id_get**](ShipmentApi.md#shipments_shipment_id_items_order_id_line_item_id_get) | **GET** /shipments/{shipmentID}/items/{orderID}/{lineItemID} | 
[**shipments_shipment_id_items_post**](ShipmentApi.md#shipments_shipment_id_items_post) | **POST** /shipments/{shipmentID}/items | 
[**shipments_shipment_id_patch**](ShipmentApi.md#shipments_shipment_id_patch) | **PATCH** /shipments/{shipmentID} | 
[**shipments_shipment_id_put**](ShipmentApi.md#shipments_shipment_id_put) | **PUT** /shipments/{shipmentID} | 


# **shipments_get**
> ListShipment shipments_get(order_id=order_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ShipmentApi = OrderCloud.ShipmentApi
order_id = 'order_id_example' # str | ID of the order. (optional)
search = 'search_example' # str | Search of the shipment. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the shipment. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the shipment. (optional)
page = 56 # int | Page of the shipment. (optional)
page_size = 56 # int | Page size of the shipment. (optional)

try: 
    response = ShipmentApi.shipments_get(order_id=order_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling ShipmentApi->shipments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| ID of the order. | [optional] 
 **search** | **str**| Search of the shipment. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the shipment. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the shipment. | [optional] 
 **page** | **int**| Page of the shipment. | [optional] 
 **page_size** | **int**| Page size of the shipment. | [optional] 

### Return type

[**ListShipment**](ListShipment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipments_post**
> Shipment shipments_post(shipment)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ShipmentApi = OrderCloud.ShipmentApi
shipment = OrderCloud.Shipment() # Shipment | 

try: 
    response = ShipmentApi.shipments_post(shipment)
    print(response)
except ApiException as e:
    print("Exception when calling ShipmentApi->shipments_post: %s\n" % e)
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

# **shipments_shipment_id_delete**
> shipments_shipment_id_delete(shipment_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ShipmentApi = OrderCloud.ShipmentApi
shipment_id = 'shipment_id_example' # str | ID of the shipment.

try: 
    ShipmentApi.shipments_shipment_id_delete(shipment_id)
except ApiException as e:
    print("Exception when calling ShipmentApi->shipments_shipment_id_delete: %s\n" % e)
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

# **shipments_shipment_id_get**
> Shipment shipments_shipment_id_get(shipment_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ShipmentApi = OrderCloud.ShipmentApi
shipment_id = 'shipment_id_example' # str | ID of the shipment.

try: 
    response = ShipmentApi.shipments_shipment_id_get(shipment_id)
    print(response)
except ApiException as e:
    print("Exception when calling ShipmentApi->shipments_shipment_id_get: %s\n" % e)
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

# **shipments_shipment_id_items_get**
> ListShipmentItem shipments_shipment_id_items_get(shipment_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ShipmentApi = OrderCloud.ShipmentApi
shipment_id = 'shipment_id_example' # str | ID of the shipment.
search = 'search_example' # str | Search of the shipment. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the shipment. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the shipment. (optional)
page = 56 # int | Page of the shipment. (optional)
page_size = 56 # int | Page size of the shipment. (optional)

try: 
    response = ShipmentApi.shipments_shipment_id_items_get(shipment_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling ShipmentApi->shipments_shipment_id_items_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| ID of the shipment. | 
 **search** | **str**| Search of the shipment. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the shipment. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the shipment. | [optional] 
 **page** | **int**| Page of the shipment. | [optional] 
 **page_size** | **int**| Page size of the shipment. | [optional] 

### Return type

[**ListShipmentItem**](ListShipmentItem.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipments_shipment_id_items_order_id_line_item_id_delete**
> shipments_shipment_id_items_order_id_line_item_id_delete(shipment_id, order_id, line_item_id)



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
    ShipmentApi.shipments_shipment_id_items_order_id_line_item_id_delete(shipment_id, order_id, line_item_id)
except ApiException as e:
    print("Exception when calling ShipmentApi->shipments_shipment_id_items_order_id_line_item_id_delete: %s\n" % e)
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

# **shipments_shipment_id_items_order_id_line_item_id_get**
> ShipmentItem shipments_shipment_id_items_order_id_line_item_id_get(shipment_id, order_id, line_item_id)



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
    response = ShipmentApi.shipments_shipment_id_items_order_id_line_item_id_get(shipment_id, order_id, line_item_id)
    print(response)
except ApiException as e:
    print("Exception when calling ShipmentApi->shipments_shipment_id_items_order_id_line_item_id_get: %s\n" % e)
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

# **shipments_shipment_id_items_post**
> ShipmentItem shipments_shipment_id_items_post(shipment_id, item)



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
    response = ShipmentApi.shipments_shipment_id_items_post(shipment_id, item)
    print(response)
except ApiException as e:
    print("Exception when calling ShipmentApi->shipments_shipment_id_items_post: %s\n" % e)
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

# **shipments_shipment_id_patch**
> Shipment shipments_shipment_id_patch(shipment_id, shipment)



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
    response = ShipmentApi.shipments_shipment_id_patch(shipment_id, shipment)
    print(response)
except ApiException as e:
    print("Exception when calling ShipmentApi->shipments_shipment_id_patch: %s\n" % e)
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

# **shipments_shipment_id_put**
> Shipment shipments_shipment_id_put(shipment_id, shipment)



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
    response = ShipmentApi.shipments_shipment_id_put(shipment_id, shipment)
    print(response)
except ApiException as e:
    print("Exception when calling ShipmentApi->shipments_shipment_id_put: %s\n" % e)
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

