# OrderCloud.CategoryApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogs_catalog_id_categories_assignments_get**](CategoryApi.md#catalogs_catalog_id_categories_assignments_get) | **GET** /catalogs/{catalogID}/categories/assignments | 
[**catalogs_catalog_id_categories_assignments_post**](CategoryApi.md#catalogs_catalog_id_categories_assignments_post) | **POST** /catalogs/{catalogID}/categories/assignments | 
[**catalogs_catalog_id_categories_category_id_assignments_delete**](CategoryApi.md#catalogs_catalog_id_categories_category_id_assignments_delete) | **DELETE** /catalogs/{catalogID}/categories/{categoryID}/assignments | 
[**catalogs_catalog_id_categories_category_id_delete**](CategoryApi.md#catalogs_catalog_id_categories_category_id_delete) | **DELETE** /catalogs/{catalogID}/categories/{categoryID} | 
[**catalogs_catalog_id_categories_category_id_get**](CategoryApi.md#catalogs_catalog_id_categories_category_id_get) | **GET** /catalogs/{catalogID}/categories/{categoryID} | 
[**catalogs_catalog_id_categories_category_id_patch**](CategoryApi.md#catalogs_catalog_id_categories_category_id_patch) | **PATCH** /catalogs/{catalogID}/categories/{categoryID} | 
[**catalogs_catalog_id_categories_category_id_productassignments_product_id_delete**](CategoryApi.md#catalogs_catalog_id_categories_category_id_productassignments_product_id_delete) | **DELETE** /catalogs/{catalogID}/categories/{categoryID}/productassignments/{productID} | 
[**catalogs_catalog_id_categories_category_id_put**](CategoryApi.md#catalogs_catalog_id_categories_category_id_put) | **PUT** /catalogs/{catalogID}/categories/{categoryID} | 
[**catalogs_catalog_id_categories_get**](CategoryApi.md#catalogs_catalog_id_categories_get) | **GET** /catalogs/{catalogID}/categories | 
[**catalogs_catalog_id_categories_post**](CategoryApi.md#catalogs_catalog_id_categories_post) | **POST** /catalogs/{catalogID}/categories | 
[**catalogs_catalog_id_categories_productassignments_get**](CategoryApi.md#catalogs_catalog_id_categories_productassignments_get) | **GET** /catalogs/{catalogID}/categories/productassignments | 
[**catalogs_catalog_id_categories_productassignments_post**](CategoryApi.md#catalogs_catalog_id_categories_productassignments_post) | **POST** /catalogs/{catalogID}/categories/productassignments | 


# **catalogs_catalog_id_categories_assignments_get**
> ListCategoryAssignment catalogs_catalog_id_categories_assignments_get(catalog_id, category_id=category_id, buyer_id=buyer_id, user_id=user_id, user_group_id=user_group_id, level=level, page=page, page_size=page_size)



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
level = 'level_example' # str | Level of the category. (optional)
page = 56 # int | Page of the category. (optional)
page_size = 56 # int | Page size of the category. (optional)

try: 
    response = CategoryApi.catalogs_catalog_id_categories_assignments_get(catalog_id, category_id=category_id, buyer_id=buyer_id, user_id=user_id, user_group_id=user_group_id, level=level, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling CategoryApi->catalogs_catalog_id_categories_assignments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | 
 **category_id** | **str**| ID of the category. | [optional] 
 **buyer_id** | **str**| ID of the buyer. | [optional] 
 **user_id** | **str**| ID of the user. | [optional] 
 **user_group_id** | **str**| ID of the user group. | [optional] 
 **level** | **str**| Level of the category. | [optional] 
 **page** | **int**| Page of the category. | [optional] 
 **page_size** | **int**| Page size of the category. | [optional] 

### Return type

[**ListCategoryAssignment**](ListCategoryAssignment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalogs_catalog_id_categories_assignments_post**
> catalogs_catalog_id_categories_assignments_post(catalog_id, category_assignment)



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
    CategoryApi.catalogs_catalog_id_categories_assignments_post(catalog_id, category_assignment)
except ApiException as e:
    print("Exception when calling CategoryApi->catalogs_catalog_id_categories_assignments_post: %s\n" % e)
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

# **catalogs_catalog_id_categories_category_id_assignments_delete**
> catalogs_catalog_id_categories_category_id_assignments_delete(catalog_id, category_id, buyer_id, user_id=user_id, user_group_id=user_group_id)



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
    CategoryApi.catalogs_catalog_id_categories_category_id_assignments_delete(catalog_id, category_id, buyer_id, user_id=user_id, user_group_id=user_group_id)
except ApiException as e:
    print("Exception when calling CategoryApi->catalogs_catalog_id_categories_category_id_assignments_delete: %s\n" % e)
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

# **catalogs_catalog_id_categories_category_id_delete**
> catalogs_catalog_id_categories_category_id_delete(catalog_id, category_id)



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
    CategoryApi.catalogs_catalog_id_categories_category_id_delete(catalog_id, category_id)
except ApiException as e:
    print("Exception when calling CategoryApi->catalogs_catalog_id_categories_category_id_delete: %s\n" % e)
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

# **catalogs_catalog_id_categories_category_id_get**
> Category catalogs_catalog_id_categories_category_id_get(catalog_id, category_id)



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
    response = CategoryApi.catalogs_catalog_id_categories_category_id_get(catalog_id, category_id)
    print(response)
except ApiException as e:
    print("Exception when calling CategoryApi->catalogs_catalog_id_categories_category_id_get: %s\n" % e)
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

# **catalogs_catalog_id_categories_category_id_patch**
> Category catalogs_catalog_id_categories_category_id_patch(catalog_id, category_id, category)



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
    response = CategoryApi.catalogs_catalog_id_categories_category_id_patch(catalog_id, category_id, category)
    print(response)
except ApiException as e:
    print("Exception when calling CategoryApi->catalogs_catalog_id_categories_category_id_patch: %s\n" % e)
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

# **catalogs_catalog_id_categories_category_id_productassignments_product_id_delete**
> catalogs_catalog_id_categories_category_id_productassignments_product_id_delete(catalog_id, category_id, product_id)



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
    CategoryApi.catalogs_catalog_id_categories_category_id_productassignments_product_id_delete(catalog_id, category_id, product_id)
except ApiException as e:
    print("Exception when calling CategoryApi->catalogs_catalog_id_categories_category_id_productassignments_product_id_delete: %s\n" % e)
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

# **catalogs_catalog_id_categories_category_id_put**
> Category catalogs_catalog_id_categories_category_id_put(catalog_id, category_id, category)



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
    response = CategoryApi.catalogs_catalog_id_categories_category_id_put(catalog_id, category_id, category)
    print(response)
except ApiException as e:
    print("Exception when calling CategoryApi->catalogs_catalog_id_categories_category_id_put: %s\n" % e)
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

# **catalogs_catalog_id_categories_get**
> ListCategory catalogs_catalog_id_categories_get(catalog_id, depth=depth, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CategoryApi = OrderCloud.CategoryApi
catalog_id = 'catalog_id_example' # str | ID of the catalog.
depth = 'depth_example' # str | Depth of the category. (optional)
search = 'search_example' # str | Search of the category. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the category. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the category. (optional)
page = 56 # int | Page of the category. (optional)
page_size = 56 # int | Page size of the category. (optional)

try: 
    response = CategoryApi.catalogs_catalog_id_categories_get(catalog_id, depth=depth, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling CategoryApi->catalogs_catalog_id_categories_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | 
 **depth** | **str**| Depth of the category. | [optional] 
 **search** | **str**| Search of the category. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the category. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the category. | [optional] 
 **page** | **int**| Page of the category. | [optional] 
 **page_size** | **int**| Page size of the category. | [optional] 

### Return type

[**ListCategory**](ListCategory.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalogs_catalog_id_categories_post**
> Category catalogs_catalog_id_categories_post(catalog_id, category)



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
    response = CategoryApi.catalogs_catalog_id_categories_post(catalog_id, category)
    print(response)
except ApiException as e:
    print("Exception when calling CategoryApi->catalogs_catalog_id_categories_post: %s\n" % e)
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

# **catalogs_catalog_id_categories_productassignments_get**
> ListCategoryProductAssignment catalogs_catalog_id_categories_productassignments_get(catalog_id, category_id=category_id, product_id=product_id, page=page, page_size=page_size)



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
page = 56 # int | Page of the category. (optional)
page_size = 56 # int | Page size of the category. (optional)

try: 
    response = CategoryApi.catalogs_catalog_id_categories_productassignments_get(catalog_id, category_id=category_id, product_id=product_id, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling CategoryApi->catalogs_catalog_id_categories_productassignments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | 
 **category_id** | **str**| ID of the category. | [optional] 
 **product_id** | **str**| ID of the product. | [optional] 
 **page** | **int**| Page of the category. | [optional] 
 **page_size** | **int**| Page size of the category. | [optional] 

### Return type

[**ListCategoryProductAssignment**](ListCategoryProductAssignment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalogs_catalog_id_categories_productassignments_post**
> catalogs_catalog_id_categories_productassignments_post(catalog_id, product_assignment)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CategoryApi = OrderCloud.CategoryApi
catalog_id = 'catalog_id_example' # str | ID of the catalog.
product_assignment = OrderCloud.CategoryProductAssignment() # CategoryProductAssignment | 

try: 
    CategoryApi.catalogs_catalog_id_categories_productassignments_post(catalog_id, product_assignment)
except ApiException as e:
    print("Exception when calling CategoryApi->catalogs_catalog_id_categories_productassignments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | 
 **product_assignment** | [**CategoryProductAssignment**](CategoryProductAssignment.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

