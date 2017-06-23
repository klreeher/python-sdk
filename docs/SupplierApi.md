# OrderCloud.SupplierApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**suppliers_get**](SupplierApi.md#suppliers_get) | **GET** /suppliers | 
[**suppliers_post**](SupplierApi.md#suppliers_post) | **POST** /suppliers | 
[**suppliers_supplier_id_delete**](SupplierApi.md#suppliers_supplier_id_delete) | **DELETE** /suppliers/{supplierID} | 
[**suppliers_supplier_id_get**](SupplierApi.md#suppliers_supplier_id_get) | **GET** /suppliers/{supplierID} | 
[**suppliers_supplier_id_patch**](SupplierApi.md#suppliers_supplier_id_patch) | **PATCH** /suppliers/{supplierID} | 
[**suppliers_supplier_id_put**](SupplierApi.md#suppliers_supplier_id_put) | **PUT** /suppliers/{supplierID} | 


# **suppliers_get**
> ListSupplier suppliers_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SupplierApi = OrderCloud.SupplierApi
search = 'search_example' # str | Search of the supplier. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the supplier. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the supplier. (optional)
page = 56 # int | Page of the supplier. (optional)
page_size = 56 # int | Page size of the supplier. (optional)

try: 
    response = SupplierApi.suppliers_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling SupplierApi->suppliers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search of the supplier. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the supplier. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the supplier. | [optional] 
 **page** | **int**| Page of the supplier. | [optional] 
 **page_size** | **int**| Page size of the supplier. | [optional] 

### Return type

[**ListSupplier**](ListSupplier.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppliers_post**
> Supplier suppliers_post(company)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SupplierApi = OrderCloud.SupplierApi
company = OrderCloud.Supplier() # Supplier | 

try: 
    response = SupplierApi.suppliers_post(company)
    print(response)
except ApiException as e:
    print("Exception when calling SupplierApi->suppliers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company** | [**Supplier**](Supplier.md)|  | 

### Return type

[**Supplier**](Supplier.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppliers_supplier_id_delete**
> suppliers_supplier_id_delete(supplier_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SupplierApi = OrderCloud.SupplierApi
supplier_id = 'supplier_id_example' # str | ID of the supplier.

try: 
    SupplierApi.suppliers_supplier_id_delete(supplier_id)
except ApiException as e:
    print("Exception when calling SupplierApi->suppliers_supplier_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | **str**| ID of the supplier. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppliers_supplier_id_get**
> Supplier suppliers_supplier_id_get(supplier_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SupplierApi = OrderCloud.SupplierApi
supplier_id = 'supplier_id_example' # str | ID of the supplier.

try: 
    response = SupplierApi.suppliers_supplier_id_get(supplier_id)
    print(response)
except ApiException as e:
    print("Exception when calling SupplierApi->suppliers_supplier_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | **str**| ID of the supplier. | 

### Return type

[**Supplier**](Supplier.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppliers_supplier_id_patch**
> Supplier suppliers_supplier_id_patch(supplier_id, company)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SupplierApi = OrderCloud.SupplierApi
supplier_id = 'supplier_id_example' # str | ID of the supplier.
company = OrderCloud.Supplier() # Supplier | 

try: 
    response = SupplierApi.suppliers_supplier_id_patch(supplier_id, company)
    print(response)
except ApiException as e:
    print("Exception when calling SupplierApi->suppliers_supplier_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | **str**| ID of the supplier. | 
 **company** | [**Supplier**](Supplier.md)|  | 

### Return type

[**Supplier**](Supplier.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppliers_supplier_id_put**
> Supplier suppliers_supplier_id_put(supplier_id, company)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SupplierApi = OrderCloud.SupplierApi
supplier_id = 'supplier_id_example' # str | ID of the supplier.
company = OrderCloud.Supplier() # Supplier | 

try: 
    response = SupplierApi.suppliers_supplier_id_put(supplier_id, company)
    print(response)
except ApiException as e:
    print("Exception when calling SupplierApi->suppliers_supplier_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | **str**| ID of the supplier. | 
 **company** | [**Supplier**](Supplier.md)|  | 

### Return type

[**Supplier**](Supplier.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

