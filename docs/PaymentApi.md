# OrderCloud.PaymentApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orders_direction_order_id_payments_get**](PaymentApi.md#orders_direction_order_id_payments_get) | **GET** /orders/{direction}/{orderID}/payments | 
[**orders_direction_order_id_payments_payment_id_delete**](PaymentApi.md#orders_direction_order_id_payments_payment_id_delete) | **DELETE** /orders/{direction}/{orderID}/payments/{paymentID} | 
[**orders_direction_order_id_payments_payment_id_get**](PaymentApi.md#orders_direction_order_id_payments_payment_id_get) | **GET** /orders/{direction}/{orderID}/payments/{paymentID} | 
[**orders_direction_order_id_payments_payment_id_patch**](PaymentApi.md#orders_direction_order_id_payments_payment_id_patch) | **PATCH** /orders/{direction}/{orderID}/payments/{paymentID} | 
[**orders_direction_order_id_payments_payment_id_transactions_post**](PaymentApi.md#orders_direction_order_id_payments_payment_id_transactions_post) | **POST** /orders/{direction}/{orderID}/payments/{paymentID}/transactions | 
[**orders_direction_order_id_payments_payment_id_transactions_transaction_id_delete**](PaymentApi.md#orders_direction_order_id_payments_payment_id_transactions_transaction_id_delete) | **DELETE** /orders/{direction}/{orderID}/payments/{paymentID}/transactions/{transactionID} | 
[**orders_direction_order_id_payments_post**](PaymentApi.md#orders_direction_order_id_payments_post) | **POST** /orders/{direction}/{orderID}/payments | 


# **orders_direction_order_id_payments_get**
> ListPayment orders_direction_order_id_payments_get(direction, order_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
PaymentApi = OrderCloud.PaymentApi
direction = 'direction_example' # str | Direction of the payment. Possible values: Incoming, Outgoing.
order_id = 'order_id_example' # str | ID of the order.
search = 'search_example' # str | Search of the payment. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the payment. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the payment. (optional)
page = 56 # int | Page of the payment. (optional)
page_size = 56 # int | Page size of the payment. (optional)

try: 
    response = PaymentApi.orders_direction_order_id_payments_get(direction, order_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling PaymentApi->orders_direction_order_id_payments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| Direction of the payment. Possible values: Incoming, Outgoing. | 
 **order_id** | **str**| ID of the order. | 
 **search** | **str**| Search of the payment. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the payment. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the payment. | [optional] 
 **page** | **int**| Page of the payment. | [optional] 
 **page_size** | **int**| Page size of the payment. | [optional] 

### Return type

[**ListPayment**](ListPayment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_direction_order_id_payments_payment_id_delete**
> orders_direction_order_id_payments_payment_id_delete(direction, order_id, payment_id)



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
    PaymentApi.orders_direction_order_id_payments_payment_id_delete(direction, order_id, payment_id)
except ApiException as e:
    print("Exception when calling PaymentApi->orders_direction_order_id_payments_payment_id_delete: %s\n" % e)
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

# **orders_direction_order_id_payments_payment_id_get**
> Payment orders_direction_order_id_payments_payment_id_get(direction, order_id, payment_id)



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
    response = PaymentApi.orders_direction_order_id_payments_payment_id_get(direction, order_id, payment_id)
    print(response)
except ApiException as e:
    print("Exception when calling PaymentApi->orders_direction_order_id_payments_payment_id_get: %s\n" % e)
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

# **orders_direction_order_id_payments_payment_id_patch**
> Payment orders_direction_order_id_payments_payment_id_patch(direction, order_id, payment_id, partial_payment)



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
    response = PaymentApi.orders_direction_order_id_payments_payment_id_patch(direction, order_id, payment_id, partial_payment)
    print(response)
except ApiException as e:
    print("Exception when calling PaymentApi->orders_direction_order_id_payments_payment_id_patch: %s\n" % e)
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

# **orders_direction_order_id_payments_payment_id_transactions_post**
> Payment orders_direction_order_id_payments_payment_id_transactions_post(direction, order_id, payment_id, transaction)



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
    response = PaymentApi.orders_direction_order_id_payments_payment_id_transactions_post(direction, order_id, payment_id, transaction)
    print(response)
except ApiException as e:
    print("Exception when calling PaymentApi->orders_direction_order_id_payments_payment_id_transactions_post: %s\n" % e)
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

# **orders_direction_order_id_payments_payment_id_transactions_transaction_id_delete**
> orders_direction_order_id_payments_payment_id_transactions_transaction_id_delete(direction, order_id, payment_id, transaction_id)



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
    PaymentApi.orders_direction_order_id_payments_payment_id_transactions_transaction_id_delete(direction, order_id, payment_id, transaction_id)
except ApiException as e:
    print("Exception when calling PaymentApi->orders_direction_order_id_payments_payment_id_transactions_transaction_id_delete: %s\n" % e)
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

# **orders_direction_order_id_payments_post**
> Payment orders_direction_order_id_payments_post(direction, order_id, payment)



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
    response = PaymentApi.orders_direction_order_id_payments_post(direction, order_id, payment)
    print(response)
except ApiException as e:
    print("Exception when calling PaymentApi->orders_direction_order_id_payments_post: %s\n" % e)
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

