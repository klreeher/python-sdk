# OrderCloud.ApprovalRuleApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buyers_buyer_id_approvalrules_approval_rule_id_delete**](ApprovalRuleApi.md#buyers_buyer_id_approvalrules_approval_rule_id_delete) | **DELETE** /buyers/{buyerID}/approvalrules/{approvalRuleID} | 
[**buyers_buyer_id_approvalrules_approval_rule_id_get**](ApprovalRuleApi.md#buyers_buyer_id_approvalrules_approval_rule_id_get) | **GET** /buyers/{buyerID}/approvalrules/{approvalRuleID} | 
[**buyers_buyer_id_approvalrules_approval_rule_id_patch**](ApprovalRuleApi.md#buyers_buyer_id_approvalrules_approval_rule_id_patch) | **PATCH** /buyers/{buyerID}/approvalrules/{approvalRuleID} | 
[**buyers_buyer_id_approvalrules_approval_rule_id_put**](ApprovalRuleApi.md#buyers_buyer_id_approvalrules_approval_rule_id_put) | **PUT** /buyers/{buyerID}/approvalrules/{approvalRuleID} | 
[**buyers_buyer_id_approvalrules_get**](ApprovalRuleApi.md#buyers_buyer_id_approvalrules_get) | **GET** /buyers/{buyerID}/approvalrules | 
[**buyers_buyer_id_approvalrules_post**](ApprovalRuleApi.md#buyers_buyer_id_approvalrules_post) | **POST** /buyers/{buyerID}/approvalrules | 


# **buyers_buyer_id_approvalrules_approval_rule_id_delete**
> buyers_buyer_id_approvalrules_approval_rule_id_delete(buyer_id, approval_rule_id)



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
    ApprovalRuleApi.buyers_buyer_id_approvalrules_approval_rule_id_delete(buyer_id, approval_rule_id)
except ApiException as e:
    print("Exception when calling ApprovalRuleApi->buyers_buyer_id_approvalrules_approval_rule_id_delete: %s\n" % e)
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

# **buyers_buyer_id_approvalrules_approval_rule_id_get**
> ApprovalRule buyers_buyer_id_approvalrules_approval_rule_id_get(buyer_id, approval_rule_id)



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
    response = ApprovalRuleApi.buyers_buyer_id_approvalrules_approval_rule_id_get(buyer_id, approval_rule_id)
    print(response)
except ApiException as e:
    print("Exception when calling ApprovalRuleApi->buyers_buyer_id_approvalrules_approval_rule_id_get: %s\n" % e)
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

# **buyers_buyer_id_approvalrules_approval_rule_id_patch**
> ApprovalRule buyers_buyer_id_approvalrules_approval_rule_id_patch(buyer_id, approval_rule_id, partial_approval_rule)



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
    response = ApprovalRuleApi.buyers_buyer_id_approvalrules_approval_rule_id_patch(buyer_id, approval_rule_id, partial_approval_rule)
    print(response)
except ApiException as e:
    print("Exception when calling ApprovalRuleApi->buyers_buyer_id_approvalrules_approval_rule_id_patch: %s\n" % e)
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

# **buyers_buyer_id_approvalrules_approval_rule_id_put**
> ApprovalRule buyers_buyer_id_approvalrules_approval_rule_id_put(buyer_id, approval_rule_id, approval_rule)



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
    response = ApprovalRuleApi.buyers_buyer_id_approvalrules_approval_rule_id_put(buyer_id, approval_rule_id, approval_rule)
    print(response)
except ApiException as e:
    print("Exception when calling ApprovalRuleApi->buyers_buyer_id_approvalrules_approval_rule_id_put: %s\n" % e)
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

# **buyers_buyer_id_approvalrules_get**
> ListApprovalRule buyers_buyer_id_approvalrules_get(buyer_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
ApprovalRuleApi = OrderCloud.ApprovalRuleApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
search = 'search_example' # str | Search of the approval rule. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the approval rule. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the approval rule. (optional)
page = 56 # int | Page of the approval rule. (optional)
page_size = 56 # int | Page size of the approval rule. (optional)

try: 
    response = ApprovalRuleApi.buyers_buyer_id_approvalrules_get(buyer_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling ApprovalRuleApi->buyers_buyer_id_approvalrules_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **search** | **str**| Search of the approval rule. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the approval rule. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the approval rule. | [optional] 
 **page** | **int**| Page of the approval rule. | [optional] 
 **page_size** | **int**| Page size of the approval rule. | [optional] 

### Return type

[**ListApprovalRule**](ListApprovalRule.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buyers_buyer_id_approvalrules_post**
> ApprovalRule buyers_buyer_id_approvalrules_post(buyer_id, approval_rule)



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
    response = ApprovalRuleApi.buyers_buyer_id_approvalrules_post(buyer_id, approval_rule)
    print(response)
except ApiException as e:
    print("Exception when calling ApprovalRuleApi->buyers_buyer_id_approvalrules_post: %s\n" % e)
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

