# OrderCloud.CostCenterApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](CostCenterApi.md#create) | **POST** /buyers/{buyerID}/costcenters | 
[**delete**](CostCenterApi.md#delete) | **DELETE** /buyers/{buyerID}/costcenters/{costCenterID} | 
[**delete_assignment**](CostCenterApi.md#delete_assignment) | **DELETE** /buyers/{buyerID}/costcenters/{costCenterID}/assignments | 
[**get**](CostCenterApi.md#get) | **GET** /buyers/{buyerID}/costcenters/{costCenterID} | 
[**list**](CostCenterApi.md#list) | **GET** /buyers/{buyerID}/costcenters | 
[**list_assignments**](CostCenterApi.md#list_assignments) | **GET** /buyers/{buyerID}/costcenters/assignments | 
[**patch**](CostCenterApi.md#patch) | **PATCH** /buyers/{buyerID}/costcenters/{costCenterID} | 
[**save_assignment**](CostCenterApi.md#save_assignment) | **POST** /buyers/{buyerID}/costcenters/assignments | 
[**update**](CostCenterApi.md#update) | **PUT** /buyers/{buyerID}/costcenters/{costCenterID} | 


# **create**
> CostCenter create(buyer_id, cost_center)



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
    response = CostCenterApi.create(buyer_id, cost_center)
    print(response)
except ApiException as e:
    print("Exception when calling CostCenterApi->create: %s\n" % e)
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

# **delete**
> delete(buyer_id, cost_center_id)



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
    CostCenterApi.delete(buyer_id, cost_center_id)
except ApiException as e:
    print("Exception when calling CostCenterApi->delete: %s\n" % e)
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

# **delete_assignment**
> delete_assignment(buyer_id, cost_center_id, user_id=user_id, user_group_id=user_group_id)



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
    CostCenterApi.delete_assignment(buyer_id, cost_center_id, user_id=user_id, user_group_id=user_group_id)
except ApiException as e:
    print("Exception when calling CostCenterApi->delete_assignment: %s\n" % e)
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

# **get**
> CostCenter get(buyer_id, cost_center_id)



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
    response = CostCenterApi.get(buyer_id, cost_center_id)
    print(response)
except ApiException as e:
    print("Exception when calling CostCenterApi->get: %s\n" % e)
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

# **list**
> ListCostCenter list(buyer_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CostCenterApi = OrderCloud.CostCenterApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = CostCenterApi.list(buyer_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling CostCenterApi->list: %s\n" % e)
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

[**ListCostCenter**](ListCostCenter.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assignments**
> ListCostCenterAssignment list_assignments(buyer_id, cost_center_id=cost_center_id, user_id=user_id, user_group_id=user_group_id, level=level, page=page, page_size=page_size)



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
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)

try: 
    response = CostCenterApi.list_assignments(buyer_id, cost_center_id=cost_center_id, user_id=user_id, user_group_id=user_group_id, level=level, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling CostCenterApi->list_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **cost_center_id** | **str**| ID of the cost center. | [optional] 
 **user_id** | **str**| ID of the user. | [optional] 
 **user_group_id** | **str**| ID of the user group. | [optional] 
 **level** | **str**| Level of the cost center. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 

### Return type

[**ListCostCenterAssignment**](ListCostCenterAssignment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch**
> CostCenter patch(buyer_id, cost_center_id, cost_center)



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
    response = CostCenterApi.patch(buyer_id, cost_center_id, cost_center)
    print(response)
except ApiException as e:
    print("Exception when calling CostCenterApi->patch: %s\n" % e)
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

# **save_assignment**
> save_assignment(buyer_id, assignment)



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
    CostCenterApi.save_assignment(buyer_id, assignment)
except ApiException as e:
    print("Exception when calling CostCenterApi->save_assignment: %s\n" % e)
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

# **update**
> CostCenter update(buyer_id, cost_center_id, cost_center)



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
    response = CostCenterApi.update(buyer_id, cost_center_id, cost_center)
    print(response)
except ApiException as e:
    print("Exception when calling CostCenterApi->update: %s\n" % e)
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

