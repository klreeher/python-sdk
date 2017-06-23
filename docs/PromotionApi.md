# OrderCloud.PromotionApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**promotions_assignments_get**](PromotionApi.md#promotions_assignments_get) | **GET** /promotions/assignments | 
[**promotions_assignments_post**](PromotionApi.md#promotions_assignments_post) | **POST** /promotions/assignments | 
[**promotions_get**](PromotionApi.md#promotions_get) | **GET** /promotions | 
[**promotions_post**](PromotionApi.md#promotions_post) | **POST** /promotions | 
[**promotions_promotion_id_assignments_delete**](PromotionApi.md#promotions_promotion_id_assignments_delete) | **DELETE** /promotions/{promotionID}/assignments | 
[**promotions_promotion_id_delete**](PromotionApi.md#promotions_promotion_id_delete) | **DELETE** /promotions/{promotionID} | 
[**promotions_promotion_id_get**](PromotionApi.md#promotions_promotion_id_get) | **GET** /promotions/{promotionID} | 
[**promotions_promotion_id_patch**](PromotionApi.md#promotions_promotion_id_patch) | **PATCH** /promotions/{promotionID} | 
[**promotions_promotion_id_put**](PromotionApi.md#promotions_promotion_id_put) | **PUT** /promotions/{promotionID} | 


# **promotions_assignments_get**
> ListPromotionAssignment promotions_assignments_get(buyer_id=buyer_id, promotion_id=promotion_id, user_id=user_id, user_group_id=user_group_id, level=level, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
PromotionApi = OrderCloud.PromotionApi
buyer_id = 'buyer_id_example' # str | ID of the buyer. (optional)
promotion_id = 'promotion_id_example' # str | ID of the promotion. (optional)
user_id = 'user_id_example' # str | ID of the user. (optional)
user_group_id = 'user_group_id_example' # str | ID of the user group. (optional)
level = 'level_example' # str | Level of the promotion. (optional)
page = 56 # int | Page of the promotion. (optional)
page_size = 56 # int | Page size of the promotion. (optional)

try: 
    response = PromotionApi.promotions_assignments_get(buyer_id=buyer_id, promotion_id=promotion_id, user_id=user_id, user_group_id=user_group_id, level=level, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling PromotionApi->promotions_assignments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | [optional] 
 **promotion_id** | **str**| ID of the promotion. | [optional] 
 **user_id** | **str**| ID of the user. | [optional] 
 **user_group_id** | **str**| ID of the user group. | [optional] 
 **level** | **str**| Level of the promotion. | [optional] 
 **page** | **int**| Page of the promotion. | [optional] 
 **page_size** | **int**| Page size of the promotion. | [optional] 

### Return type

[**ListPromotionAssignment**](ListPromotionAssignment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **promotions_assignments_post**
> promotions_assignments_post(assignment)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
PromotionApi = OrderCloud.PromotionApi
assignment = OrderCloud.PromotionAssignment() # PromotionAssignment | 

try: 
    PromotionApi.promotions_assignments_post(assignment)
except ApiException as e:
    print("Exception when calling PromotionApi->promotions_assignments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment** | [**PromotionAssignment**](PromotionAssignment.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **promotions_get**
> ListPromotion promotions_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
PromotionApi = OrderCloud.PromotionApi
search = 'search_example' # str | Search of the promotion. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the promotion. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the promotion. (optional)
page = 56 # int | Page of the promotion. (optional)
page_size = 56 # int | Page size of the promotion. (optional)

try: 
    response = PromotionApi.promotions_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling PromotionApi->promotions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search of the promotion. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the promotion. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the promotion. | [optional] 
 **page** | **int**| Page of the promotion. | [optional] 
 **page_size** | **int**| Page size of the promotion. | [optional] 

### Return type

[**ListPromotion**](ListPromotion.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **promotions_post**
> Promotion promotions_post(promo)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
PromotionApi = OrderCloud.PromotionApi
promo = OrderCloud.Promotion() # Promotion | 

try: 
    response = PromotionApi.promotions_post(promo)
    print(response)
except ApiException as e:
    print("Exception when calling PromotionApi->promotions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **promo** | [**Promotion**](Promotion.md)|  | 

### Return type

[**Promotion**](Promotion.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **promotions_promotion_id_assignments_delete**
> promotions_promotion_id_assignments_delete(promotion_id, buyer_id, user_id=user_id, user_group_id=user_group_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
PromotionApi = OrderCloud.PromotionApi
promotion_id = 'promotion_id_example' # str | ID of the promotion.
buyer_id = 'buyer_id_example' # str | ID of the buyer.
user_id = 'user_id_example' # str | ID of the user. (optional)
user_group_id = 'user_group_id_example' # str | ID of the user group. (optional)

try: 
    PromotionApi.promotions_promotion_id_assignments_delete(promotion_id, buyer_id, user_id=user_id, user_group_id=user_group_id)
except ApiException as e:
    print("Exception when calling PromotionApi->promotions_promotion_id_assignments_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **promotion_id** | **str**| ID of the promotion. | 
 **buyer_id** | **str**| ID of the buyer. | 
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

# **promotions_promotion_id_delete**
> promotions_promotion_id_delete(promotion_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
PromotionApi = OrderCloud.PromotionApi
promotion_id = 'promotion_id_example' # str | ID of the promotion.

try: 
    PromotionApi.promotions_promotion_id_delete(promotion_id)
except ApiException as e:
    print("Exception when calling PromotionApi->promotions_promotion_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **promotion_id** | **str**| ID of the promotion. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **promotions_promotion_id_get**
> Promotion promotions_promotion_id_get(promotion_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
PromotionApi = OrderCloud.PromotionApi
promotion_id = 'promotion_id_example' # str | ID of the promotion.

try: 
    response = PromotionApi.promotions_promotion_id_get(promotion_id)
    print(response)
except ApiException as e:
    print("Exception when calling PromotionApi->promotions_promotion_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **promotion_id** | **str**| ID of the promotion. | 

### Return type

[**Promotion**](Promotion.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **promotions_promotion_id_patch**
> Promotion promotions_promotion_id_patch(promotion_id, partial_promotion)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
PromotionApi = OrderCloud.PromotionApi
promotion_id = 'promotion_id_example' # str | ID of the promotion.
partial_promotion = OrderCloud.Promotion() # Promotion | 

try: 
    response = PromotionApi.promotions_promotion_id_patch(promotion_id, partial_promotion)
    print(response)
except ApiException as e:
    print("Exception when calling PromotionApi->promotions_promotion_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **promotion_id** | **str**| ID of the promotion. | 
 **partial_promotion** | [**Promotion**](Promotion.md)|  | 

### Return type

[**Promotion**](Promotion.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **promotions_promotion_id_put**
> Promotion promotions_promotion_id_put(promotion_id, promo)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
PromotionApi = OrderCloud.PromotionApi
promotion_id = 'promotion_id_example' # str | ID of the promotion.
promo = OrderCloud.Promotion() # Promotion | 

try: 
    response = PromotionApi.promotions_promotion_id_put(promotion_id, promo)
    print(response)
except ApiException as e:
    print("Exception when calling PromotionApi->promotions_promotion_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **promotion_id** | **str**| ID of the promotion. | 
 **promo** | [**Promotion**](Promotion.md)|  | 

### Return type

[**Promotion**](Promotion.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

