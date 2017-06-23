# OrderCloud.ProductApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_assignments_get**](ProductApi.md#products_assignments_get) | **GET** /products/assignments | 
[**products_assignments_post**](ProductApi.md#products_assignments_post) | **POST** /products/assignments | 
[**products_get**](ProductApi.md#products_get) | **GET** /products | 
[**products_post**](ProductApi.md#products_post) | **POST** /products | 
[**products_product_id_assignments_buyer_id_delete**](ProductApi.md#products_product_id_assignments_buyer_id_delete) | **DELETE** /products/{productID}/assignments/{buyerID} | 
[**products_product_id_delete**](ProductApi.md#products_product_id_delete) | **DELETE** /products/{productID} | 
[**products_product_id_get**](ProductApi.md#products_product_id_get) | **GET** /products/{productID} | 
[**products_product_id_patch**](ProductApi.md#products_product_id_patch) | **PATCH** /products/{productID} | 
[**products_product_id_put**](ProductApi.md#products_product_id_put) | **PUT** /products/{productID} | 
[**products_product_id_suppliers_get**](ProductApi.md#products_product_id_suppliers_get) | **GET** /products/{productID}/suppliers | 
[**products_product_id_suppliers_supplier_id_delete**](ProductApi.md#products_product_id_suppliers_supplier_id_delete) | **DELETE** /products/{productID}/suppliers/{supplierID} | 
[**products_product_id_suppliers_supplier_id_put**](ProductApi.md#products_product_id_suppliers_supplier_id_put) | **PUT** /products/{productID}/suppliers/{supplierID} | 
[**products_product_id_variants_generate_post**](ProductApi.md#products_product_id_variants_generate_post) | **POST** /products/{productID}/variants/generate | 
[**products_product_id_variants_get**](ProductApi.md#products_product_id_variants_get) | **GET** /products/{productID}/variants | 
[**products_product_id_variants_variant_id_get**](ProductApi.md#products_product_id_variants_variant_id_get) | **GET** /products/{productID}/variants/{variantID} | 
[**products_product_id_variants_variant_id_patch**](ProductApi.md#products_product_id_variants_variant_id_patch) | **PATCH** /products/{productID}/variants/{variantID} | 
[**products_product_id_variants_variant_id_put**](ProductApi.md#products_product_id_variants_variant_id_put) | **PUT** /products/{productID}/variants/{variantID} | 


# **products_assignments_get**
> ListProductAssignment products_assignments_get(product_id=product_id, price_schedule_id=price_schedule_id, buyer_id=buyer_id, user_id=user_id, user_group_id=user_group_id, level=level, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ProductApi = OrderCloud.ProductApi
product_id = 'product_id_example' # str | ID of the product. (optional)
price_schedule_id = 'price_schedule_id_example' # str | ID of the price schedule. (optional)
buyer_id = 'buyer_id_example' # str | ID of the buyer. (optional)
user_id = 'user_id_example' # str | ID of the user. (optional)
user_group_id = 'user_group_id_example' # str | ID of the user group. (optional)
level = 'level_example' # str | Level of the product. (optional)
page = 56 # int | Page of the product. (optional)
page_size = 56 # int | Page size of the product. (optional)

try: 
    response = ProductApi.products_assignments_get(product_id=product_id, price_schedule_id=price_schedule_id, buyer_id=buyer_id, user_id=user_id, user_group_id=user_group_id, level=level, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling ProductApi->products_assignments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of the product. | [optional] 
 **price_schedule_id** | **str**| ID of the price schedule. | [optional] 
 **buyer_id** | **str**| ID of the buyer. | [optional] 
 **user_id** | **str**| ID of the user. | [optional] 
 **user_group_id** | **str**| ID of the user group. | [optional] 
 **level** | **str**| Level of the product. | [optional] 
 **page** | **int**| Page of the product. | [optional] 
 **page_size** | **int**| Page size of the product. | [optional] 

### Return type

[**ListProductAssignment**](ListProductAssignment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_assignments_post**
> products_assignments_post(product_assignment)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ProductApi = OrderCloud.ProductApi
product_assignment = OrderCloud.ProductAssignment() # ProductAssignment | 

try: 
    ProductApi.products_assignments_post(product_assignment)
except ApiException as e:
    print("Exception when calling ProductApi->products_assignments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_assignment** | [**ProductAssignment**](ProductAssignment.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_get**
> ListProduct products_get(catalog_id=catalog_id, category_id=category_id, supplier_id=supplier_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ProductApi = OrderCloud.ProductApi
catalog_id = 'catalog_id_example' # str | ID of the catalog. (optional)
category_id = 'category_id_example' # str | ID of the category. (optional)
supplier_id = 'supplier_id_example' # str | ID of the supplier. (optional)
search = 'search_example' # str | Search of the product. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the product. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the product. (optional)
page = 56 # int | Page of the product. (optional)
page_size = 56 # int | Page size of the product. (optional)

try: 
    response = ProductApi.products_get(catalog_id=catalog_id, category_id=category_id, supplier_id=supplier_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling ProductApi->products_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| ID of the catalog. | [optional] 
 **category_id** | **str**| ID of the category. | [optional] 
 **supplier_id** | **str**| ID of the supplier. | [optional] 
 **search** | **str**| Search of the product. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the product. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the product. | [optional] 
 **page** | **int**| Page of the product. | [optional] 
 **page_size** | **int**| Page size of the product. | [optional] 

### Return type

[**ListProduct**](ListProduct.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_post**
> Product products_post(product)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ProductApi = OrderCloud.ProductApi
product = OrderCloud.Product() # Product | 

try: 
    response = ProductApi.products_post(product)
    print(response)
except ApiException as e:
    print("Exception when calling ProductApi->products_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | [**Product**](Product.md)|  | 

### Return type

[**Product**](Product.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_assignments_buyer_id_delete**
> products_product_id_assignments_buyer_id_delete(product_id, buyer_id, user_id=user_id, user_group_id=user_group_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ProductApi = OrderCloud.ProductApi
product_id = 'product_id_example' # str | ID of the product.
buyer_id = 'buyer_id_example' # str | ID of the buyer.
user_id = 'user_id_example' # str | ID of the user. (optional)
user_group_id = 'user_group_id_example' # str | ID of the user group. (optional)

try: 
    ProductApi.products_product_id_assignments_buyer_id_delete(product_id, buyer_id, user_id=user_id, user_group_id=user_group_id)
except ApiException as e:
    print("Exception when calling ProductApi->products_product_id_assignments_buyer_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of the product. | 
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

# **products_product_id_delete**
> products_product_id_delete(product_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ProductApi = OrderCloud.ProductApi
product_id = 'product_id_example' # str | ID of the product.

try: 
    ProductApi.products_product_id_delete(product_id)
except ApiException as e:
    print("Exception when calling ProductApi->products_product_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of the product. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_get**
> Product products_product_id_get(product_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ProductApi = OrderCloud.ProductApi
product_id = 'product_id_example' # str | ID of the product.

try: 
    response = ProductApi.products_product_id_get(product_id)
    print(response)
except ApiException as e:
    print("Exception when calling ProductApi->products_product_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of the product. | 

### Return type

[**Product**](Product.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_patch**
> Product products_product_id_patch(product_id, product)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ProductApi = OrderCloud.ProductApi
product_id = 'product_id_example' # str | ID of the product.
product = OrderCloud.Product() # Product | 

try: 
    response = ProductApi.products_product_id_patch(product_id, product)
    print(response)
except ApiException as e:
    print("Exception when calling ProductApi->products_product_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of the product. | 
 **product** | [**Product**](Product.md)|  | 

### Return type

[**Product**](Product.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_put**
> Product products_product_id_put(product_id, product)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ProductApi = OrderCloud.ProductApi
product_id = 'product_id_example' # str | ID of the product.
product = OrderCloud.Product() # Product | 

try: 
    response = ProductApi.products_product_id_put(product_id, product)
    print(response)
except ApiException as e:
    print("Exception when calling ProductApi->products_product_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of the product. | 
 **product** | [**Product**](Product.md)|  | 

### Return type

[**Product**](Product.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_suppliers_get**
> ListSupplier products_product_id_suppliers_get(product_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ProductApi = OrderCloud.ProductApi
product_id = 'product_id_example' # str | ID of the product.
search = 'search_example' # str | Search of the product. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the product. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the product. (optional)
page = 56 # int | Page of the product. (optional)
page_size = 56 # int | Page size of the product. (optional)

try: 
    response = ProductApi.products_product_id_suppliers_get(product_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling ProductApi->products_product_id_suppliers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of the product. | 
 **search** | **str**| Search of the product. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the product. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the product. | [optional] 
 **page** | **int**| Page of the product. | [optional] 
 **page_size** | **int**| Page size of the product. | [optional] 

### Return type

[**ListSupplier**](ListSupplier.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_suppliers_supplier_id_delete**
> products_product_id_suppliers_supplier_id_delete(product_id, supplier_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ProductApi = OrderCloud.ProductApi
product_id = 'product_id_example' # str | ID of the product.
supplier_id = 'supplier_id_example' # str | ID of the supplier.

try: 
    ProductApi.products_product_id_suppliers_supplier_id_delete(product_id, supplier_id)
except ApiException as e:
    print("Exception when calling ProductApi->products_product_id_suppliers_supplier_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of the product. | 
 **supplier_id** | **str**| ID of the supplier. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_suppliers_supplier_id_put**
> products_product_id_suppliers_supplier_id_put(product_id, supplier_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ProductApi = OrderCloud.ProductApi
product_id = 'product_id_example' # str | ID of the product.
supplier_id = 'supplier_id_example' # str | ID of the supplier.

try: 
    ProductApi.products_product_id_suppliers_supplier_id_put(product_id, supplier_id)
except ApiException as e:
    print("Exception when calling ProductApi->products_product_id_suppliers_supplier_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of the product. | 
 **supplier_id** | **str**| ID of the supplier. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_variants_generate_post**
> Product products_product_id_variants_generate_post(product_id, overwrite_existing=overwrite_existing)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ProductApi = OrderCloud.ProductApi
product_id = 'product_id_example' # str | ID of the product.
overwrite_existing = true # bool | Overwrite existing of the product. (optional)

try: 
    response = ProductApi.products_product_id_variants_generate_post(product_id, overwrite_existing=overwrite_existing)
    print(response)
except ApiException as e:
    print("Exception when calling ProductApi->products_product_id_variants_generate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of the product. | 
 **overwrite_existing** | **bool**| Overwrite existing of the product. | [optional] 

### Return type

[**Product**](Product.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_variants_get**
> ListVariant products_product_id_variants_get(product_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ProductApi = OrderCloud.ProductApi
product_id = 'product_id_example' # str | ID of the product.
search = 'search_example' # str | Search of the product. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the product. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the product. (optional)
page = 56 # int | Page of the product. (optional)
page_size = 56 # int | Page size of the product. (optional)

try: 
    response = ProductApi.products_product_id_variants_get(product_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling ProductApi->products_product_id_variants_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of the product. | 
 **search** | **str**| Search of the product. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the product. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the product. | [optional] 
 **page** | **int**| Page of the product. | [optional] 
 **page_size** | **int**| Page size of the product. | [optional] 

### Return type

[**ListVariant**](ListVariant.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_variants_variant_id_get**
> Variant products_product_id_variants_variant_id_get(product_id, variant_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ProductApi = OrderCloud.ProductApi
product_id = 'product_id_example' # str | ID of the product.
variant_id = 'variant_id_example' # str | ID of the variant.

try: 
    response = ProductApi.products_product_id_variants_variant_id_get(product_id, variant_id)
    print(response)
except ApiException as e:
    print("Exception when calling ProductApi->products_product_id_variants_variant_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of the product. | 
 **variant_id** | **str**| ID of the variant. | 

### Return type

[**Variant**](Variant.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_variants_variant_id_patch**
> Variant products_product_id_variants_variant_id_patch(product_id, variant_id, variant)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ProductApi = OrderCloud.ProductApi
product_id = 'product_id_example' # str | ID of the product.
variant_id = 'variant_id_example' # str | ID of the variant.
variant = OrderCloud.Variant() # Variant | 

try: 
    response = ProductApi.products_product_id_variants_variant_id_patch(product_id, variant_id, variant)
    print(response)
except ApiException as e:
    print("Exception when calling ProductApi->products_product_id_variants_variant_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of the product. | 
 **variant_id** | **str**| ID of the variant. | 
 **variant** | [**Variant**](Variant.md)|  | 

### Return type

[**Variant**](Variant.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_variants_variant_id_put**
> Variant products_product_id_variants_variant_id_put(product_id, variant_id, variant)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ProductApi = OrderCloud.ProductApi
product_id = 'product_id_example' # str | ID of the product.
variant_id = 'variant_id_example' # str | ID of the variant.
variant = OrderCloud.Variant() # Variant | 

try: 
    response = ProductApi.products_product_id_variants_variant_id_put(product_id, variant_id, variant)
    print(response)
except ApiException as e:
    print("Exception when calling ProductApi->products_product_id_variants_variant_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of the product. | 
 **variant_id** | **str**| ID of the variant. | 
 **variant** | [**Variant**](Variant.md)|  | 

### Return type

[**Variant**](Variant.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

