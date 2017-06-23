# OrderCloud.UserApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buyers_buyer_id_users_get**](UserApi.md#buyers_buyer_id_users_get) | **GET** /buyers/{buyerID}/users | 
[**buyers_buyer_id_users_post**](UserApi.md#buyers_buyer_id_users_post) | **POST** /buyers/{buyerID}/users | 
[**buyers_buyer_id_users_user_id_accesstoken_post**](UserApi.md#buyers_buyer_id_users_user_id_accesstoken_post) | **POST** /buyers/{buyerID}/users/{userID}/accesstoken | 
[**buyers_buyer_id_users_user_id_delete**](UserApi.md#buyers_buyer_id_users_user_id_delete) | **DELETE** /buyers/{buyerID}/users/{userID} | 
[**buyers_buyer_id_users_user_id_get**](UserApi.md#buyers_buyer_id_users_user_id_get) | **GET** /buyers/{buyerID}/users/{userID} | 
[**buyers_buyer_id_users_user_id_patch**](UserApi.md#buyers_buyer_id_users_user_id_patch) | **PATCH** /buyers/{buyerID}/users/{userID} | 
[**buyers_buyer_id_users_user_id_put**](UserApi.md#buyers_buyer_id_users_user_id_put) | **PUT** /buyers/{buyerID}/users/{userID} | 


# **buyers_buyer_id_users_get**
> ListUser buyers_buyer_id_users_get(buyer_id, user_group_id=user_group_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
UserApi = OrderCloud.UserApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
user_group_id = 'user_group_id_example' # str | ID of the user group. (optional)
search = 'search_example' # str | Search of the user. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the user. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the user. (optional)
page = 56 # int | Page of the user. (optional)
page_size = 56 # int | Page size of the user. (optional)

try: 
    response = UserApi.buyers_buyer_id_users_get(buyer_id, user_group_id=user_group_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling UserApi->buyers_buyer_id_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **user_group_id** | **str**| ID of the user group. | [optional] 
 **search** | **str**| Search of the user. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the user. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the user. | [optional] 
 **page** | **int**| Page of the user. | [optional] 
 **page_size** | **int**| Page size of the user. | [optional] 

### Return type

[**ListUser**](ListUser.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_users_post**
> User buyers_buyer_id_users_post(buyer_id, user)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
UserApi = OrderCloud.UserApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
user = OrderCloud.User() # User | 

try: 
    response = UserApi.buyers_buyer_id_users_post(buyer_id, user)
    print(response)
except ApiException as e:
    print("Exception when calling UserApi->buyers_buyer_id_users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **user** | [**User**](User.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_users_user_id_accesstoken_post**
> AccessToken buyers_buyer_id_users_user_id_accesstoken_post(buyer_id, user_id, token_request)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
UserApi = OrderCloud.UserApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
user_id = 'user_id_example' # str | ID of the user.
token_request = OrderCloud.ImpersonateTokenRequest() # ImpersonateTokenRequest | 

try: 
    response = UserApi.buyers_buyer_id_users_user_id_accesstoken_post(buyer_id, user_id, token_request)
    print(response)
except ApiException as e:
    print("Exception when calling UserApi->buyers_buyer_id_users_user_id_accesstoken_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **user_id** | **str**| ID of the user. | 
 **token_request** | [**ImpersonateTokenRequest**](ImpersonateTokenRequest.md)|  | 

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_users_user_id_delete**
> buyers_buyer_id_users_user_id_delete(buyer_id, user_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
UserApi = OrderCloud.UserApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
user_id = 'user_id_example' # str | ID of the user.

try: 
    UserApi.buyers_buyer_id_users_user_id_delete(buyer_id, user_id)
except ApiException as e:
    print("Exception when calling UserApi->buyers_buyer_id_users_user_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **user_id** | **str**| ID of the user. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_users_user_id_get**
> User buyers_buyer_id_users_user_id_get(buyer_id, user_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
UserApi = OrderCloud.UserApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
user_id = 'user_id_example' # str | ID of the user.

try: 
    response = UserApi.buyers_buyer_id_users_user_id_get(buyer_id, user_id)
    print(response)
except ApiException as e:
    print("Exception when calling UserApi->buyers_buyer_id_users_user_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **user_id** | **str**| ID of the user. | 

### Return type

[**User**](User.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_users_user_id_patch**
> User buyers_buyer_id_users_user_id_patch(buyer_id, user_id, user)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
UserApi = OrderCloud.UserApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
user_id = 'user_id_example' # str | ID of the user.
user = OrderCloud.User() # User | 

try: 
    response = UserApi.buyers_buyer_id_users_user_id_patch(buyer_id, user_id, user)
    print(response)
except ApiException as e:
    print("Exception when calling UserApi->buyers_buyer_id_users_user_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **user_id** | **str**| ID of the user. | 
 **user** | [**User**](User.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_users_user_id_put**
> User buyers_buyer_id_users_user_id_put(buyer_id, user_id, user)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
UserApi = OrderCloud.UserApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
user_id = 'user_id_example' # str | ID of the user.
user = OrderCloud.User() # User | 

try: 
    response = UserApi.buyers_buyer_id_users_user_id_put(buyer_id, user_id, user)
    print(response)
except ApiException as e:
    print("Exception when calling UserApi->buyers_buyer_id_users_user_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **user_id** | **str**| ID of the user. | 
 **user** | [**User**](User.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

