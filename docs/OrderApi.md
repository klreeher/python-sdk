# OrderCloud.OrderApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_promotion**](OrderApi.md#add_promotion) | **POST** /orders/{direction}/{orderID}/promotions/{promoCode} | 
[**approve**](OrderApi.md#approve) | **POST** /orders/{direction}/{orderID}/approve | 
[**cancel**](OrderApi.md#cancel) | **POST** /orders/{direction}/{orderID}/cancel | 
[**create**](OrderApi.md#create) | **POST** /orders/{direction} | 
[**decline**](OrderApi.md#decline) | **POST** /orders/{direction}/{orderID}/decline | 
[**delete**](OrderApi.md#delete) | **DELETE** /orders/{direction}/{orderID} | 
[**get**](OrderApi.md#get) | **GET** /orders/{direction}/{orderID} | 
[**list**](OrderApi.md#list) | **GET** /orders/{direction} | 
[**list_approvals**](OrderApi.md#list_approvals) | **GET** /orders/{direction}/{orderID}/approvals | 
[**list_eligible_approvers**](OrderApi.md#list_eligible_approvers) | **GET** /orders/{direction}/{orderID}/eligibleapprovers | 
[**list_promotions**](OrderApi.md#list_promotions) | **GET** /orders/{direction}/{orderID}/promotions | 
[**patch**](OrderApi.md#patch) | **PATCH** /orders/{direction}/{orderID} | 
[**patch_billing_address**](OrderApi.md#patch_billing_address) | **PATCH** /orders/{direction}/{orderID}/billto | 
[**patch_shipping_address**](OrderApi.md#patch_shipping_address) | **PATCH** /orders/{direction}/{orderID}/shipto | 
[**remove_promotion**](OrderApi.md#remove_promotion) | **DELETE** /orders/{direction}/{orderID}/promotions/{promoCode} | 
[**set_billing_address**](OrderApi.md#set_billing_address) | **PUT** /orders/{direction}/{orderID}/billto | 
[**set_shipping_address**](OrderApi.md#set_shipping_address) | **PUT** /orders/{direction}/{orderID}/shipto | 
[**ship**](OrderApi.md#ship) | **POST** /orders/{direction}/{orderID}/ship | 
[**submit**](OrderApi.md#submit) | **POST** /orders/{direction}/{orderID}/submit | 
[**update**](OrderApi.md#update) | **PUT** /orders/{direction}/{orderID} | 


# **add_promotion**
> Promotion add_promotion(direction, order_id, promo_code)



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
    response = OrderApi.add_promotion(direction, order_id, promo_code)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->add_promotion: %s\n" % e)
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

# **approve**
> Order approve(direction, order_id, info)



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
    response = OrderApi.approve(direction, order_id, info)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->approve: %s\n" % e)
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

# **cancel**
> Order cancel(direction, order_id)



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
    response = OrderApi.cancel(direction, order_id)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->cancel: %s\n" % e)
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

# **create**
> Order create(direction, order)



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
    response = OrderApi.create(direction, order)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->create: %s\n" % e)
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

# **decline**
> Order decline(direction, order_id, info)



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
    response = OrderApi.decline(direction, order_id, info)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->decline: %s\n" % e)
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

# **delete**
> delete(direction, order_id)



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
    OrderApi.delete(direction, order_id)
except ApiException as e:
    print("Exception when calling OrderApi->delete: %s\n" % e)
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

# **get**
> Order get(direction, order_id)



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
    response = OrderApi.get(direction, order_id)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->get: %s\n" % e)
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

# **list**
> ListOrder list(direction, buyer_id=buyer_id, supplier_id=supplier_id, _from=_from, to=to, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



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
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = OrderApi.list(direction, buyer_id=buyer_id, supplier_id=supplier_id, _from=_from, to=to, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the order. Possible values: Incoming, Outgoing. | 
 **buyer_id** | **str**| ID of the buyer. | [optional] 
 **supplier_id** | **str**| ID of the supplier. | [optional] 
 **_from** | **str**| Lower bound of date range that the order was created. | [optional] 
 **to** | **str**| Upper bound of date range that the order was created. | [optional] 
 **search** | **str**| Word or phrase to search for. | [optional] 
 **search_on** | **str**| Comma-delimited list of fields to search on. | [optional] 
 **sort_by** | **str**| Comma-delimited list of fields to sort by. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 
 **filters** | [**dict(str, str)**](str.md)| Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or &#39;xp.???&#39; | [optional] 

### Return type

[**ListOrder**](ListOrder.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_approvals**
> ListOrderApproval list_approvals(direction, order_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
OrderApi = OrderCloud.OrderApi
direction = 'direction_example' # str | Direction of the order. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = OrderApi.list_approvals(direction, order_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->list_approvals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the order. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **search** | **str**| Word or phrase to search for. | [optional] 
 **search_on** | **str**| Comma-delimited list of fields to search on. | [optional] 
 **sort_by** | **str**| Comma-delimited list of fields to sort by. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 
 **filters** | [**dict(str, str)**](str.md)| Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or &#39;xp.???&#39; | [optional] 

### Return type

[**ListOrderApproval**](ListOrderApproval.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_eligible_approvers**
> ListUser list_eligible_approvers(direction, order_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
OrderApi = OrderCloud.OrderApi
direction = 'direction_example' # str | Direction of the order. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = OrderApi.list_eligible_approvers(direction, order_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->list_eligible_approvers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the order. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **search** | **str**| Word or phrase to search for. | [optional] 
 **search_on** | **str**| Comma-delimited list of fields to search on. | [optional] 
 **sort_by** | **str**| Comma-delimited list of fields to sort by. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 
 **filters** | [**dict(str, str)**](str.md)| Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or &#39;xp.???&#39; | [optional] 

### Return type

[**ListUser**](ListUser.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_promotions**
> ListOrderPromotion list_promotions(direction, order_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
OrderApi = OrderCloud.OrderApi
direction = 'direction_example' # str | Direction of the order. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = OrderApi.list_promotions(direction, order_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->list_promotions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the order. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **search** | **str**| Word or phrase to search for. | [optional] 
 **search_on** | **str**| Comma-delimited list of fields to search on. | [optional] 
 **sort_by** | **str**| Comma-delimited list of fields to sort by. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 
 **filters** | [**dict(str, str)**](str.md)| Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or &#39;xp.???&#39; | [optional] 

### Return type

[**ListOrderPromotion**](ListOrderPromotion.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch**
> Order patch(direction, order_id, partial_order)



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
    response = OrderApi.patch(direction, order_id, partial_order)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->patch: %s\n" % e)
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

# **patch_billing_address**
> Order patch_billing_address(direction, order_id, address)



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
    response = OrderApi.patch_billing_address(direction, order_id, address)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->patch_billing_address: %s\n" % e)
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

# **patch_shipping_address**
> Order patch_shipping_address(direction, order_id, address)



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
    response = OrderApi.patch_shipping_address(direction, order_id, address)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->patch_shipping_address: %s\n" % e)
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

# **remove_promotion**
> Order remove_promotion(direction, order_id, promo_code)



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
    response = OrderApi.remove_promotion(direction, order_id, promo_code)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->remove_promotion: %s\n" % e)
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

# **set_billing_address**
> Order set_billing_address(direction, order_id, address)



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
    response = OrderApi.set_billing_address(direction, order_id, address)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->set_billing_address: %s\n" % e)
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

# **set_shipping_address**
> Order set_shipping_address(direction, order_id, address)



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
    response = OrderApi.set_shipping_address(direction, order_id, address)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->set_shipping_address: %s\n" % e)
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

# **ship**
> Order ship(direction, order_id, shipment)



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
    response = OrderApi.ship(direction, order_id, shipment)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->ship: %s\n" % e)
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

# **submit**
> Order submit(direction, order_id)



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
    response = OrderApi.submit(direction, order_id)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->submit: %s\n" % e)
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

# **update**
> Order update(direction, order_id, order)



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
    response = OrderApi.update(direction, order_id, order)
    print(response)
except ApiException as e:
    print("Exception when calling OrderApi->update: %s\n" % e)
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

