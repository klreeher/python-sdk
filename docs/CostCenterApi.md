# OrderCloud.CostCenterApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buyers_buyer_id_costcenters_assignments_get**](CostCenterApi.md#buyers_buyer_id_costcenters_assignments_get) | **GET** /buyers/{buyerID}/costcenters/assignments | 
[**buyers_buyer_id_costcenters_assignments_post**](CostCenterApi.md#buyers_buyer_id_costcenters_assignments_post) | **POST** /buyers/{buyerID}/costcenters/assignments | 
[**buyers_buyer_id_costcenters_cost_center_id_assignments_delete**](CostCenterApi.md#buyers_buyer_id_costcenters_cost_center_id_assignments_delete) | **DELETE** /buyers/{buyerID}/costcenters/{costCenterID}/assignments | 
[**buyers_buyer_id_costcenters_cost_center_id_delete**](CostCenterApi.md#buyers_buyer_id_costcenters_cost_center_id_delete) | **DELETE** /buyers/{buyerID}/costcenters/{costCenterID} | 
[**buyers_buyer_id_costcenters_cost_center_id_get**](CostCenterApi.md#buyers_buyer_id_costcenters_cost_center_id_get) | **GET** /buyers/{buyerID}/costcenters/{costCenterID} | 
[**buyers_buyer_id_costcenters_cost_center_id_patch**](CostCenterApi.md#buyers_buyer_id_costcenters_cost_center_id_patch) | **PATCH** /buyers/{buyerID}/costcenters/{costCenterID} | 
[**buyers_buyer_id_costcenters_cost_center_id_put**](CostCenterApi.md#buyers_buyer_id_costcenters_cost_center_id_put) | **PUT** /buyers/{buyerID}/costcenters/{costCenterID} | 
[**buyers_buyer_id_costcenters_get**](CostCenterApi.md#buyers_buyer_id_costcenters_get) | **GET** /buyers/{buyerID}/costcenters | 
[**buyers_buyer_id_costcenters_post**](CostCenterApi.md#buyers_buyer_id_costcenters_post) | **POST** /buyers/{buyerID}/costcenters | 


# **buyers_buyer_id_costcenters_assignments_get**
> ListCostCenterAssignment buyers_buyer_id_costcenters_assignments_get(buyer_id, cost_center_id=cost_center_id, user_id=user_id, user_group_id=user_group_id, level=level, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CostCenterApi = OrderCloud.CostCenterApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
cost_center_id = 'cost_center_id_example' # str | ID of the cost center. (optional)
user_id = 'user_id_example' # str | ID of the user. (optional)
user_group_id = 'user_group_id_example' # str | ID of the user group. (optional)
level = 'level_example' # str | Level of the cost center. (optional)
page = 56 # int | Page of the cost center. (optional)
page_size = 56 # int | Page size of the cost center. (optional)

try: 
    response = CostCenterApi.buyers_buyer_id_costcenters_assignments_get(buyer_id, cost_center_id=cost_center_id, user_id=user_id, user_group_id=user_group_id, level=level, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling CostCenterApi->buyers_buyer_id_costcenters_assignments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **cost_center_id** | **str**| ID of the cost center. | [optional] 
 **user_id** | **str**| ID of the user. | [optional] 
 **user_group_id** | **str**| ID of the user group. | [optional] 
 **level** | **str**| Level of the cost center. | [optional] 
 **page** | **int**| Page of the cost center. | [optional] 
 **page_size** | **int**| Page size of the cost center. | [optional] 

### Return type

[**ListCostCenterAssignment**](ListCostCenterAssignment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_costcenters_assignments_post**
> buyers_buyer_id_costcenters_assignments_post(buyer_id, assignment)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CostCenterApi = OrderCloud.CostCenterApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
assignment = OrderCloud.CostCenterAssignment() # CostCenterAssignment | 

try: 
    CostCenterApi.buyers_buyer_id_costcenters_assignments_post(buyer_id, assignment)
except ApiException as e:
    print("Exception when calling CostCenterApi->buyers_buyer_id_costcenters_assignments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **assignment** | [**CostCenterAssignment**](CostCenterAssignment.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_costcenters_cost_center_id_assignments_delete**
> buyers_buyer_id_costcenters_cost_center_id_assignments_delete(buyer_id, cost_center_id, user_id=user_id, user_group_id=user_group_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CostCenterApi = OrderCloud.CostCenterApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
cost_center_id = 'cost_center_id_example' # str | ID of the cost center.
user_id = 'user_id_example' # str | ID of the user. (optional)
user_group_id = 'user_group_id_example' # str | ID of the user group. (optional)

try: 
    CostCenterApi.buyers_buyer_id_costcenters_cost_center_id_assignments_delete(buyer_id, cost_center_id, user_id=user_id, user_group_id=user_group_id)
except ApiException as e:
    print("Exception when calling CostCenterApi->buyers_buyer_id_costcenters_cost_center_id_assignments_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **cost_center_id** | **str**| ID of the cost center. | 
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

# **buyers_buyer_id_costcenters_cost_center_id_delete**
> buyers_buyer_id_costcenters_cost_center_id_delete(buyer_id, cost_center_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CostCenterApi = OrderCloud.CostCenterApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
cost_center_id = 'cost_center_id_example' # str | ID of the cost center.

try: 
    CostCenterApi.buyers_buyer_id_costcenters_cost_center_id_delete(buyer_id, cost_center_id)
except ApiException as e:
    print("Exception when calling CostCenterApi->buyers_buyer_id_costcenters_cost_center_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **cost_center_id** | **str**| ID of the cost center. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_costcenters_cost_center_id_get**
> CostCenter buyers_buyer_id_costcenters_cost_center_id_get(buyer_id, cost_center_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CostCenterApi = OrderCloud.CostCenterApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
cost_center_id = 'cost_center_id_example' # str | ID of the cost center.

try: 
    response = CostCenterApi.buyers_buyer_id_costcenters_cost_center_id_get(buyer_id, cost_center_id)
    print(response)
except ApiException as e:
    print("Exception when calling CostCenterApi->buyers_buyer_id_costcenters_cost_center_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **cost_center_id** | **str**| ID of the cost center. | 

### Return type

[**CostCenter**](CostCenter.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_costcenters_cost_center_id_patch**
> CostCenter buyers_buyer_id_costcenters_cost_center_id_patch(buyer_id, cost_center_id, cost_center)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CostCenterApi = OrderCloud.CostCenterApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
cost_center_id = 'cost_center_id_example' # str | ID of the cost center.
cost_center = OrderCloud.CostCenter() # CostCenter | 

try: 
    response = CostCenterApi.buyers_buyer_id_costcenters_cost_center_id_patch(buyer_id, cost_center_id, cost_center)
    print(response)
except ApiException as e:
    print("Exception when calling CostCenterApi->buyers_buyer_id_costcenters_cost_center_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **cost_center_id** | **str**| ID of the cost center. | 
 **cost_center** | [**CostCenter**](CostCenter.md)|  | 

### Return type

[**CostCenter**](CostCenter.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_costcenters_cost_center_id_put**
> CostCenter buyers_buyer_id_costcenters_cost_center_id_put(buyer_id, cost_center_id, cost_center)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CostCenterApi = OrderCloud.CostCenterApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
cost_center_id = 'cost_center_id_example' # str | ID of the cost center.
cost_center = OrderCloud.CostCenter() # CostCenter | 

try: 
    response = CostCenterApi.buyers_buyer_id_costcenters_cost_center_id_put(buyer_id, cost_center_id, cost_center)
    print(response)
except ApiException as e:
    print("Exception when calling CostCenterApi->buyers_buyer_id_costcenters_cost_center_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **cost_center_id** | **str**| ID of the cost center. | 
 **cost_center** | [**CostCenter**](CostCenter.md)|  | 

### Return type

[**CostCenter**](CostCenter.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_costcenters_get**
> ListCostCenter buyers_buyer_id_costcenters_get(buyer_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CostCenterApi = OrderCloud.CostCenterApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
search = 'search_example' # str | Search of the cost center. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the cost center. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the cost center. (optional)
page = 56 # int | Page of the cost center. (optional)
page_size = 56 # int | Page size of the cost center. (optional)

try: 
    response = CostCenterApi.buyers_buyer_id_costcenters_get(buyer_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling CostCenterApi->buyers_buyer_id_costcenters_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **search** | **str**| Search of the cost center. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the cost center. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the cost center. | [optional] 
 **page** | **int**| Page of the cost center. | [optional] 
 **page_size** | **int**| Page size of the cost center. | [optional] 

### Return type

[**ListCostCenter**](ListCostCenter.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_costcenters_post**
> CostCenter buyers_buyer_id_costcenters_post(buyer_id, cost_center)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CostCenterApi = OrderCloud.CostCenterApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
cost_center = OrderCloud.CostCenter() # CostCenter | 

try: 
    response = CostCenterApi.buyers_buyer_id_costcenters_post(buyer_id, cost_center)
    print(response)
except ApiException as e:
    print("Exception when calling CostCenterApi->buyers_buyer_id_costcenters_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **cost_center** | [**CostCenter**](CostCenter.md)|  | 

### Return type

[**CostCenter**](CostCenter.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

