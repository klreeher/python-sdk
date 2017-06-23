# OrderCloud.MessageSendersApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**messagesenders_assignments_get**](MessageSendersApi.md#messagesenders_assignments_get) | **GET** /messagesenders/assignments | 
[**messagesenders_assignments_post**](MessageSendersApi.md#messagesenders_assignments_post) | **POST** /messagesenders/assignments | 
[**messagesenders_cc_listener_assignments_get**](MessageSendersApi.md#messagesenders_cc_listener_assignments_get) | **GET** /messagesenders/CCListenerAssignments | 
[**messagesenders_cc_listener_assignments_post**](MessageSendersApi.md#messagesenders_cc_listener_assignments_post) | **POST** /messagesenders/CCListenerAssignments | 
[**messagesenders_get**](MessageSendersApi.md#messagesenders_get) | **GET** /messagesenders | 
[**messagesenders_message_sender_id_assignments_delete**](MessageSendersApi.md#messagesenders_message_sender_id_assignments_delete) | **DELETE** /messagesenders/{messageSenderID}/assignments | 
[**messagesenders_message_sender_id_get**](MessageSendersApi.md#messagesenders_message_sender_id_get) | **GET** /messagesenders/{messageSenderID} | 


# **messagesenders_assignments_get**
> ListMessageSenderAssignment messagesenders_assignments_get(buyer_id=buyer_id, message_sender_id=message_sender_id, user_id=user_id, user_group_id=user_group_id, level=level, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MessageSendersApi = OrderCloud.MessageSendersApi
buyer_id = 'buyer_id_example' # str | ID of the buyer. (optional)
message_sender_id = 'message_sender_id_example' # str | ID of the message sender. (optional)
user_id = 'user_id_example' # str | ID of the user. (optional)
user_group_id = 'user_group_id_example' # str | ID of the user group. (optional)
level = 'level_example' # str | Level of the message sender. (optional)
page = 56 # int | Page of the message sender. (optional)
page_size = 56 # int | Page size of the message sender. (optional)

try: 
    response = MessageSendersApi.messagesenders_assignments_get(buyer_id=buyer_id, message_sender_id=message_sender_id, user_id=user_id, user_group_id=user_group_id, level=level, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling MessageSendersApi->messagesenders_assignments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | [optional] 
 **message_sender_id** | **str**| ID of the message sender. | [optional] 
 **user_id** | **str**| ID of the user. | [optional] 
 **user_group_id** | **str**| ID of the user group. | [optional] 
 **level** | **str**| Level of the message sender. | [optional] 
 **page** | **int**| Page of the message sender. | [optional] 
 **page_size** | **int**| Page size of the message sender. | [optional] 

### Return type

[**ListMessageSenderAssignment**](ListMessageSenderAssignment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messagesenders_assignments_post**
> messagesenders_assignments_post(assignment)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MessageSendersApi = OrderCloud.MessageSendersApi
assignment = OrderCloud.MessageSenderAssignment() # MessageSenderAssignment | 

try: 
    MessageSendersApi.messagesenders_assignments_post(assignment)
except ApiException as e:
    print("Exception when calling MessageSendersApi->messagesenders_assignments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment** | [**MessageSenderAssignment**](MessageSenderAssignment.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messagesenders_cc_listener_assignments_get**
> ListMessageCCListenerAssignment messagesenders_cc_listener_assignments_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MessageSendersApi = OrderCloud.MessageSendersApi
search = 'search_example' # str | Search of the message sender. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the message sender. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the message sender. (optional)
page = 56 # int | Page of the message sender. (optional)
page_size = 56 # int | Page size of the message sender. (optional)

try: 
    response = MessageSendersApi.messagesenders_cc_listener_assignments_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling MessageSendersApi->messagesenders_cc_listener_assignments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search of the message sender. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the message sender. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the message sender. | [optional] 
 **page** | **int**| Page of the message sender. | [optional] 
 **page_size** | **int**| Page size of the message sender. | [optional] 

### Return type

[**ListMessageCCListenerAssignment**](ListMessageCCListenerAssignment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messagesenders_cc_listener_assignments_post**
> messagesenders_cc_listener_assignments_post(assignment)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MessageSendersApi = OrderCloud.MessageSendersApi
assignment = OrderCloud.MessageCCListenerAssignment() # MessageCCListenerAssignment | 

try: 
    MessageSendersApi.messagesenders_cc_listener_assignments_post(assignment)
except ApiException as e:
    print("Exception when calling MessageSendersApi->messagesenders_cc_listener_assignments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment** | [**MessageCCListenerAssignment**](MessageCCListenerAssignment.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messagesenders_get**
> ListMessageSender messagesenders_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MessageSendersApi = OrderCloud.MessageSendersApi
search = 'search_example' # str | Search of the message sender. (optional)
search_on = ['search_on_example'] # list[str] | Search on of the message sender. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort by of the message sender. (optional)
page = 56 # int | Page of the message sender. (optional)
page_size = 56 # int | Page size of the message sender. (optional)

try: 
    response = MessageSendersApi.messagesenders_get(search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling MessageSendersApi->messagesenders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search of the message sender. | [optional] 
 **search_on** | [**list[str]**](str.md)| Search on of the message sender. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort by of the message sender. | [optional] 
 **page** | **int**| Page of the message sender. | [optional] 
 **page_size** | **int**| Page size of the message sender. | [optional] 

### Return type

[**ListMessageSender**](ListMessageSender.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messagesenders_message_sender_id_assignments_delete**
> messagesenders_message_sender_id_assignments_delete(message_sender_id, buyer_id=buyer_id, user_id=user_id, user_group_id=user_group_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MessageSendersApi = OrderCloud.MessageSendersApi
message_sender_id = 'message_sender_id_example' # str | ID of the message sender.
buyer_id = 'buyer_id_example' # str | ID of the buyer. (optional)
user_id = 'user_id_example' # str | ID of the user. (optional)
user_group_id = 'user_group_id_example' # str | ID of the user group. (optional)

try: 
    MessageSendersApi.messagesenders_message_sender_id_assignments_delete(message_sender_id, buyer_id=buyer_id, user_id=user_id, user_group_id=user_group_id)
except ApiException as e:
    print("Exception when calling MessageSendersApi->messagesenders_message_sender_id_assignments_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_sender_id** | **str**| ID of the message sender. | 
 **buyer_id** | **str**| ID of the buyer. | [optional] 
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

# **messagesenders_message_sender_id_get**
> MessageSender messagesenders_message_sender_id_get(message_sender_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
MessageSendersApi = OrderCloud.MessageSendersApi
message_sender_id = 'message_sender_id_example' # str | ID of the message sender.

try: 
    response = MessageSendersApi.messagesenders_message_sender_id_get(message_sender_id)
    print(response)
except ApiException as e:
    print("Exception when calling MessageSendersApi->messagesenders_message_sender_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_sender_id** | **str**| ID of the message sender. | 

### Return type

[**MessageSender**](MessageSender.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

