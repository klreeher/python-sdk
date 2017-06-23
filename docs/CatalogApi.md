# OrderCloud.CatalogApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogs_assignments_get**](CatalogApi.md#catalogs_assignments_get) | **GET** /catalogs/assignments | 
[**catalogs_assignments_post**](CatalogApi.md#catalogs_assignments_post) | **POST** /catalogs/assignments | 
[**catalogs_catalog_id_assignments_delete**](CatalogApi.md#catalogs_catalog_id_assignments_delete) | **DELETE** /catalogs/{catalogID}/assignments | 
[**catalogs_catalog_id_delete**](CatalogApi.md#catalogs_catalog_id_delete) | **DELETE** /catalogs/{catalogID} | 
[**catalogs_catalog_id_get**](CatalogApi.md#catalogs_catalog_id_get) | **GET** /catalogs/{catalogID} | 
[**catalogs_catalog_id_patch**](CatalogApi.md#catalogs_catalog_id_patch) | **PATCH** /catalogs/{catalogID} | 
[**catalogs_catalog_id_productassignments_product_id_delete**](CatalogApi.md#catalogs_catalog_id_productassignments_product_id_delete) | **DELETE** /catalogs/{catalogID}/productassignments/{productID} | 
[**catalogs_catalog_id_put**](CatalogApi.md#catalogs_catalog_id_put) | **PUT** /catalogs/{catalogID} | 
[**catalogs_get**](CatalogApi.md#catalogs_get) | **GET** /catalogs | 
[**catalogs_post**](CatalogApi.md#catalogs_post) | **POST** /catalogs | 
[**catalogs_productassignments_get**](CatalogApi.md#catalogs_productassignments_get) | **GET** /catalogs/productassignments | 
[**catalogs_productassignments_post**](CatalogApi.md#catalogs_productassignments_post) | **POST** /catalogs/productassignments | 


# **catalogs_assignments_get**
> ListCatalogAssignment catalogs_assignments_get(catalog_id=catalog_id, buyer_id=buyer_id, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CatalogApi = OrderCloud.CatalogApi
catalog_id = 'catalog_id_example' # str | ID of the catalog. (optional)
buyer_id = 'buyer_id_example' # str | ID of the buyer. (optional)
page = 56 # int | Page of the catalog. (optional)
page_size = 56 # int | Page size of the catalog. (optional)

try: 
    response = CatalogApi.catalogs_assignments_get(catalog_id=catalog_id, buyer_id=buyer_id, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling CatalogApi->catalogs_assignments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | [optional] 
 **buyer_id** | **str**| ID of the buyer. | [optional] 
 **page** | **int**| Page of the catalog. | [optional] 
 **page_size** | **int**| Page size of the catalog. | [optional] 

### Return type

[**ListCatalogAssignment**](ListCatalogAssignment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalogs_assignments_post**
> catalogs_assignments_post(assignment)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CatalogApi = OrderCloud.CatalogApi
assignment = OrderCloud.CatalogAssignment() # CatalogAssignment | 

try: 
    CatalogApi.catalogs_assignments_post(assignment)
except ApiException as e:
    print("Exception when calling CatalogApi->catalogs_assignments_post: %s\n" % e)
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

# **catalogs_catalog_id_assignments_delete**
> catalogs_catalog_id_assignments_delete(catalog_id, buyer_id)



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
    CatalogApi.catalogs_catalog_id_assignments_delete(catalog_id, buyer_id)
except ApiException as e:
    print("Exception when calling CatalogApi->catalogs_catalog_id_assignments_delete: %s\n" % e)
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

# **catalogs_catalog_id_delete**
> catalogs_catalog_id_delete(catalog_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CatalogApi = OrderCloud.CatalogApi
catalog_id = 'catalog_id_example' # str | ID of the catalog.

try: 
    CatalogApi.catalogs_catalog_id_delete(catalog_id)
except ApiException as e:
    print("Exception when calling CatalogApi->catalogs_catalog_id_delete: %s\n" % e)
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

# **catalogs_catalog_id_get**
> Catalog catalogs_catalog_id_get(catalog_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CatalogApi = OrderCloud.CatalogApi
catalog_id = 'catalog_id_example' # str | ID of the catalog.

try: 
    response = CatalogApi.catalogs_catalog_id_get(catalog_id)
    print(response)
except ApiException as e:
    print("Exception when calling CatalogApi->catalogs_catalog_id_get: %s\n" % e)
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

# **catalogs_catalog_id_patch**
> Catalog catalogs_catalog_id_patch(catalog_id, partial_catalog)



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
    response = CatalogApi.catalogs_catalog_id_patch(catalog_id, partial_catalog)
    print(response)
except ApiException as e:
    print("Exception when calling CatalogApi->catalogs_catalog_id_patch: %s\n" % e)
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

# **catalogs_catalog_id_productassignments_product_id_delete**
> catalogs_catalog_id_productassignments_product_id_delete(catalog_id, product_id)



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
    CatalogApi.catalogs_catalog_id_productassignments_product_id_delete(catalog_id, product_id)
except ApiException as e:
    print("Exception when calling CatalogApi->catalogs_catalog_id_productassignments_product_id_delete: %s\n" % e)
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

# **catalogs_catalog_id_put**
> Catalog catalogs_catalog_id_put(catalog_id, catalog)



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
    response = CatalogApi.catalogs_catalog_id_put(catalog_id, catalog)
    print(response)
except ApiException as e:
    print("Exception when calling CatalogApi->catalogs_catalog_id_put: %s\n" % e)
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

# **catalogs_get**
> ListCatalog catalogs_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CatalogApi = OrderCloud.CatalogApi
search = 'search_example' # str | Search of the catalog. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the catalog. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the catalog. (optional)
page = 56 # int | Page of the catalog. (optional)
page_size = 56 # int | Page size of the catalog. (optional)

try: 
    response = CatalogApi.catalogs_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling CatalogApi->catalogs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search of the catalog. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the catalog. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the catalog. | [optional] 
 **page** | **int**| Page of the catalog. | [optional] 
 **page_size** | **int**| Page size of the catalog. | [optional] 

### Return type

[**ListCatalog**](ListCatalog.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalogs_post**
> Catalog catalogs_post(catalog)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CatalogApi = OrderCloud.CatalogApi
catalog = OrderCloud.Catalog() # Catalog | 

try: 
    response = CatalogApi.catalogs_post(catalog)
    print(response)
except ApiException as e:
    print("Exception when calling CatalogApi->catalogs_post: %s\n" % e)
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

# **catalogs_productassignments_get**
> ListProductCatalogAssignment catalogs_productassignments_get(catalog_id=catalog_id, product_id=product_id, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CatalogApi = OrderCloud.CatalogApi
catalog_id = 'catalog_id_example' # str | ID of the catalog. (optional)
product_id = 'product_id_example' # str | ID of the product. (optional)
page = 56 # int | Page of the catalog. (optional)
page_size = 56 # int | Page size of the catalog. (optional)

try: 
    response = CatalogApi.catalogs_productassignments_get(catalog_id=catalog_id, product_id=product_id, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling CatalogApi->catalogs_productassignments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | [optional] 
 **product_id** | **str**| ID of the product. | [optional] 
 **page** | **int**| Page of the catalog. | [optional] 
 **page_size** | **int**| Page size of the catalog. | [optional] 

### Return type

[**ListProductCatalogAssignment**](ListProductCatalogAssignment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalogs_productassignments_post**
> catalogs_productassignments_post(product_assignment)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
CatalogApi = OrderCloud.CatalogApi
product_assignment = OrderCloud.ProductCatalogAssignment() # ProductCatalogAssignment | 

try: 
    CatalogApi.catalogs_productassignments_post(product_assignment)
except ApiException as e:
    print("Exception when calling CatalogApi->catalogs_productassignments_post: %s\n" % e)
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

