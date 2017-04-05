# OrderCloud.CatalogApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](CatalogApi.md#create) | **POST** /catalogs | 
[**delete**](CatalogApi.md#delete) | **DELETE** /catalogs/{catalogID} | 
[**delete_assignment**](CatalogApi.md#delete_assignment) | **DELETE** /catalogs/{catalogID}/assignments | 
[**delete_product_assignment**](CatalogApi.md#delete_product_assignment) | **DELETE** /catalogs/{catalogID}/productassignments/{productID} | 
[**get**](CatalogApi.md#get) | **GET** /catalogs/{catalogID} | 
[**list**](CatalogApi.md#list) | **GET** /catalogs | 
[**list_assignments**](CatalogApi.md#list_assignments) | **GET** /catalogs/assignments | 
[**list_product_assignments**](CatalogApi.md#list_product_assignments) | **GET** /catalogs/productassignments | 
[**patch**](CatalogApi.md#patch) | **PATCH** /catalogs/{catalogID} | 
[**save_assignment**](CatalogApi.md#save_assignment) | **POST** /catalogs/assignments | 
[**save_product_assignment**](CatalogApi.md#save_product_assignment) | **POST** /catalogs/productassignments | 
[**update**](CatalogApi.md#update) | **PUT** /catalogs/{catalogID} | 


# **create**
> Catalog create(catalog)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CatalogApi = OrderCloud.CatalogApi
catalog = OrderCloud.Catalog() # Catalog | 

try: 
    response = CatalogApi.create(catalog)
    print(response)
except ApiException as e:
    print("Exception when calling CatalogApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | [**Catalog**](Catalog.md)|  | 

### Return type

[**Catalog**](Catalog.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(catalog_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CatalogApi = OrderCloud.CatalogApi
catalog_id = 'catalog_id_example' # str | ID of the catalog.

try: 
    CatalogApi.delete(catalog_id)
except ApiException as e:
    print("Exception when calling CatalogApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_assignment**
> delete_assignment(catalog_id, buyer_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CatalogApi = OrderCloud.CatalogApi
catalog_id = 'catalog_id_example' # str | ID of the catalog.
buyer_id = 'buyer_id_example' # str | ID of the buyer.

try: 
    CatalogApi.delete_assignment(catalog_id, buyer_id)
except ApiException as e:
    print("Exception when calling CatalogApi->delete_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | 
 **buyer_id** | **str**| ID of the buyer. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_product_assignment**
> delete_product_assignment(catalog_id, product_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CatalogApi = OrderCloud.CatalogApi
catalog_id = 'catalog_id_example' # str | ID of the catalog.
product_id = 'product_id_example' # str | ID of the product.

try: 
    CatalogApi.delete_product_assignment(catalog_id, product_id)
except ApiException as e:
    print("Exception when calling CatalogApi->delete_product_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | 
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
> Catalog get(catalog_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CatalogApi = OrderCloud.CatalogApi
catalog_id = 'catalog_id_example' # str | ID of the catalog.

try: 
    response = CatalogApi.get(catalog_id)
    print(response)
except ApiException as e:
    print("Exception when calling CatalogApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | 

### Return type

[**Catalog**](Catalog.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ListCatalog list(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CatalogApi = OrderCloud.CatalogApi
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = CatalogApi.list(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling CatalogApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Word or phrase to search for. | [optional] 
 **search_on** | **str**| Comma-delimited list of fields to search on. | [optional] 
 **sort_by** | **str**| Comma-delimited list of fields to sort by. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 
 **filters** | [**dict(str, str)**](str.md)| Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or &#39;xp.???&#39; | [optional] 

### Return type

[**ListCatalog**](ListCatalog.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assignments**
> ListCatalogAssignment list_assignments(catalog_id=catalog_id, buyer_id=buyer_id, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CatalogApi = OrderCloud.CatalogApi
catalog_id = 'catalog_id_example' # str | ID of the catalog. (optional)
buyer_id = 'buyer_id_example' # str | ID of the buyer. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)

try: 
    response = CatalogApi.list_assignments(catalog_id=catalog_id, buyer_id=buyer_id, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling CatalogApi->list_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | [optional] 
 **buyer_id** | **str**| ID of the buyer. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 

### Return type

[**ListCatalogAssignment**](ListCatalogAssignment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_product_assignments**
> ListProductCatalogAssignment list_product_assignments(catalog_id=catalog_id, product_id=product_id, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CatalogApi = OrderCloud.CatalogApi
catalog_id = 'catalog_id_example' # str | ID of the catalog. (optional)
product_id = 'product_id_example' # str | ID of the product. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)

try: 
    response = CatalogApi.list_product_assignments(catalog_id=catalog_id, product_id=product_id, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling CatalogApi->list_product_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | [optional] 
 **product_id** | **str**| ID of the product. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 

### Return type

[**ListProductCatalogAssignment**](ListProductCatalogAssignment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch**
> Catalog patch(catalog_id, partial_catalog)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CatalogApi = OrderCloud.CatalogApi
catalog_id = 'catalog_id_example' # str | ID of the catalog.
partial_catalog = OrderCloud.Catalog() # Catalog | 

try: 
    response = CatalogApi.patch(catalog_id, partial_catalog)
    print(response)
except ApiException as e:
    print("Exception when calling CatalogApi->patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | 
 **partial_catalog** | [**Catalog**](Catalog.md)|  | 

### Return type

[**Catalog**](Catalog.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_assignment**
> save_assignment(assignment)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CatalogApi = OrderCloud.CatalogApi
assignment = OrderCloud.CatalogAssignment() # CatalogAssignment | 

try: 
    CatalogApi.save_assignment(assignment)
except ApiException as e:
    print("Exception when calling CatalogApi->save_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment** | [**CatalogAssignment**](CatalogAssignment.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_product_assignment**
> save_product_assignment(product_assignment)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CatalogApi = OrderCloud.CatalogApi
product_assignment = OrderCloud.ProductCatalogAssignment() # ProductCatalogAssignment | 

try: 
    CatalogApi.save_product_assignment(product_assignment)
except ApiException as e:
    print("Exception when calling CatalogApi->save_product_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_assignment** | [**ProductCatalogAssignment**](ProductCatalogAssignment.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Catalog update(catalog_id, catalog)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CatalogApi = OrderCloud.CatalogApi
catalog_id = 'catalog_id_example' # str | ID of the catalog.
catalog = OrderCloud.Catalog() # Catalog | 

try: 
    response = CatalogApi.update(catalog_id, catalog)
    print(response)
except ApiException as e:
    print("Exception when calling CatalogApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | 
 **catalog** | [**Catalog**](Catalog.md)|  | 

### Return type

[**Catalog**](Catalog.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

