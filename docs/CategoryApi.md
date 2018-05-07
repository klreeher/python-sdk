# OrderCloud.CategoryApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](CategoryApi.md#create) | **POST** /catalogs/{catalogID}/categories | 
[**delete**](CategoryApi.md#delete) | **DELETE** /catalogs/{catalogID}/categories/{categoryID} | 
[**delete_assignment**](CategoryApi.md#delete_assignment) | **DELETE** /catalogs/{catalogID}/categories/{categoryID}/assignments | 
[**delete_product_assignment**](CategoryApi.md#delete_product_assignment) | **DELETE** /catalogs/{catalogID}/categories/{categoryID}/productassignments/{productID} | 
[**get**](CategoryApi.md#get) | **GET** /catalogs/{catalogID}/categories/{categoryID} | 
[**list**](CategoryApi.md#list) | **GET** /catalogs/{catalogID}/categories | 
[**list_assignments**](CategoryApi.md#list_assignments) | **GET** /catalogs/{catalogID}/categories/assignments | 
[**list_product_assignments**](CategoryApi.md#list_product_assignments) | **GET** /catalogs/{catalogID}/categories/productassignments | 
[**patch**](CategoryApi.md#patch) | **PATCH** /catalogs/{catalogID}/categories/{categoryID} | 
[**save**](CategoryApi.md#save) | **PUT** /catalogs/{catalogID}/categories/{categoryID} | 
[**save_assignment**](CategoryApi.md#save_assignment) | **POST** /catalogs/{catalogID}/categories/assignments | 
[**save_product_assignment**](CategoryApi.md#save_product_assignment) | **POST** /catalogs/{catalogID}/categories/productassignments | 


# **create**
> Category create(catalog_id, category)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CategoryApi = OrderCloud.CategoryApi
catalog_id = 'catalog_id_example' # str | ID of the catalog.
category = OrderCloud.Category() # Category | 

try: 
    response = CategoryApi.create(catalog_id, category)
    print(response)
except ApiException as e:
    print("Exception when calling CategoryApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | 
 **category** | [**Category**](Category.md)|  | 

### Return type

[**Category**](Category.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(catalog_id, category_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CategoryApi = OrderCloud.CategoryApi
catalog_id = 'catalog_id_example' # str | ID of the catalog.
category_id = 'category_id_example' # str | ID of the category.

try: 
    CategoryApi.delete(catalog_id, category_id)
except ApiException as e:
    print("Exception when calling CategoryApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | 
 **category_id** | **str**| ID of the category. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_assignment**
> delete_assignment(catalog_id, category_id, buyer_id, user_id=user_id, user_group_id=user_group_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CategoryApi = OrderCloud.CategoryApi
catalog_id = 'catalog_id_example' # str | ID of the catalog.
category_id = 'category_id_example' # str | ID of the category.
buyer_id = 'buyer_id_example' # str | ID of the buyer.
user_id = 'user_id_example' # str | ID of the user. (optional)
user_group_id = 'user_group_id_example' # str | ID of the user group. (optional)

try: 
    CategoryApi.delete_assignment(catalog_id, category_id, buyer_id, user_id=user_id, user_group_id=user_group_id)
except ApiException as e:
    print("Exception when calling CategoryApi->delete_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | 
 **category_id** | **str**| ID of the category. | 
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

# **delete_product_assignment**
> delete_product_assignment(catalog_id, category_id, product_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CategoryApi = OrderCloud.CategoryApi
catalog_id = 'catalog_id_example' # str | ID of the catalog.
category_id = 'category_id_example' # str | ID of the category.
product_id = 'product_id_example' # str | ID of the product.

try: 
    CategoryApi.delete_product_assignment(catalog_id, category_id, product_id)
except ApiException as e:
    print("Exception when calling CategoryApi->delete_product_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | 
 **category_id** | **str**| ID of the category. | 
 **product_id** | **str**| ID of the product. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Category get(catalog_id, category_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CategoryApi = OrderCloud.CategoryApi
catalog_id = 'catalog_id_example' # str | ID of the catalog.
category_id = 'category_id_example' # str | ID of the category.

try: 
    response = CategoryApi.get(catalog_id, category_id)
    print(response)
except ApiException as e:
    print("Exception when calling CategoryApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | 
 **category_id** | **str**| ID of the category. | 

### Return type

[**Category**](Category.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ListCategory list(catalog_id, depth=depth, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CategoryApi = OrderCloud.CategoryApi
catalog_id = 'catalog_id_example' # str | ID of the catalog.
depth = 'depth_example' # str | Depth of the category. (optional)
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = CategoryApi.list(catalog_id, depth=depth, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling CategoryApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | 
 **depth** | **str**| Depth of the category. | [optional] 
 **search** | **str**| Word or phrase to search for. | [optional] 
 **search_on** | **str**| Comma-delimited list of fields to search on. | [optional] 
 **sort_by** | **str**| Comma-delimited list of fields to sort by. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 
 **filters** | [**dict(str, str)**](str.md)| Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or &#39;xp.???&#39; | [optional] 

### Return type

[**ListCategory**](ListCategory.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assignments**
> ListCategoryAssignment list_assignments(catalog_id, category_id=category_id, buyer_id=buyer_id, user_id=user_id, user_group_id=user_group_id, level=level, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CategoryApi = OrderCloud.CategoryApi
catalog_id = 'catalog_id_example' # str | ID of the catalog.
category_id = 'category_id_example' # str | ID of the category. (optional)
buyer_id = 'buyer_id_example' # str | ID of the buyer. (optional)
user_id = 'user_id_example' # str | ID of the user. (optional)
user_group_id = 'user_group_id_example' # str | ID of the user group. (optional)
level = 'level_example' # str | Level of the category assignment. Possible values: User, Group, Company. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)

try: 
    response = CategoryApi.list_assignments(catalog_id, category_id=category_id, buyer_id=buyer_id, user_id=user_id, user_group_id=user_group_id, level=level, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling CategoryApi->list_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | 
 **category_id** | **str**| ID of the category. | [optional] 
 **buyer_id** | **str**| ID of the buyer. | [optional] 
 **user_id** | **str**| ID of the user. | [optional] 
 **user_group_id** | **str**| ID of the user group. | [optional] 
 **level** | **str**| Level of the category assignment. Possible values: User, Group, Company. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 

### Return type

[**ListCategoryAssignment**](ListCategoryAssignment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_product_assignments**
> ListCategoryProductAssignment list_product_assignments(catalog_id, category_id=category_id, product_id=product_id, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CategoryApi = OrderCloud.CategoryApi
catalog_id = 'catalog_id_example' # str | ID of the catalog.
category_id = 'category_id_example' # str | ID of the category. (optional)
product_id = 'product_id_example' # str | ID of the product. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)

try: 
    response = CategoryApi.list_product_assignments(catalog_id, category_id=category_id, product_id=product_id, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling CategoryApi->list_product_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | 
 **category_id** | **str**| ID of the category. | [optional] 
 **product_id** | **str**| ID of the product. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 

### Return type

[**ListCategoryProductAssignment**](ListCategoryProductAssignment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch**
> Category patch(catalog_id, category_id, partial_category)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CategoryApi = OrderCloud.CategoryApi
catalog_id = 'catalog_id_example' # str | ID of the catalog.
category_id = 'category_id_example' # str | ID of the category.
partial_category = OrderCloud.Category() # Category | 

try: 
    response = CategoryApi.patch(catalog_id, category_id, partial_category)
    print(response)
except ApiException as e:
    print("Exception when calling CategoryApi->patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | 
 **category_id** | **str**| ID of the category. | 
 **partial_category** | [**Category**](Category.md)|  | 

### Return type

[**Category**](Category.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save**
> Category save(catalog_id, category_id, category)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CategoryApi = OrderCloud.CategoryApi
catalog_id = 'catalog_id_example' # str | ID of the catalog.
category_id = 'category_id_example' # str | ID of the category.
category = OrderCloud.Category() # Category | 

try: 
    response = CategoryApi.save(catalog_id, category_id, category)
    print(response)
except ApiException as e:
    print("Exception when calling CategoryApi->save: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | 
 **category_id** | **str**| ID of the category. | 
 **category** | [**Category**](Category.md)|  | 

### Return type

[**Category**](Category.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_assignment**
> save_assignment(catalog_id, category_assignment)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CategoryApi = OrderCloud.CategoryApi
catalog_id = 'catalog_id_example' # str | ID of the catalog.
category_assignment = OrderCloud.CategoryAssignment() # CategoryAssignment | 

try: 
    CategoryApi.save_assignment(catalog_id, category_assignment)
except ApiException as e:
    print("Exception when calling CategoryApi->save_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | 
 **category_assignment** | [**CategoryAssignment**](CategoryAssignment.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_product_assignment**
> save_product_assignment(catalog_id, category_product_assignment)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CategoryApi = OrderCloud.CategoryApi
catalog_id = 'catalog_id_example' # str | ID of the catalog.
category_product_assignment = OrderCloud.CategoryProductAssignment() # CategoryProductAssignment | 

try: 
    CategoryApi.save_product_assignment(catalog_id, category_product_assignment)
except ApiException as e:
    print("Exception when calling CategoryApi->save_product_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | 
 **category_product_assignment** | [**CategoryProductAssignment**](CategoryProductAssignment.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

