# OrderCloud.CreditCardApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](CreditCardApi.md#create) | **POST** /buyers/{buyerID}/creditcards | 
[**delete**](CreditCardApi.md#delete) | **DELETE** /buyers/{buyerID}/creditcards/{creditCardID} | 
[**delete_assignment**](CreditCardApi.md#delete_assignment) | **DELETE** /buyers/{buyerID}/creditcards/{creditCardID}/assignments | 
[**get**](CreditCardApi.md#get) | **GET** /buyers/{buyerID}/creditcards/{creditCardID} | 
[**list**](CreditCardApi.md#list) | **GET** /buyers/{buyerID}/creditcards | 
[**list_assignments**](CreditCardApi.md#list_assignments) | **GET** /buyers/{buyerID}/creditcards/assignments | 
[**patch**](CreditCardApi.md#patch) | **PATCH** /buyers/{buyerID}/creditcards/{creditCardID} | 
[**save**](CreditCardApi.md#save) | **PUT** /buyers/{buyerID}/creditcards/{creditCardID} | 
[**save_assignment**](CreditCardApi.md#save_assignment) | **POST** /buyers/{buyerID}/creditcards/assignments | 


# **create**
> CreditCard create(buyer_id, credit_card)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CreditCardApi = OrderCloud.CreditCardApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
credit_card = OrderCloud.CreditCard() # CreditCard | 

try: 
    response = CreditCardApi.create(buyer_id, credit_card)
    print(response)
except ApiException as e:
    print("Exception when calling CreditCardApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **credit_card** | [**CreditCard**](CreditCard.md)|  | 

### Return type

[**CreditCard**](CreditCard.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(buyer_id, credit_card_id)



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
    CreditCardApi.delete(buyer_id, credit_card_id)
except ApiException as e:
    print("Exception when calling CreditCardApi->delete: %s\n" % e)
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

# **delete_assignment**
> delete_assignment(buyer_id, credit_card_id, user_id=user_id, user_group_id=user_group_id)



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
    CreditCardApi.delete_assignment(buyer_id, credit_card_id, user_id=user_id, user_group_id=user_group_id)
except ApiException as e:
    print("Exception when calling CreditCardApi->delete_assignment: %s\n" % e)
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

# **get**
> CreditCard get(buyer_id, credit_card_id)



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
    response = CreditCardApi.get(buyer_id, credit_card_id)
    print(response)
except ApiException as e:
    print("Exception when calling CreditCardApi->get: %s\n" % e)
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

# **list**
> ListCreditCard list(buyer_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CreditCardApi = OrderCloud.CreditCardApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = CreditCardApi.list(buyer_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling CreditCardApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **search** | **str**| Word or phrase to search for. | [optional] 
 **search_on** | **str**| Comma-delimited list of fields to search on. | [optional] 
 **sort_by** | **str**| Comma-delimited list of fields to sort by. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 
 **filters** | [**dict(str, str)**](str.md)| Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or &#39;xp.???&#39; | [optional] 

### Return type

[**ListCreditCard**](ListCreditCard.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assignments**
> ListCreditCardAssignment list_assignments(buyer_id, credit_card_id=credit_card_id, user_id=user_id, user_group_id=user_group_id, level=level, page=page, page_size=page_size)



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
level = 'level_example' # str | Level of the credit card assignment. Possible values: User, Group, Company. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)

try: 
    response = CreditCardApi.list_assignments(buyer_id, credit_card_id=credit_card_id, user_id=user_id, user_group_id=user_group_id, level=level, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling CreditCardApi->list_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **credit_card_id** | **str**| ID of the credit card. | [optional] 
 **user_id** | **str**| ID of the user. | [optional] 
 **user_group_id** | **str**| ID of the user group. | [optional] 
 **level** | **str**| Level of the credit card assignment. Possible values: User, Group, Company. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 

### Return type

[**ListCreditCardAssignment**](ListCreditCardAssignment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch**
> CreditCard patch(buyer_id, credit_card_id, partial_credit_card)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CreditCardApi = OrderCloud.CreditCardApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
credit_card_id = 'credit_card_id_example' # str | ID of the credit card.
partial_credit_card = OrderCloud.CreditCard() # CreditCard | 

try: 
    response = CreditCardApi.patch(buyer_id, credit_card_id, partial_credit_card)
    print(response)
except ApiException as e:
    print("Exception when calling CreditCardApi->patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **credit_card_id** | **str**| ID of the credit card. | 
 **partial_credit_card** | [**CreditCard**](CreditCard.md)|  | 

### Return type

[**CreditCard**](CreditCard.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save**
> CreditCard save(buyer_id, credit_card_id, credit_card)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CreditCardApi = OrderCloud.CreditCardApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
credit_card_id = 'credit_card_id_example' # str | ID of the credit card.
credit_card = OrderCloud.CreditCard() # CreditCard | 

try: 
    response = CreditCardApi.save(buyer_id, credit_card_id, credit_card)
    print(response)
except ApiException as e:
    print("Exception when calling CreditCardApi->save: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **credit_card_id** | **str**| ID of the credit card. | 
 **credit_card** | [**CreditCard**](CreditCard.md)|  | 

### Return type

[**CreditCard**](CreditCard.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_assignment**
> save_assignment(buyer_id, credit_card_assignment)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CreditCardApi = OrderCloud.CreditCardApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
credit_card_assignment = OrderCloud.CreditCardAssignment() # CreditCardAssignment | 

try: 
    CreditCardApi.save_assignment(buyer_id, credit_card_assignment)
except ApiException as e:
    print("Exception when calling CreditCardApi->save_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **credit_card_assignment** | [**CreditCardAssignment**](CreditCardAssignment.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

