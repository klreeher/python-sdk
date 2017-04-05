# OrderCloud.PaymentApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](PaymentApi.md#create) | **POST** /orders/{direction}/{orderID}/payments | 
[**create_transaction**](PaymentApi.md#create_transaction) | **POST** /orders/{direction}/{orderID}/payments/{paymentID}/transactions | 
[**delete**](PaymentApi.md#delete) | **DELETE** /orders/{direction}/{orderID}/payments/{paymentID} | 
[**delete_transaction**](PaymentApi.md#delete_transaction) | **DELETE** /orders/{direction}/{orderID}/payments/{paymentID}/transactions/{transactionID} | 
[**get**](PaymentApi.md#get) | **GET** /orders/{direction}/{orderID}/payments/{paymentID} | 
[**list**](PaymentApi.md#list) | **GET** /orders/{direction}/{orderID}/payments | 
[**patch**](PaymentApi.md#patch) | **PATCH** /orders/{direction}/{orderID}/payments/{paymentID} | 


# **create**
> Payment create(direction, order_id, payment)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
PaymentApi = OrderCloud.PaymentApi
direction = 'direction_example' # str | Direction of the payment. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
payment = OrderCloud.Payment() # Payment | 

try: 
    response = PaymentApi.create(direction, order_id, payment)
    print(response)
except ApiException as e:
    print("Exception when calling PaymentApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the payment. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **payment** | [**Payment**](Payment.md)|  | 

### Return type

[**Payment**](Payment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_transaction**
> Payment create_transaction(direction, order_id, payment_id, transaction)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
PaymentApi = OrderCloud.PaymentApi
direction = 'direction_example' # str | Direction of the payment. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
payment_id = 'payment_id_example' # str | ID of the payment.
transaction = OrderCloud.PaymentTransaction() # PaymentTransaction | 

try: 
    response = PaymentApi.create_transaction(direction, order_id, payment_id, transaction)
    print(response)
except ApiException as e:
    print("Exception when calling PaymentApi->create_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the payment. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **payment_id** | **str**| ID of the payment. | 
 **transaction** | [**PaymentTransaction**](PaymentTransaction.md)|  | 

### Return type

[**Payment**](Payment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(direction, order_id, payment_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
PaymentApi = OrderCloud.PaymentApi
direction = 'direction_example' # str | Direction of the payment. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
payment_id = 'payment_id_example' # str | ID of the payment.

try: 
    PaymentApi.delete(direction, order_id, payment_id)
except ApiException as e:
    print("Exception when calling PaymentApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the payment. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **payment_id** | **str**| ID of the payment. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transaction**
> delete_transaction(direction, order_id, payment_id, transaction_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
PaymentApi = OrderCloud.PaymentApi
direction = 'direction_example' # str | Direction of the payment. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
payment_id = 'payment_id_example' # str | ID of the payment.
transaction_id = 'transaction_id_example' # str | ID of the transaction.

try: 
    PaymentApi.delete_transaction(direction, order_id, payment_id, transaction_id)
except ApiException as e:
    print("Exception when calling PaymentApi->delete_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the payment. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **payment_id** | **str**| ID of the payment. | 
 **transaction_id** | **str**| ID of the transaction. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Payment get(direction, order_id, payment_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
PaymentApi = OrderCloud.PaymentApi
direction = 'direction_example' # str | Direction of the payment. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
payment_id = 'payment_id_example' # str | ID of the payment.

try: 
    response = PaymentApi.get(direction, order_id, payment_id)
    print(response)
except ApiException as e:
    print("Exception when calling PaymentApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the payment. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **payment_id** | **str**| ID of the payment. | 

### Return type

[**Payment**](Payment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ListPayment list(direction, order_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
PaymentApi = OrderCloud.PaymentApi
direction = 'direction_example' # str | Direction of the payment. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = PaymentApi.list(direction, order_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling PaymentApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the payment. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **search** | **str**| Word or phrase to search for. | [optional] 
 **search_on** | **str**| Comma-delimited list of fields to search on. | [optional] 
 **sort_by** | **str**| Comma-delimited list of fields to sort by. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 
 **filters** | [**dict(str, str)**](str.md)| Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or &#39;xp.???&#39; | [optional] 

### Return type

[**ListPayment**](ListPayment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch**
> Payment patch(direction, order_id, payment_id, partial_payment)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
PaymentApi = OrderCloud.PaymentApi
direction = 'direction_example' # str | Direction of the payment. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
payment_id = 'payment_id_example' # str | ID of the payment.
partial_payment = OrderCloud.Payment() # Payment | 

try: 
    response = PaymentApi.patch(direction, order_id, payment_id, partial_payment)
    print(response)
except ApiException as e:
    print("Exception when calling PaymentApi->patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the payment. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **payment_id** | **str**| ID of the payment. | 
 **partial_payment** | [**Payment**](Payment.md)|  | 

### Return type

[**Payment**](Payment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

