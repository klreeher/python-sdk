# OrderCloud.BuyerApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buyers_buyer_id_delete**](BuyerApi.md#buyers_buyer_id_delete) | **DELETE** /buyers/{buyerID} | 
[**buyers_buyer_id_get**](BuyerApi.md#buyers_buyer_id_get) | **GET** /buyers/{buyerID} | 
[**buyers_buyer_id_patch**](BuyerApi.md#buyers_buyer_id_patch) | **PATCH** /buyers/{buyerID} | 
[**buyers_buyer_id_put**](BuyerApi.md#buyers_buyer_id_put) | **PUT** /buyers/{buyerID} | 
[**buyers_get**](BuyerApi.md#buyers_get) | **GET** /buyers | 
[**buyers_post**](BuyerApi.md#buyers_post) | **POST** /buyers | 


# **buyers_buyer_id_delete**
> buyers_buyer_id_delete(buyer_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
BuyerApi = OrderCloud.BuyerApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.

try: 
    BuyerApi.buyers_buyer_id_delete(buyer_id)
except ApiException as e:
    print("Exception when calling BuyerApi->buyers_buyer_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_get**
> Buyer buyers_buyer_id_get(buyer_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
BuyerApi = OrderCloud.BuyerApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.

try: 
    response = BuyerApi.buyers_buyer_id_get(buyer_id)
    print(response)
except ApiException as e:
    print("Exception when calling BuyerApi->buyers_buyer_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 

### Return type

[**Buyer**](Buyer.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_patch**
> Buyer buyers_buyer_id_patch(buyer_id, company)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
BuyerApi = OrderCloud.BuyerApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
company = OrderCloud.Buyer() # Buyer | 

try: 
    response = BuyerApi.buyers_buyer_id_patch(buyer_id, company)
    print(response)
except ApiException as e:
    print("Exception when calling BuyerApi->buyers_buyer_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **company** | [**Buyer**](Buyer.md)|  | 

### Return type

[**Buyer**](Buyer.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_put**
> Buyer buyers_buyer_id_put(buyer_id, company)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
BuyerApi = OrderCloud.BuyerApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
company = OrderCloud.Buyer() # Buyer | 

try: 
    response = BuyerApi.buyers_buyer_id_put(buyer_id, company)
    print(response)
except ApiException as e:
    print("Exception when calling BuyerApi->buyers_buyer_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **company** | [**Buyer**](Buyer.md)|  | 

### Return type

[**Buyer**](Buyer.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_get**
> ListBuyer buyers_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
BuyerApi = OrderCloud.BuyerApi
search = 'search_example' # str | Search of the buyer. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the buyer. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the buyer. (optional)
page = 56 # int | Page of the buyer. (optional)
page_size = 56 # int | Page size of the buyer. (optional)

try: 
    response = BuyerApi.buyers_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling BuyerApi->buyers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search of the buyer. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the buyer. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the buyer. | [optional] 
 **page** | **int**| Page of the buyer. | [optional] 
 **page_size** | **int**| Page size of the buyer. | [optional] 

### Return type

[**ListBuyer**](ListBuyer.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_post**
> Buyer buyers_post(company)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
BuyerApi = OrderCloud.BuyerApi
company = OrderCloud.Buyer() # Buyer | 

try: 
    response = BuyerApi.buyers_post(company)
    print(response)
except ApiException as e:
    print("Exception when calling BuyerApi->buyers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company** | [**Buyer**](Buyer.md)|  | 

### Return type

[**Buyer**](Buyer.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

