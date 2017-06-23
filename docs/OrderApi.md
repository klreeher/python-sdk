# OrderCloud.OrderApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orders_direction_get**](OrderApi.md#orders_direction_get) | **GET** /orders/{direction} | 
[**orders_direction_order_id_approvals_get**](OrderApi.md#orders_direction_order_id_approvals_get) | **GET** /orders/{direction}/{orderID}/approvals | 
[**orders_direction_order_id_approve_post**](OrderApi.md#orders_direction_order_id_approve_post) | **POST** /orders/{direction}/{orderID}/approve | 
[**orders_direction_order_id_billto_patch**](OrderApi.md#orders_direction_order_id_billto_patch) | **PATCH** /orders/{direction}/{orderID}/billto | 
[**orders_direction_order_id_billto_put**](OrderApi.md#orders_direction_order_id_billto_put) | **PUT** /orders/{direction}/{orderID}/billto | 
[**orders_direction_order_id_cancel_post**](OrderApi.md#orders_direction_order_id_cancel_post) | **POST** /orders/{direction}/{orderID}/cancel | 
[**orders_direction_order_id_decline_post**](OrderApi.md#orders_direction_order_id_decline_post) | **POST** /orders/{direction}/{orderID}/decline | 
[**orders_direction_order_id_delete**](OrderApi.md#orders_direction_order_id_delete) | **DELETE** /orders/{direction}/{orderID} | 
[**orders_direction_order_id_eligibleapprovers_get**](OrderApi.md#orders_direction_order_id_eligibleapprovers_get) | **GET** /orders/{direction}/{orderID}/eligibleapprovers | 
[**orders_direction_order_id_get**](OrderApi.md#orders_direction_order_id_get) | **GET** /orders/{direction}/{orderID} | 
[**orders_direction_order_id_patch**](OrderApi.md#orders_direction_order_id_patch) | **PATCH** /orders/{direction}/{orderID} | 
[**orders_direction_order_id_promotions_get**](OrderApi.md#orders_direction_order_id_promotions_get) | **GET** /orders/{direction}/{orderID}/promotions | 
[**orders_direction_order_id_promotions_promo_code_delete**](OrderApi.md#orders_direction_order_id_promotions_promo_code_delete) | **DELETE** /orders/{direction}/{orderID}/promotions/{promoCode} | 
[**orders_direction_order_id_promotions_promo_code_post**](OrderApi.md#orders_direction_order_id_promotions_promo_code_post) | **POST** /orders/{direction}/{orderID}/promotions/{promoCode} | 
[**orders_direction_order_id_put**](OrderApi.md#orders_direction_order_id_put) | **PUT** /orders/{direction}/{orderID} | 
[**orders_direction_order_id_ship_post**](OrderApi.md#orders_direction_order_id_ship_post) | **POST** /orders/{direction}/{orderID}/ship | 
[**orders_direction_order_id_shipto_patch**](OrderApi.md#orders_direction_order_id_shipto_patch) | **PATCH** /orders/{direction}/{orderID}/shipto | 
[**orders_direction_order_id_shipto_put**](OrderApi.md#orders_direction_order_id_shipto_put) | **PUT** /orders/{direction}/{orderID}/shipto | 
[**orders_direction_order_id_submit_post**](OrderApi.md#orders_direction_order_id_submit_post) | **POST** /orders/{direction}/{orderID}/submit | 
[**orders_direction_post**](OrderApi.md#orders_direction_post) | **POST** /orders/{direction} | 


# **orders_direction_get**
> ListOrder orders_direction_get(direction, buyer_id=buyer_id, supplier_id=supplier_id, _from=_from, to=to, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
OrderApi = OrderCloud.OrderApi
direction = 'direction_example' # str | Direction of the order. Possible values: Incoming, Outgoing.
buyer_id = 'buyer_id_example' # str | ID of the buyer. (optional)
supplier_id = 'supplier_id_example' # str | ID of the supplier. (optional)
_from = '_from_example' # str | Lower bound of date range that the order was created. (optional)
to = 'to_example' # str | Upper bound of date range that the order was created. (optional)
search = 'search_example' # str | Search of the order. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the order. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the order. (optional)
page = 56 # int | Page of the order. (optional)
page_size = 56 # int | Page size of the order. (optional)

try: 
    response = OrderApi.orders_direction_get(direction, buyer_id=buyer_id, supplier_id=supplier_id, _from=_from, to=to, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->orders_direction_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the order. Possible values: Incoming, Outgoing. | 
 **buyer_id** | **str**| ID of the buyer. | [optional] 
 **supplier_id** | **str**| ID of the supplier. | [optional] 
 **_from** | **str**| Lower bound of date range that the order was created. | [optional] 
 **to** | **str**| Upper bound of date range that the order was created. | [optional] 
 **search** | **str**| Search of the order. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the order. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the order. | [optional] 
 **page** | **int**| Page of the order. | [optional] 
 **page_size** | **int**| Page size of the order. | [optional] 

### Return type

[**ListOrder**](ListOrder.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_direction_order_id_approvals_get**
> ListOrderApproval orders_direction_order_id_approvals_get(direction, order_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
OrderApi = OrderCloud.OrderApi
direction = 'direction_example' # str | Direction of the order. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
search = 'search_example' # str | Search of the order. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the order. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the order. (optional)
page = 56 # int | Page of the order. (optional)
page_size = 56 # int | Page size of the order. (optional)

try: 
    response = OrderApi.orders_direction_order_id_approvals_get(direction, order_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->orders_direction_order_id_approvals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the order. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **search** | **str**| Search of the order. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the order. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the order. | [optional] 
 **page** | **int**| Page of the order. | [optional] 
 **page_size** | **int**| Page size of the order. | [optional] 

### Return type

[**ListOrderApproval**](ListOrderApproval.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_direction_order_id_approve_post**
> Order orders_direction_order_id_approve_post(direction, order_id, info)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
OrderApi = OrderCloud.OrderApi
direction = 'direction_example' # str | Direction of the order. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
info = OrderCloud.OrderApprovalInfo() # OrderApprovalInfo | 

try: 
    response = OrderApi.orders_direction_order_id_approve_post(direction, order_id, info)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->orders_direction_order_id_approve_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the order. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **info** | [**OrderApprovalInfo**](OrderApprovalInfo.md)|  | 

### Return type

[**Order**](Order.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_direction_order_id_billto_patch**
> Order orders_direction_order_id_billto_patch(direction, order_id, address)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
OrderApi = OrderCloud.OrderApi
direction = 'direction_example' # str | Direction of the order. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
address = OrderCloud.Address() # Address | 

try: 
    response = OrderApi.orders_direction_order_id_billto_patch(direction, order_id, address)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->orders_direction_order_id_billto_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the order. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **address** | [**Address**](Address.md)|  | 

### Return type

[**Order**](Order.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_direction_order_id_billto_put**
> Order orders_direction_order_id_billto_put(direction, order_id, address)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
OrderApi = OrderCloud.OrderApi
direction = 'direction_example' # str | Direction of the order. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
address = OrderCloud.Address() # Address | 

try: 
    response = OrderApi.orders_direction_order_id_billto_put(direction, order_id, address)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->orders_direction_order_id_billto_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the order. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **address** | [**Address**](Address.md)|  | 

### Return type

[**Order**](Order.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_direction_order_id_cancel_post**
> Order orders_direction_order_id_cancel_post(direction, order_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
OrderApi = OrderCloud.OrderApi
direction = 'direction_example' # str | Direction of the order. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.

try: 
    response = OrderApi.orders_direction_order_id_cancel_post(direction, order_id)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->orders_direction_order_id_cancel_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the order. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 

### Return type

[**Order**](Order.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_direction_order_id_decline_post**
> Order orders_direction_order_id_decline_post(direction, order_id, info)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
OrderApi = OrderCloud.OrderApi
direction = 'direction_example' # str | Direction of the order. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
info = OrderCloud.OrderApprovalInfo() # OrderApprovalInfo | 

try: 
    response = OrderApi.orders_direction_order_id_decline_post(direction, order_id, info)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->orders_direction_order_id_decline_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the order. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **info** | [**OrderApprovalInfo**](OrderApprovalInfo.md)|  | 

### Return type

[**Order**](Order.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_direction_order_id_delete**
> orders_direction_order_id_delete(direction, order_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
OrderApi = OrderCloud.OrderApi
direction = 'direction_example' # str | Direction of the order. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.

try: 
    OrderApi.orders_direction_order_id_delete(direction, order_id)
except ApiException as e:
    print("Exception when calling OrderApi->orders_direction_order_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the order. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_direction_order_id_eligibleapprovers_get**
> ListUser orders_direction_order_id_eligibleapprovers_get(direction, order_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
OrderApi = OrderCloud.OrderApi
direction = 'direction_example' # str | Direction of the order. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
search = 'search_example' # str | Search of the order. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the order. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the order. (optional)
page = 56 # int | Page of the order. (optional)
page_size = 56 # int | Page size of the order. (optional)

try: 
    response = OrderApi.orders_direction_order_id_eligibleapprovers_get(direction, order_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->orders_direction_order_id_eligibleapprovers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the order. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **search** | **str**| Search of the order. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the order. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the order. | [optional] 
 **page** | **int**| Page of the order. | [optional] 
 **page_size** | **int**| Page size of the order. | [optional] 

### Return type

[**ListUser**](ListUser.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_direction_order_id_get**
> Order orders_direction_order_id_get(direction, order_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
OrderApi = OrderCloud.OrderApi
direction = 'direction_example' # str | Direction of the order. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.

try: 
    response = OrderApi.orders_direction_order_id_get(direction, order_id)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->orders_direction_order_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the order. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 

### Return type

[**Order**](Order.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_direction_order_id_patch**
> Order orders_direction_order_id_patch(direction, order_id, partial_order)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
OrderApi = OrderCloud.OrderApi
direction = 'direction_example' # str | Direction of the order. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
partial_order = OrderCloud.Order() # Order | 

try: 
    response = OrderApi.orders_direction_order_id_patch(direction, order_id, partial_order)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->orders_direction_order_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the order. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **partial_order** | [**Order**](Order.md)|  | 

### Return type

[**Order**](Order.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_direction_order_id_promotions_get**
> ListOrderPromotion orders_direction_order_id_promotions_get(direction, order_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
OrderApi = OrderCloud.OrderApi
direction = 'direction_example' # str | Direction of the order. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
search = 'search_example' # str | Search of the order. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the order. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the order. (optional)
page = 56 # int | Page of the order. (optional)
page_size = 56 # int | Page size of the order. (optional)

try: 
    response = OrderApi.orders_direction_order_id_promotions_get(direction, order_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->orders_direction_order_id_promotions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the order. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **search** | **str**| Search of the order. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the order. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the order. | [optional] 
 **page** | **int**| Page of the order. | [optional] 
 **page_size** | **int**| Page size of the order. | [optional] 

### Return type

[**ListOrderPromotion**](ListOrderPromotion.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_direction_order_id_promotions_promo_code_delete**
> Order orders_direction_order_id_promotions_promo_code_delete(direction, order_id, promo_code)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
OrderApi = OrderCloud.OrderApi
direction = 'direction_example' # str | Direction of the order. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
promo_code = 'promo_code_example' # str | Promo code of the order.

try: 
    response = OrderApi.orders_direction_order_id_promotions_promo_code_delete(direction, order_id, promo_code)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->orders_direction_order_id_promotions_promo_code_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the order. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **promo_code** | **str**| Promo code of the order. | 

### Return type

[**Order**](Order.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_direction_order_id_promotions_promo_code_post**
> Promotion orders_direction_order_id_promotions_promo_code_post(direction, order_id, promo_code)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
OrderApi = OrderCloud.OrderApi
direction = 'direction_example' # str | Direction of the order. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
promo_code = 'promo_code_example' # str | Promo code of the order.

try: 
    response = OrderApi.orders_direction_order_id_promotions_promo_code_post(direction, order_id, promo_code)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->orders_direction_order_id_promotions_promo_code_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the order. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **promo_code** | **str**| Promo code of the order. | 

### Return type

[**Promotion**](Promotion.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_direction_order_id_put**
> Order orders_direction_order_id_put(direction, order_id, order)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
OrderApi = OrderCloud.OrderApi
direction = 'direction_example' # str | Direction of the order. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
order = OrderCloud.Order() # Order | 

try: 
    response = OrderApi.orders_direction_order_id_put(direction, order_id, order)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->orders_direction_order_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the order. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **order** | [**Order**](Order.md)|  | 

### Return type

[**Order**](Order.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_direction_order_id_ship_post**
> Order orders_direction_order_id_ship_post(direction, order_id, shipment)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
OrderApi = OrderCloud.OrderApi
direction = 'direction_example' # str | Direction of the order. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
shipment = OrderCloud.BuyerShipment() # BuyerShipment | 

try: 
    response = OrderApi.orders_direction_order_id_ship_post(direction, order_id, shipment)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->orders_direction_order_id_ship_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the order. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **shipment** | [**BuyerShipment**](BuyerShipment.md)|  | 

### Return type

[**Order**](Order.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_direction_order_id_shipto_patch**
> Order orders_direction_order_id_shipto_patch(direction, order_id, address)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
OrderApi = OrderCloud.OrderApi
direction = 'direction_example' # str | Direction of the order. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
address = OrderCloud.Address() # Address | 

try: 
    response = OrderApi.orders_direction_order_id_shipto_patch(direction, order_id, address)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->orders_direction_order_id_shipto_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the order. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **address** | [**Address**](Address.md)|  | 

### Return type

[**Order**](Order.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_direction_order_id_shipto_put**
> Order orders_direction_order_id_shipto_put(direction, order_id, address)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
OrderApi = OrderCloud.OrderApi
direction = 'direction_example' # str | Direction of the order. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
address = OrderCloud.Address() # Address | 

try: 
    response = OrderApi.orders_direction_order_id_shipto_put(direction, order_id, address)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->orders_direction_order_id_shipto_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the order. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **address** | [**Address**](Address.md)|  | 

### Return type

[**Order**](Order.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_direction_order_id_submit_post**
> Order orders_direction_order_id_submit_post(direction, order_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
OrderApi = OrderCloud.OrderApi
direction = 'direction_example' # str | Direction of the order. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.

try: 
    response = OrderApi.orders_direction_order_id_submit_post(direction, order_id)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->orders_direction_order_id_submit_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the order. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 

### Return type

[**Order**](Order.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_direction_post**
> Order orders_direction_post(direction, order)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
OrderApi = OrderCloud.OrderApi
direction = 'direction_example' # str | Direction of the order. Possible values: Incoming, Outgoing.
order = OrderCloud.Order() # Order | 

try: 
    response = OrderApi.orders_direction_post(direction, order)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->orders_direction_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the order. Possible values: Incoming, Outgoing. | 
 **order** | [**Order**](Order.md)|  | 

### Return type

[**Order**](Order.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

