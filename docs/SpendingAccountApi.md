# OrderCloud.SpendingAccountApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buyers_buyer_id_spendingaccounts_assignments_get**](SpendingAccountApi.md#buyers_buyer_id_spendingaccounts_assignments_get) | **GET** /buyers/{buyerID}/spendingaccounts/assignments | 
[**buyers_buyer_id_spendingaccounts_assignments_post**](SpendingAccountApi.md#buyers_buyer_id_spendingaccounts_assignments_post) | **POST** /buyers/{buyerID}/spendingaccounts/assignments | 
[**buyers_buyer_id_spendingaccounts_get**](SpendingAccountApi.md#buyers_buyer_id_spendingaccounts_get) | **GET** /buyers/{buyerID}/spendingaccounts | 
[**buyers_buyer_id_spendingaccounts_post**](SpendingAccountApi.md#buyers_buyer_id_spendingaccounts_post) | **POST** /buyers/{buyerID}/spendingaccounts | 
[**buyers_buyer_id_spendingaccounts_spending_account_id_assignments_delete**](SpendingAccountApi.md#buyers_buyer_id_spendingaccounts_spending_account_id_assignments_delete) | **DELETE** /buyers/{buyerID}/spendingaccounts/{spendingAccountID}/assignments | 
[**buyers_buyer_id_spendingaccounts_spending_account_id_delete**](SpendingAccountApi.md#buyers_buyer_id_spendingaccounts_spending_account_id_delete) | **DELETE** /buyers/{buyerID}/spendingaccounts/{spendingAccountID} | 
[**buyers_buyer_id_spendingaccounts_spending_account_id_get**](SpendingAccountApi.md#buyers_buyer_id_spendingaccounts_spending_account_id_get) | **GET** /buyers/{buyerID}/spendingaccounts/{spendingAccountID} | 
[**buyers_buyer_id_spendingaccounts_spending_account_id_patch**](SpendingAccountApi.md#buyers_buyer_id_spendingaccounts_spending_account_id_patch) | **PATCH** /buyers/{buyerID}/spendingaccounts/{spendingAccountID} | 
[**buyers_buyer_id_spendingaccounts_spending_account_id_put**](SpendingAccountApi.md#buyers_buyer_id_spendingaccounts_spending_account_id_put) | **PUT** /buyers/{buyerID}/spendingaccounts/{spendingAccountID} | 


# **buyers_buyer_id_spendingaccounts_assignments_get**
> ListSpendingAccountAssignment buyers_buyer_id_spendingaccounts_assignments_get(buyer_id, spending_account_id=spending_account_id, user_id=user_id, user_group_id=user_group_id, level=level, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SpendingAccountApi = OrderCloud.SpendingAccountApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
spending_account_id = 'spending_account_id_example' # str | ID of the spending account. (optional)
user_id = 'user_id_example' # str | ID of the user. (optional)
user_group_id = 'user_group_id_example' # str | ID of the user group. (optional)
level = 'level_example' # str | Level of the spending account. (optional)
page = 56 # int | Page of the spending account. (optional)
page_size = 56 # int | Page size of the spending account. (optional)

try: 
    response = SpendingAccountApi.buyers_buyer_id_spendingaccounts_assignments_get(buyer_id, spending_account_id=spending_account_id, user_id=user_id, user_group_id=user_group_id, level=level, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling SpendingAccountApi->buyers_buyer_id_spendingaccounts_assignments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **spending_account_id** | **str**| ID of the spending account. | [optional] 
 **user_id** | **str**| ID of the user. | [optional] 
 **user_group_id** | **str**| ID of the user group. | [optional] 
 **level** | **str**| Level of the spending account. | [optional] 
 **page** | **int**| Page of the spending account. | [optional] 
 **page_size** | **int**| Page size of the spending account. | [optional] 

### Return type

[**ListSpendingAccountAssignment**](ListSpendingAccountAssignment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_spendingaccounts_assignments_post**
> buyers_buyer_id_spendingaccounts_assignments_post(buyer_id, assignment)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SpendingAccountApi = OrderCloud.SpendingAccountApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
assignment = OrderCloud.SpendingAccountAssignment() # SpendingAccountAssignment | 

try: 
    SpendingAccountApi.buyers_buyer_id_spendingaccounts_assignments_post(buyer_id, assignment)
except ApiException as e:
    print("Exception when calling SpendingAccountApi->buyers_buyer_id_spendingaccounts_assignments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **assignment** | [**SpendingAccountAssignment**](SpendingAccountAssignment.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_spendingaccounts_get**
> ListSpendingAccount buyers_buyer_id_spendingaccounts_get(buyer_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SpendingAccountApi = OrderCloud.SpendingAccountApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
search = 'search_example' # str | Search of the spending account. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the spending account. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the spending account. (optional)
page = 56 # int | Page of the spending account. (optional)
page_size = 56 # int | Page size of the spending account. (optional)

try: 
    response = SpendingAccountApi.buyers_buyer_id_spendingaccounts_get(buyer_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling SpendingAccountApi->buyers_buyer_id_spendingaccounts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **search** | **str**| Search of the spending account. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the spending account. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the spending account. | [optional] 
 **page** | **int**| Page of the spending account. | [optional] 
 **page_size** | **int**| Page size of the spending account. | [optional] 

### Return type

[**ListSpendingAccount**](ListSpendingAccount.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_spendingaccounts_post**
> SpendingAccount buyers_buyer_id_spendingaccounts_post(buyer_id, spending_account)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SpendingAccountApi = OrderCloud.SpendingAccountApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
spending_account = OrderCloud.SpendingAccount() # SpendingAccount | 

try: 
    response = SpendingAccountApi.buyers_buyer_id_spendingaccounts_post(buyer_id, spending_account)
    print(response)
except ApiException as e:
    print("Exception when calling SpendingAccountApi->buyers_buyer_id_spendingaccounts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **spending_account** | [**SpendingAccount**](SpendingAccount.md)|  | 

### Return type

[**SpendingAccount**](SpendingAccount.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_spendingaccounts_spending_account_id_assignments_delete**
> buyers_buyer_id_spendingaccounts_spending_account_id_assignments_delete(buyer_id, spending_account_id, user_id=user_id, user_group_id=user_group_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SpendingAccountApi = OrderCloud.SpendingAccountApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
spending_account_id = 'spending_account_id_example' # str | ID of the spending account.
user_id = 'user_id_example' # str | ID of the user. (optional)
user_group_id = 'user_group_id_example' # str | ID of the user group. (optional)

try: 
    SpendingAccountApi.buyers_buyer_id_spendingaccounts_spending_account_id_assignments_delete(buyer_id, spending_account_id, user_id=user_id, user_group_id=user_group_id)
except ApiException as e:
    print("Exception when calling SpendingAccountApi->buyers_buyer_id_spendingaccounts_spending_account_id_assignments_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **spending_account_id** | **str**| ID of the spending account. | 
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

# **buyers_buyer_id_spendingaccounts_spending_account_id_delete**
> buyers_buyer_id_spendingaccounts_spending_account_id_delete(buyer_id, spending_account_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SpendingAccountApi = OrderCloud.SpendingAccountApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
spending_account_id = 'spending_account_id_example' # str | ID of the spending account.

try: 
    SpendingAccountApi.buyers_buyer_id_spendingaccounts_spending_account_id_delete(buyer_id, spending_account_id)
except ApiException as e:
    print("Exception when calling SpendingAccountApi->buyers_buyer_id_spendingaccounts_spending_account_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **spending_account_id** | **str**| ID of the spending account. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_spendingaccounts_spending_account_id_get**
> SpendingAccount buyers_buyer_id_spendingaccounts_spending_account_id_get(buyer_id, spending_account_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SpendingAccountApi = OrderCloud.SpendingAccountApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
spending_account_id = 'spending_account_id_example' # str | ID of the spending account.

try: 
    response = SpendingAccountApi.buyers_buyer_id_spendingaccounts_spending_account_id_get(buyer_id, spending_account_id)
    print(response)
except ApiException as e:
    print("Exception when calling SpendingAccountApi->buyers_buyer_id_spendingaccounts_spending_account_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **spending_account_id** | **str**| ID of the spending account. | 

### Return type

[**SpendingAccount**](SpendingAccount.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_spendingaccounts_spending_account_id_patch**
> SpendingAccount buyers_buyer_id_spendingaccounts_spending_account_id_patch(buyer_id, spending_account_id, spending_account)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SpendingAccountApi = OrderCloud.SpendingAccountApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
spending_account_id = 'spending_account_id_example' # str | ID of the spending account.
spending_account = OrderCloud.SpendingAccount() # SpendingAccount | 

try: 
    response = SpendingAccountApi.buyers_buyer_id_spendingaccounts_spending_account_id_patch(buyer_id, spending_account_id, spending_account)
    print(response)
except ApiException as e:
    print("Exception when calling SpendingAccountApi->buyers_buyer_id_spendingaccounts_spending_account_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **spending_account_id** | **str**| ID of the spending account. | 
 **spending_account** | [**SpendingAccount**](SpendingAccount.md)|  | 

### Return type

[**SpendingAccount**](SpendingAccount.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_spendingaccounts_spending_account_id_put**
> SpendingAccount buyers_buyer_id_spendingaccounts_spending_account_id_put(buyer_id, spending_account_id, spending_account)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SpendingAccountApi = OrderCloud.SpendingAccountApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
spending_account_id = 'spending_account_id_example' # str | ID of the spending account.
spending_account = OrderCloud.SpendingAccount() # SpendingAccount | 

try: 
    response = SpendingAccountApi.buyers_buyer_id_spendingaccounts_spending_account_id_put(buyer_id, spending_account_id, spending_account)
    print(response)
except ApiException as e:
    print("Exception when calling SpendingAccountApi->buyers_buyer_id_spendingaccounts_spending_account_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **spending_account_id** | **str**| ID of the spending account. | 
 **spending_account** | [**SpendingAccount**](SpendingAccount.md)|  | 

### Return type

[**SpendingAccount**](SpendingAccount.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

