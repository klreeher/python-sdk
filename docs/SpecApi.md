# OrderCloud.SpecApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**specs_get**](SpecApi.md#specs_get) | **GET** /specs | 
[**specs_post**](SpecApi.md#specs_post) | **POST** /specs | 
[**specs_productassignments_get**](SpecApi.md#specs_productassignments_get) | **GET** /specs/productassignments | 
[**specs_productassignments_post**](SpecApi.md#specs_productassignments_post) | **POST** /specs/productassignments | 
[**specs_spec_id_delete**](SpecApi.md#specs_spec_id_delete) | **DELETE** /specs/{specID} | 
[**specs_spec_id_get**](SpecApi.md#specs_spec_id_get) | **GET** /specs/{specID} | 
[**specs_spec_id_options_get**](SpecApi.md#specs_spec_id_options_get) | **GET** /specs/{specID}/options | 
[**specs_spec_id_options_option_id_delete**](SpecApi.md#specs_spec_id_options_option_id_delete) | **DELETE** /specs/{specID}/options/{optionID} | 
[**specs_spec_id_options_option_id_get**](SpecApi.md#specs_spec_id_options_option_id_get) | **GET** /specs/{specID}/options/{optionID} | 
[**specs_spec_id_options_option_id_patch**](SpecApi.md#specs_spec_id_options_option_id_patch) | **PATCH** /specs/{specID}/options/{optionID} | 
[**specs_spec_id_options_option_id_put**](SpecApi.md#specs_spec_id_options_option_id_put) | **PUT** /specs/{specID}/options/{optionID} | 
[**specs_spec_id_options_post**](SpecApi.md#specs_spec_id_options_post) | **POST** /specs/{specID}/options | 
[**specs_spec_id_patch**](SpecApi.md#specs_spec_id_patch) | **PATCH** /specs/{specID} | 
[**specs_spec_id_productassignments_product_id_delete**](SpecApi.md#specs_spec_id_productassignments_product_id_delete) | **DELETE** /specs/{specID}/productassignments/{productID} | 
[**specs_spec_id_put**](SpecApi.md#specs_spec_id_put) | **PUT** /specs/{specID} | 


# **specs_get**
> ListSpec specs_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SpecApi = OrderCloud.SpecApi
search = 'search_example' # str | Search of the spec. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the spec. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the spec. (optional)
page = 56 # int | Page of the spec. (optional)
page_size = 56 # int | Page size of the spec. (optional)

try: 
    response = SpecApi.specs_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling SpecApi->specs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search of the spec. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the spec. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the spec. | [optional] 
 **page** | **int**| Page of the spec. | [optional] 
 **page_size** | **int**| Page size of the spec. | [optional] 

### Return type

[**ListSpec**](ListSpec.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **specs_post**
> Spec specs_post(spec)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SpecApi = OrderCloud.SpecApi
spec = OrderCloud.Spec() # Spec | 

try: 
    response = SpecApi.specs_post(spec)
    print(response)
except ApiException as e:
    print("Exception when calling SpecApi->specs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec** | [**Spec**](Spec.md)|  | 

### Return type

[**Spec**](Spec.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **specs_productassignments_get**
> ListSpecProductAssignment specs_productassignments_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SpecApi = OrderCloud.SpecApi
search = 'search_example' # str | Search of the spec. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the spec. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the spec. (optional)
page = 56 # int | Page of the spec. (optional)
page_size = 56 # int | Page size of the spec. (optional)

try: 
    response = SpecApi.specs_productassignments_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling SpecApi->specs_productassignments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search of the spec. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the spec. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the spec. | [optional] 
 **page** | **int**| Page of the spec. | [optional] 
 **page_size** | **int**| Page size of the spec. | [optional] 

### Return type

[**ListSpecProductAssignment**](ListSpecProductAssignment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **specs_productassignments_post**
> specs_productassignments_post(product_assignment)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SpecApi = OrderCloud.SpecApi
product_assignment = OrderCloud.SpecProductAssignment() # SpecProductAssignment | 

try: 
    SpecApi.specs_productassignments_post(product_assignment)
except ApiException as e:
    print("Exception when calling SpecApi->specs_productassignments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_assignment** | [**SpecProductAssignment**](SpecProductAssignment.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **specs_spec_id_delete**
> specs_spec_id_delete(spec_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SpecApi = OrderCloud.SpecApi
spec_id = 'spec_id_example' # str | ID of the spec.

try: 
    SpecApi.specs_spec_id_delete(spec_id)
except ApiException as e:
    print("Exception when calling SpecApi->specs_spec_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_id** | **str**| ID of the spec. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **specs_spec_id_get**
> Spec specs_spec_id_get(spec_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SpecApi = OrderCloud.SpecApi
spec_id = 'spec_id_example' # str | ID of the spec.

try: 
    response = SpecApi.specs_spec_id_get(spec_id)
    print(response)
except ApiException as e:
    print("Exception when calling SpecApi->specs_spec_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_id** | **str**| ID of the spec. | 

### Return type

[**Spec**](Spec.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **specs_spec_id_options_get**
> ListSpecOption specs_spec_id_options_get(spec_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SpecApi = OrderCloud.SpecApi
spec_id = 'spec_id_example' # str | ID of the spec.
search = 'search_example' # str | Search of the spec. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the spec. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the spec. (optional)
page = 56 # int | Page of the spec. (optional)
page_size = 56 # int | Page size of the spec. (optional)

try: 
    response = SpecApi.specs_spec_id_options_get(spec_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling SpecApi->specs_spec_id_options_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_id** | **str**| ID of the spec. | 
 **search** | **str**| Search of the spec. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the spec. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the spec. | [optional] 
 **page** | **int**| Page of the spec. | [optional] 
 **page_size** | **int**| Page size of the spec. | [optional] 

### Return type

[**ListSpecOption**](ListSpecOption.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **specs_spec_id_options_option_id_delete**
> specs_spec_id_options_option_id_delete(spec_id, option_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SpecApi = OrderCloud.SpecApi
spec_id = 'spec_id_example' # str | ID of the spec.
option_id = 'option_id_example' # str | ID of the option.

try: 
    SpecApi.specs_spec_id_options_option_id_delete(spec_id, option_id)
except ApiException as e:
    print("Exception when calling SpecApi->specs_spec_id_options_option_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_id** | **str**| ID of the spec. | 
 **option_id** | **str**| ID of the option. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **specs_spec_id_options_option_id_get**
> SpecOption specs_spec_id_options_option_id_get(spec_id, option_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SpecApi = OrderCloud.SpecApi
spec_id = 'spec_id_example' # str | ID of the spec.
option_id = 'option_id_example' # str | ID of the option.

try: 
    response = SpecApi.specs_spec_id_options_option_id_get(spec_id, option_id)
    print(response)
except ApiException as e:
    print("Exception when calling SpecApi->specs_spec_id_options_option_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_id** | **str**| ID of the spec. | 
 **option_id** | **str**| ID of the option. | 

### Return type

[**SpecOption**](SpecOption.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **specs_spec_id_options_option_id_patch**
> SpecOption specs_spec_id_options_option_id_patch(spec_id, option_id, option)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SpecApi = OrderCloud.SpecApi
spec_id = 'spec_id_example' # str | ID of the spec.
option_id = 'option_id_example' # str | ID of the option.
option = OrderCloud.SpecOption() # SpecOption | 

try: 
    response = SpecApi.specs_spec_id_options_option_id_patch(spec_id, option_id, option)
    print(response)
except ApiException as e:
    print("Exception when calling SpecApi->specs_spec_id_options_option_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_id** | **str**| ID of the spec. | 
 **option_id** | **str**| ID of the option. | 
 **option** | [**SpecOption**](SpecOption.md)|  | 

### Return type

[**SpecOption**](SpecOption.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **specs_spec_id_options_option_id_put**
> SpecOption specs_spec_id_options_option_id_put(spec_id, option_id, option)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SpecApi = OrderCloud.SpecApi
spec_id = 'spec_id_example' # str | ID of the spec.
option_id = 'option_id_example' # str | ID of the option.
option = OrderCloud.SpecOption() # SpecOption | 

try: 
    response = SpecApi.specs_spec_id_options_option_id_put(spec_id, option_id, option)
    print(response)
except ApiException as e:
    print("Exception when calling SpecApi->specs_spec_id_options_option_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_id** | **str**| ID of the spec. | 
 **option_id** | **str**| ID of the option. | 
 **option** | [**SpecOption**](SpecOption.md)|  | 

### Return type

[**SpecOption**](SpecOption.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **specs_spec_id_options_post**
> SpecOption specs_spec_id_options_post(spec_id, option)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SpecApi = OrderCloud.SpecApi
spec_id = 'spec_id_example' # str | ID of the spec.
option = OrderCloud.SpecOption() # SpecOption | 

try: 
    response = SpecApi.specs_spec_id_options_post(spec_id, option)
    print(response)
except ApiException as e:
    print("Exception when calling SpecApi->specs_spec_id_options_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_id** | **str**| ID of the spec. | 
 **option** | [**SpecOption**](SpecOption.md)|  | 

### Return type

[**SpecOption**](SpecOption.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **specs_spec_id_patch**
> Spec specs_spec_id_patch(spec_id, spec)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SpecApi = OrderCloud.SpecApi
spec_id = 'spec_id_example' # str | ID of the spec.
spec = OrderCloud.Spec() # Spec | 

try: 
    response = SpecApi.specs_spec_id_patch(spec_id, spec)
    print(response)
except ApiException as e:
    print("Exception when calling SpecApi->specs_spec_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_id** | **str**| ID of the spec. | 
 **spec** | [**Spec**](Spec.md)|  | 

### Return type

[**Spec**](Spec.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **specs_spec_id_productassignments_product_id_delete**
> specs_spec_id_productassignments_product_id_delete(spec_id, product_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SpecApi = OrderCloud.SpecApi
spec_id = 'spec_id_example' # str | ID of the spec.
product_id = 'product_id_example' # str | ID of the product.

try: 
    SpecApi.specs_spec_id_productassignments_product_id_delete(spec_id, product_id)
except ApiException as e:
    print("Exception when calling SpecApi->specs_spec_id_productassignments_product_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_id** | **str**| ID of the spec. | 
 **product_id** | **str**| ID of the product. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **specs_spec_id_put**
> Spec specs_spec_id_put(spec_id, spec)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
SpecApi = OrderCloud.SpecApi
spec_id = 'spec_id_example' # str | ID of the spec.
spec = OrderCloud.Spec() # Spec | 

try: 
    response = SpecApi.specs_spec_id_put(spec_id, spec)
    print(response)
except ApiException as e:
    print("Exception when calling SpecApi->specs_spec_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_id** | **str**| ID of the spec. | 
 **spec** | [**Spec**](Spec.md)|  | 

### Return type

[**Spec**](Spec.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

