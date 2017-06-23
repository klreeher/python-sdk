# OrderCloud.CreditCardApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buyers_buyer_id_creditcards_assignments_get**](CreditCardApi.md#buyers_buyer_id_creditcards_assignments_get) | **GET** /buyers/{buyerID}/creditcards/assignments | 
[**buyers_buyer_id_creditcards_assignments_post**](CreditCardApi.md#buyers_buyer_id_creditcards_assignments_post) | **POST** /buyers/{buyerID}/creditcards/assignments | 
[**buyers_buyer_id_creditcards_credit_card_id_assignments_delete**](CreditCardApi.md#buyers_buyer_id_creditcards_credit_card_id_assignments_delete) | **DELETE** /buyers/{buyerID}/creditcards/{creditCardID}/assignments | 
[**buyers_buyer_id_creditcards_credit_card_id_delete**](CreditCardApi.md#buyers_buyer_id_creditcards_credit_card_id_delete) | **DELETE** /buyers/{buyerID}/creditcards/{creditCardID} | 
[**buyers_buyer_id_creditcards_credit_card_id_get**](CreditCardApi.md#buyers_buyer_id_creditcards_credit_card_id_get) | **GET** /buyers/{buyerID}/creditcards/{creditCardID} | 
[**buyers_buyer_id_creditcards_credit_card_id_patch**](CreditCardApi.md#buyers_buyer_id_creditcards_credit_card_id_patch) | **PATCH** /buyers/{buyerID}/creditcards/{creditCardID} | 
[**buyers_buyer_id_creditcards_credit_card_id_put**](CreditCardApi.md#buyers_buyer_id_creditcards_credit_card_id_put) | **PUT** /buyers/{buyerID}/creditcards/{creditCardID} | 
[**buyers_buyer_id_creditcards_get**](CreditCardApi.md#buyers_buyer_id_creditcards_get) | **GET** /buyers/{buyerID}/creditcards | 
[**buyers_buyer_id_creditcards_post**](CreditCardApi.md#buyers_buyer_id_creditcards_post) | **POST** /buyers/{buyerID}/creditcards | 


# **buyers_buyer_id_creditcards_assignments_get**
> ListCreditCardAssignment buyers_buyer_id_creditcards_assignments_get(buyer_id, credit_card_id=credit_card_id, user_id=user_id, user_group_id=user_group_id, level=level, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CreditCardApi = OrderCloud.CreditCardApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
credit_card_id = 'credit_card_id_example' # str | ID of the credit card. (optional)
user_id = 'user_id_example' # str | ID of the user. (optional)
user_group_id = 'user_group_id_example' # str | ID of the user group. (optional)
level = 'level_example' # str | Level of the credit card. (optional)
page = 56 # int | Page of the credit card. (optional)
page_size = 56 # int | Page size of the credit card. (optional)

try: 
    response = CreditCardApi.buyers_buyer_id_creditcards_assignments_get(buyer_id, credit_card_id=credit_card_id, user_id=user_id, user_group_id=user_group_id, level=level, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling CreditCardApi->buyers_buyer_id_creditcards_assignments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **credit_card_id** | **str**| ID of the credit card. | [optional] 
 **user_id** | **str**| ID of the user. | [optional] 
 **user_group_id** | **str**| ID of the user group. | [optional] 
 **level** | **str**| Level of the credit card. | [optional] 
 **page** | **int**| Page of the credit card. | [optional] 
 **page_size** | **int**| Page size of the credit card. | [optional] 

### Return type

[**ListCreditCardAssignment**](ListCreditCardAssignment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_creditcards_assignments_post**
> buyers_buyer_id_creditcards_assignments_post(buyer_id, assignment)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CreditCardApi = OrderCloud.CreditCardApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
assignment = OrderCloud.CreditCardAssignment() # CreditCardAssignment | 

try: 
    CreditCardApi.buyers_buyer_id_creditcards_assignments_post(buyer_id, assignment)
except ApiException as e:
    print("Exception when calling CreditCardApi->buyers_buyer_id_creditcards_assignments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **assignment** | [**CreditCardAssignment**](CreditCardAssignment.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_creditcards_credit_card_id_assignments_delete**
> buyers_buyer_id_creditcards_credit_card_id_assignments_delete(buyer_id, credit_card_id, user_id=user_id, user_group_id=user_group_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CreditCardApi = OrderCloud.CreditCardApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
credit_card_id = 'credit_card_id_example' # str | ID of the credit card.
user_id = 'user_id_example' # str | ID of the user. (optional)
user_group_id = 'user_group_id_example' # str | ID of the user group. (optional)

try: 
    CreditCardApi.buyers_buyer_id_creditcards_credit_card_id_assignments_delete(buyer_id, credit_card_id, user_id=user_id, user_group_id=user_group_id)
except ApiException as e:
    print("Exception when calling CreditCardApi->buyers_buyer_id_creditcards_credit_card_id_assignments_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **credit_card_id** | **str**| ID of the credit card. | 
 **user_id** | **str**| ID of the user. | [optional] 
 **user_group_id** | **str**| ID of the user group. | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_creditcards_credit_card_id_delete**
> buyers_buyer_id_creditcards_credit_card_id_delete(buyer_id, credit_card_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CreditCardApi = OrderCloud.CreditCardApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
credit_card_id = 'credit_card_id_example' # str | ID of the credit card.

try: 
    CreditCardApi.buyers_buyer_id_creditcards_credit_card_id_delete(buyer_id, credit_card_id)
except ApiException as e:
    print("Exception when calling CreditCardApi->buyers_buyer_id_creditcards_credit_card_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **credit_card_id** | **str**| ID of the credit card. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_creditcards_credit_card_id_get**
> CreditCard buyers_buyer_id_creditcards_credit_card_id_get(buyer_id, credit_card_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CreditCardApi = OrderCloud.CreditCardApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
credit_card_id = 'credit_card_id_example' # str | ID of the credit card.

try: 
    response = CreditCardApi.buyers_buyer_id_creditcards_credit_card_id_get(buyer_id, credit_card_id)
    print(response)
except ApiException as e:
    print("Exception when calling CreditCardApi->buyers_buyer_id_creditcards_credit_card_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **credit_card_id** | **str**| ID of the credit card. | 

### Return type

[**CreditCard**](CreditCard.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_creditcards_credit_card_id_patch**
> CreditCard buyers_buyer_id_creditcards_credit_card_id_patch(buyer_id, credit_card_id, card)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CreditCardApi = OrderCloud.CreditCardApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
credit_card_id = 'credit_card_id_example' # str | ID of the credit card.
card = OrderCloud.CreditCard() # CreditCard | 

try: 
    response = CreditCardApi.buyers_buyer_id_creditcards_credit_card_id_patch(buyer_id, credit_card_id, card)
    print(response)
except ApiException as e:
    print("Exception when calling CreditCardApi->buyers_buyer_id_creditcards_credit_card_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **credit_card_id** | **str**| ID of the credit card. | 
 **card** | [**CreditCard**](CreditCard.md)|  | 

### Return type

[**CreditCard**](CreditCard.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_creditcards_credit_card_id_put**
> CreditCard buyers_buyer_id_creditcards_credit_card_id_put(buyer_id, credit_card_id, card)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CreditCardApi = OrderCloud.CreditCardApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
credit_card_id = 'credit_card_id_example' # str | ID of the credit card.
card = OrderCloud.CreditCard() # CreditCard | 

try: 
    response = CreditCardApi.buyers_buyer_id_creditcards_credit_card_id_put(buyer_id, credit_card_id, card)
    print(response)
except ApiException as e:
    print("Exception when calling CreditCardApi->buyers_buyer_id_creditcards_credit_card_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **credit_card_id** | **str**| ID of the credit card. | 
 **card** | [**CreditCard**](CreditCard.md)|  | 

### Return type

[**CreditCard**](CreditCard.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_creditcards_get**
> ListCreditCard buyers_buyer_id_creditcards_get(buyer_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CreditCardApi = OrderCloud.CreditCardApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
search = 'search_example' # str | Search of the credit card. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the credit card. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the credit card. (optional)
page = 56 # int | Page of the credit card. (optional)
page_size = 56 # int | Page size of the credit card. (optional)

try: 
    response = CreditCardApi.buyers_buyer_id_creditcards_get(buyer_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling CreditCardApi->buyers_buyer_id_creditcards_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **search** | **str**| Search of the credit card. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the credit card. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the credit card. | [optional] 
 **page** | **int**| Page of the credit card. | [optional] 
 **page_size** | **int**| Page size of the credit card. | [optional] 

### Return type

[**ListCreditCard**](ListCreditCard.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_creditcards_post**
> CreditCard buyers_buyer_id_creditcards_post(buyer_id, card)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CreditCardApi = OrderCloud.CreditCardApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
card = OrderCloud.CreditCard() # CreditCard | 

try: 
    response = CreditCardApi.buyers_buyer_id_creditcards_post(buyer_id, card)
    print(response)
except ApiException as e:
    print("Exception when calling CreditCardApi->buyers_buyer_id_creditcards_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **card** | [**CreditCard**](CreditCard.md)|  | 

### Return type

[**CreditCard**](CreditCard.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

