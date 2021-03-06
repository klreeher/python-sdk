# OrderCloud.ApprovalRuleApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ApprovalRuleApi.md#create) | **POST** /buyers/{buyerID}/approvalrules | 
[**delete**](ApprovalRuleApi.md#delete) | **DELETE** /buyers/{buyerID}/approvalrules/{approvalRuleID} | 
[**get**](ApprovalRuleApi.md#get) | **GET** /buyers/{buyerID}/approvalrules/{approvalRuleID} | 
[**list**](ApprovalRuleApi.md#list) | **GET** /buyers/{buyerID}/approvalrules | 
[**patch**](ApprovalRuleApi.md#patch) | **PATCH** /buyers/{buyerID}/approvalrules/{approvalRuleID} | 
[**save**](ApprovalRuleApi.md#save) | **PUT** /buyers/{buyerID}/approvalrules/{approvalRuleID} | 


# **create**
> ApprovalRule create(buyer_id, approval_rule)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ApprovalRuleApi = OrderCloud.ApprovalRuleApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
approval_rule = OrderCloud.ApprovalRule() # ApprovalRule | 

try: 
    response = ApprovalRuleApi.create(buyer_id, approval_rule)
    print(response)
except ApiException as e:
    print("Exception when calling ApprovalRuleApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **approval_rule** | [**ApprovalRule**](ApprovalRule.md)|  | 

### Return type

[**ApprovalRule**](ApprovalRule.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(buyer_id, approval_rule_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ApprovalRuleApi = OrderCloud.ApprovalRuleApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
approval_rule_id = 'approval_rule_id_example' # str | ID of the approval rule.

try: 
    ApprovalRuleApi.delete(buyer_id, approval_rule_id)
except ApiException as e:
    print("Exception when calling ApprovalRuleApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **approval_rule_id** | **str**| ID of the approval rule. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> ApprovalRule get(buyer_id, approval_rule_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ApprovalRuleApi = OrderCloud.ApprovalRuleApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
approval_rule_id = 'approval_rule_id_example' # str | ID of the approval rule.

try: 
    response = ApprovalRuleApi.get(buyer_id, approval_rule_id)
    print(response)
except ApiException as e:
    print("Exception when calling ApprovalRuleApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **approval_rule_id** | **str**| ID of the approval rule. | 

### Return type

[**ApprovalRule**](ApprovalRule.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ListApprovalRule list(buyer_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ApprovalRuleApi = OrderCloud.ApprovalRuleApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = ApprovalRuleApi.list(buyer_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling ApprovalRuleApi->list: %s\n" % e)
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

[**ListApprovalRule**](ListApprovalRule.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch**
> ApprovalRule patch(buyer_id, approval_rule_id, partial_approval_rule)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ApprovalRuleApi = OrderCloud.ApprovalRuleApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
approval_rule_id = 'approval_rule_id_example' # str | ID of the approval rule.
partial_approval_rule = OrderCloud.ApprovalRule() # ApprovalRule | 

try: 
    response = ApprovalRuleApi.patch(buyer_id, approval_rule_id, partial_approval_rule)
    print(response)
except ApiException as e:
    print("Exception when calling ApprovalRuleApi->patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **approval_rule_id** | **str**| ID of the approval rule. | 
 **partial_approval_rule** | [**ApprovalRule**](ApprovalRule.md)|  | 

### Return type

[**ApprovalRule**](ApprovalRule.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save**
> ApprovalRule save(buyer_id, approval_rule_id, approval_rule)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ApprovalRuleApi = OrderCloud.ApprovalRuleApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
approval_rule_id = 'approval_rule_id_example' # str | ID of the approval rule.
approval_rule = OrderCloud.ApprovalRule() # ApprovalRule | 

try: 
    response = ApprovalRuleApi.save(buyer_id, approval_rule_id, approval_rule)
    print(response)
except ApiException as e:
    print("Exception when calling ApprovalRuleApi->save: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **approval_rule_id** | **str**| ID of the approval rule. | 
 **approval_rule** | [**ApprovalRule**](ApprovalRule.md)|  | 

### Return type

[**ApprovalRule**](ApprovalRule.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

