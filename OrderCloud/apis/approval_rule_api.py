# coding: utf-8

"""
    OrderCloud

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    Contact: ordercloud@four51.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class ApprovalRuleApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create(self, buyer_id, approval_rule, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create(buyer_id, approval_rule, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str buyer_id: ID of the buyer. (required)
        :param ApprovalRule approval_rule:  (required)
        :return: ApprovalRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_with_http_info(buyer_id, approval_rule, **kwargs)
        else:
            (data) = self.create_with_http_info(buyer_id, approval_rule, **kwargs)
            return data

    def create_with_http_info(self, buyer_id, approval_rule, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_with_http_info(buyer_id, approval_rule, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str buyer_id: ID of the buyer. (required)
        :param ApprovalRule approval_rule:  (required)
        :return: ApprovalRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['buyer_id', 'approval_rule']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'buyer_id' is set
        if ('buyer_id' not in params) or (params['buyer_id'] is None):
            raise ValueError("Missing the required parameter `buyer_id` when calling `create`")
        # verify the required parameter 'approval_rule' is set
        if ('approval_rule' not in params) or (params['approval_rule'] is None):
            raise ValueError("Missing the required parameter `approval_rule` when calling `create`")

        resource_path = '/buyers/{buyerID}/approvalrules'.replace('{format}', 'json')
        path_params = {}
        if 'buyer_id' in params:
            path_params['buyerID'] = params['buyer_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'approval_rule' in params:
            body_params = params['approval_rule']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/plain; charset=utf-8'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ApprovalRule',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def delete(self, buyer_id, approval_rule_id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete(buyer_id, approval_rule_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str buyer_id: ID of the buyer. (required)
        :param str approval_rule_id: ID of the approval rule. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_with_http_info(buyer_id, approval_rule_id, **kwargs)
        else:
            (data) = self.delete_with_http_info(buyer_id, approval_rule_id, **kwargs)
            return data

    def delete_with_http_info(self, buyer_id, approval_rule_id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_with_http_info(buyer_id, approval_rule_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str buyer_id: ID of the buyer. (required)
        :param str approval_rule_id: ID of the approval rule. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['buyer_id', 'approval_rule_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'buyer_id' is set
        if ('buyer_id' not in params) or (params['buyer_id'] is None):
            raise ValueError("Missing the required parameter `buyer_id` when calling `delete`")
        # verify the required parameter 'approval_rule_id' is set
        if ('approval_rule_id' not in params) or (params['approval_rule_id'] is None):
            raise ValueError("Missing the required parameter `approval_rule_id` when calling `delete`")

        resource_path = '/buyers/{buyerID}/approvalrules/{approvalRuleID}'.replace('{format}', 'json')
        path_params = {}
        if 'buyer_id' in params:
            path_params['buyerID'] = params['buyer_id']
        if 'approval_rule_id' in params:
            path_params['approvalRuleID'] = params['approval_rule_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/plain; charset=utf-8'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get(self, buyer_id, approval_rule_id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get(buyer_id, approval_rule_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str buyer_id: ID of the buyer. (required)
        :param str approval_rule_id: ID of the approval rule. (required)
        :return: ApprovalRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_with_http_info(buyer_id, approval_rule_id, **kwargs)
        else:
            (data) = self.get_with_http_info(buyer_id, approval_rule_id, **kwargs)
            return data

    def get_with_http_info(self, buyer_id, approval_rule_id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_with_http_info(buyer_id, approval_rule_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str buyer_id: ID of the buyer. (required)
        :param str approval_rule_id: ID of the approval rule. (required)
        :return: ApprovalRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['buyer_id', 'approval_rule_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'buyer_id' is set
        if ('buyer_id' not in params) or (params['buyer_id'] is None):
            raise ValueError("Missing the required parameter `buyer_id` when calling `get`")
        # verify the required parameter 'approval_rule_id' is set
        if ('approval_rule_id' not in params) or (params['approval_rule_id'] is None):
            raise ValueError("Missing the required parameter `approval_rule_id` when calling `get`")

        resource_path = '/buyers/{buyerID}/approvalrules/{approvalRuleID}'.replace('{format}', 'json')
        path_params = {}
        if 'buyer_id' in params:
            path_params['buyerID'] = params['buyer_id']
        if 'approval_rule_id' in params:
            path_params['approvalRuleID'] = params['approval_rule_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/plain; charset=utf-8'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ApprovalRule',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def list(self, buyer_id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list(buyer_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str buyer_id: ID of the buyer. (required)
        :param str search: Word or phrase to search for.
        :param str search_on: Comma-delimited list of fields to search on.
        :param str sort_by: Comma-delimited list of fields to sort by.
        :param int page: Page of results to return. Default: 1
        :param int page_size: Number of results to return per page. Default: 20, max: 100.
        :param dict(str, str) filters: Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???'
        :return: ListApprovalRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_with_http_info(buyer_id, **kwargs)
        else:
            (data) = self.list_with_http_info(buyer_id, **kwargs)
            return data

    def list_with_http_info(self, buyer_id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_with_http_info(buyer_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str buyer_id: ID of the buyer. (required)
        :param str search: Word or phrase to search for.
        :param str search_on: Comma-delimited list of fields to search on.
        :param str sort_by: Comma-delimited list of fields to sort by.
        :param int page: Page of results to return. Default: 1
        :param int page_size: Number of results to return per page. Default: 20, max: 100.
        :param dict(str, str) filters: Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???'
        :return: ListApprovalRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['buyer_id', 'search', 'search_on', 'sort_by', 'page', 'page_size', 'filters']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'buyer_id' is set
        if ('buyer_id' not in params) or (params['buyer_id'] is None):
            raise ValueError("Missing the required parameter `buyer_id` when calling `list`")

        resource_path = '/buyers/{buyerID}/approvalrules'.replace('{format}', 'json')
        path_params = {}
        if 'buyer_id' in params:
            path_params['buyerID'] = params['buyer_id']

        query_params = {}
        if 'search' in params:
            query_params['search'] = params['search']
        if 'search_on' in params:
            query_params['searchOn'] = params['search_on']
        if 'sort_by' in params:
            query_params['sortBy'] = params['sort_by']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'filters' in params:
            query_params['filters'] = params['filters']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/plain; charset=utf-8'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ListApprovalRule',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def patch(self, buyer_id, approval_rule_id, partial_approval_rule, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch(buyer_id, approval_rule_id, partial_approval_rule, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str buyer_id: ID of the buyer. (required)
        :param str approval_rule_id: ID of the approval rule. (required)
        :param ApprovalRule partial_approval_rule:  (required)
        :return: ApprovalRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.patch_with_http_info(buyer_id, approval_rule_id, partial_approval_rule, **kwargs)
        else:
            (data) = self.patch_with_http_info(buyer_id, approval_rule_id, partial_approval_rule, **kwargs)
            return data

    def patch_with_http_info(self, buyer_id, approval_rule_id, partial_approval_rule, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_with_http_info(buyer_id, approval_rule_id, partial_approval_rule, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str buyer_id: ID of the buyer. (required)
        :param str approval_rule_id: ID of the approval rule. (required)
        :param ApprovalRule partial_approval_rule:  (required)
        :return: ApprovalRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['buyer_id', 'approval_rule_id', 'partial_approval_rule']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'buyer_id' is set
        if ('buyer_id' not in params) or (params['buyer_id'] is None):
            raise ValueError("Missing the required parameter `buyer_id` when calling `patch`")
        # verify the required parameter 'approval_rule_id' is set
        if ('approval_rule_id' not in params) or (params['approval_rule_id'] is None):
            raise ValueError("Missing the required parameter `approval_rule_id` when calling `patch`")
        # verify the required parameter 'partial_approval_rule' is set
        if ('partial_approval_rule' not in params) or (params['partial_approval_rule'] is None):
            raise ValueError("Missing the required parameter `partial_approval_rule` when calling `patch`")

        resource_path = '/buyers/{buyerID}/approvalrules/{approvalRuleID}'.replace('{format}', 'json')
        path_params = {}
        if 'buyer_id' in params:
            path_params['buyerID'] = params['buyer_id']
        if 'approval_rule_id' in params:
            path_params['approvalRuleID'] = params['approval_rule_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'partial_approval_rule' in params:
            body_params = params['partial_approval_rule']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/plain; charset=utf-8'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ApprovalRule',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def save(self, buyer_id, approval_rule_id, approval_rule, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.save(buyer_id, approval_rule_id, approval_rule, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str buyer_id: ID of the buyer. (required)
        :param str approval_rule_id: ID of the approval rule. (required)
        :param ApprovalRule approval_rule:  (required)
        :return: ApprovalRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.save_with_http_info(buyer_id, approval_rule_id, approval_rule, **kwargs)
        else:
            (data) = self.save_with_http_info(buyer_id, approval_rule_id, approval_rule, **kwargs)
            return data

    def save_with_http_info(self, buyer_id, approval_rule_id, approval_rule, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.save_with_http_info(buyer_id, approval_rule_id, approval_rule, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str buyer_id: ID of the buyer. (required)
        :param str approval_rule_id: ID of the approval rule. (required)
        :param ApprovalRule approval_rule:  (required)
        :return: ApprovalRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['buyer_id', 'approval_rule_id', 'approval_rule']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'buyer_id' is set
        if ('buyer_id' not in params) or (params['buyer_id'] is None):
            raise ValueError("Missing the required parameter `buyer_id` when calling `save`")
        # verify the required parameter 'approval_rule_id' is set
        if ('approval_rule_id' not in params) or (params['approval_rule_id'] is None):
            raise ValueError("Missing the required parameter `approval_rule_id` when calling `save`")
        # verify the required parameter 'approval_rule' is set
        if ('approval_rule' not in params) or (params['approval_rule'] is None):
            raise ValueError("Missing the required parameter `approval_rule` when calling `save`")

        resource_path = '/buyers/{buyerID}/approvalrules/{approvalRuleID}'.replace('{format}', 'json')
        path_params = {}
        if 'buyer_id' in params:
            path_params['buyerID'] = params['buyer_id']
        if 'approval_rule_id' in params:
            path_params['approvalRuleID'] = params['approval_rule_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'approval_rule' in params:
            body_params = params['approval_rule']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/plain; charset=utf-8'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ApprovalRule',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
