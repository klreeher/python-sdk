# OrderCloud.LineItemApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](LineItemApi.md#create) | **POST** /buyers/{buyerID}/orders/{orderID}/lineitems | 
[**delete**](LineItemApi.md#delete) | **DELETE** /buyers/{buyerID}/orders/{orderID}/lineitems/{lineItemID} | 
[**get**](LineItemApi.md#get) | **GET** /buyers/{buyerID}/orders/{orderID}/lineitems/{lineItemID} | 
[**list**](LineItemApi.md#list) | **GET** /buyers/{buyerID}/orders/{orderID}/lineitems | 
[**patch**](LineItemApi.md#patch) | **PATCH** /buyers/{buyerID}/orders/{orderID}/lineitems/{lineItemID} | 
[**patch_shipping_address**](LineItemApi.md#patch_shipping_address) | **PATCH** /buyers/{buyerID}/orders/{orderID}/lineitems/{lineItemID}/shipto | 
[**set_shipping_address**](LineItemApi.md#set_shipping_address) | **PUT** /buyers/{buyerID}/orders/{orderID}/lineitems/{lineItemID}/shipto | 
[**update**](LineItemApi.md#update) | **PUT** /buyers/{buyerID}/orders/{orderID}/lineitems/{lineItemID} | 


# **create**
> LineItem create(buyer_id, order_id, line_item)



### Example 
```python
import OrderCloud as oc
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an acess_token (see the Getting Started guide)

# create an instance of the API class
LineItemApi = OrderCloud.LineItemApi()
buyer_id = 'buyer_id_example' # str | ID of the buyer.
order_id = 'order_id_example' # str | ID of the order.
line_item = OrderCloud.LineItem() # LineItem | 

try: 
    response = LineItemApi.create(buyer_id, order_id, line_item)
    print(response)
except ApiException as e:
    print("Exception when calling LineItemApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
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

# **delete**
> delete(buyer_id, order_id, line_item_id)



### Example 
```python
import OrderCloud as oc
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an acess_token (see the Getting Started guide)

# create an instance of the API class
LineItemApi = OrderCloud.LineItemApi()
buyer_id = 'buyer_id_example' # str | ID of the buyer.
order_id = 'order_id_example' # str | ID of the order.
line_item_id = 'line_item_id_example' # str | ID of the line item.

try: 
    LineItemApi.delete(buyer_id, order_id, line_item_id)
except ApiException as e:
    print("Exception when calling LineItemApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
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
> LineItem get(buyer_id, order_id, line_item_id)



### Example 
```python
import OrderCloud as oc
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an acess_token (see the Getting Started guide)

# create an instance of the API class
LineItemApi = OrderCloud.LineItemApi()
buyer_id = 'buyer_id_example' # str | ID of the buyer.
order_id = 'order_id_example' # str | ID of the order.
line_item_id = 'line_item_id_example' # str | ID of the line item.

try: 
    response = LineItemApi.get(buyer_id, order_id, line_item_id)
    print(response)
except ApiException as e:
    print("Exception when calling LineItemApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
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

# **list**
> list[LineItem] list(buyer_id, order_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



### Example 
```python
import OrderCloud as oc
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an acess_token (see the Getting Started guide)

# create an instance of the API class
LineItemApi = OrderCloud.LineItemApi()
buyer_id = 'buyer_id_example' # str | ID of the buyer.
order_id = 'order_id_example' # str | ID of the order.
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = LineItemApi.list(buyer_id, order_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling LineItemApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **order_id** | **str**| ID of the order. | 
 **search** | **str**| Word or phrase to search for. | [optional] 
 **search_on** | **str**| Comma-delimited list of fields to search on. | [optional] 
 **sort_by** | **str**| Comma-delimited list of fields to sort by. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 
 **filters** | [**dict(str, str)**](str.md)| Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or &#39;xp.???&#39; | [optional] 

### Return type

[**list[LineItem]**](LineItem.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch**
> LineItem patch(buyer_id, order_id, line_item_id, partial_line_item)



### Example 
```python
import OrderCloud as oc
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an acess_token (see the Getting Started guide)

# create an instance of the API class
LineItemApi = OrderCloud.LineItemApi()
buyer_id = 'buyer_id_example' # str | ID of the buyer.
order_id = 'order_id_example' # str | ID of the order.
line_item_id = 'line_item_id_example' # str | ID of the line item.
partial_line_item = OrderCloud.LineItem() # LineItem | 

try: 
    response = LineItemApi.patch(buyer_id, order_id, line_item_id, partial_line_item)
    print(response)
except ApiException as e:
    print("Exception when calling LineItemApi->patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
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

# **patch_shipping_address**
> LineItem patch_shipping_address(buyer_id, order_id, line_item_id, partial_address)



### Example 
```python
import OrderCloud as oc
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an acess_token (see the Getting Started guide)

# create an instance of the API class
LineItemApi = OrderCloud.LineItemApi()
buyer_id = 'buyer_id_example' # str | ID of the buyer.
order_id = 'order_id_example' # str | ID of the order.
line_item_id = 'line_item_id_example' # str | ID of the line item.
partial_address = OrderCloud.Address() # Address | 

try: 
    response = LineItemApi.patch_shipping_address(buyer_id, order_id, line_item_id, partial_address)
    print(response)
except ApiException as e:
    print("Exception when calling LineItemApi->patch_shipping_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
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

# **set_shipping_address**
> LineItem set_shipping_address(buyer_id, order_id, line_item_id, address)



### Example 
```python
import OrderCloud as oc
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an acess_token (see the Getting Started guide)

# create an instance of the API class
LineItemApi = OrderCloud.LineItemApi()
buyer_id = 'buyer_id_example' # str | ID of the buyer.
order_id = 'order_id_example' # str | ID of the order.
line_item_id = 'line_item_id_example' # str | ID of the line item.
address = OrderCloud.Address() # Address | 

try: 
    response = LineItemApi.set_shipping_address(buyer_id, order_id, line_item_id, address)
    print(response)
except ApiException as e:
    print("Exception when calling LineItemApi->set_shipping_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
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

# **update**
> LineItem update(buyer_id, order_id, line_item_id, line_item)



### Example 
```python
import OrderCloud as oc
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an acess_token (see the Getting Started guide)

# create an instance of the API class
LineItemApi = OrderCloud.LineItemApi()
buyer_id = 'buyer_id_example' # str | ID of the buyer.
order_id = 'order_id_example' # str | ID of the order.
line_item_id = 'line_item_id_example' # str | ID of the line item.
line_item = OrderCloud.LineItem() # LineItem | 

try: 
    response = LineItemApi.update(buyer_id, order_id, line_item_id, line_item)
    print(response)
except ApiException as e:
    print("Exception when calling LineItemApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
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

