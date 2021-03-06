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


class PasswordResetApi(object):
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

    def reset_password_by_verification_code(self, verification_code, password_reset, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.reset_password_by_verification_code(verification_code, password_reset, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str verification_code: Verification code of the password reset. (required)
        :param PasswordReset password_reset:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.reset_password_by_verification_code_with_http_info(verification_code, password_reset, **kwargs)
        else:
            (data) = self.reset_password_by_verification_code_with_http_info(verification_code, password_reset, **kwargs)
            return data

    def reset_password_by_verification_code_with_http_info(self, verification_code, password_reset, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.reset_password_by_verification_code_with_http_info(verification_code, password_reset, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str verification_code: Verification code of the password reset. (required)
        :param PasswordReset password_reset:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['verification_code', 'password_reset']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reset_password_by_verification_code" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'verification_code' is set
        if ('verification_code' not in params) or (params['verification_code'] is None):
            raise ValueError("Missing the required parameter `verification_code` when calling `reset_password_by_verification_code`")
        # verify the required parameter 'password_reset' is set
        if ('password_reset' not in params) or (params['password_reset'] is None):
            raise ValueError("Missing the required parameter `password_reset` when calling `reset_password_by_verification_code`")

        resource_path = '/password/reset/{verificationCode}'.replace('{format}', 'json')
        path_params = {}
        if 'verification_code' in params:
            path_params['verificationCode'] = params['verification_code']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'password_reset' in params:
            body_params = params['password_reset']

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
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def send_verification_code(self, password_reset_request, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.send_verification_code(password_reset_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param PasswordResetRequest password_reset_request:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.send_verification_code_with_http_info(password_reset_request, **kwargs)
        else:
            (data) = self.send_verification_code_with_http_info(password_reset_request, **kwargs)
            return data

    def send_verification_code_with_http_info(self, password_reset_request, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.send_verification_code_with_http_info(password_reset_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param PasswordResetRequest password_reset_request:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['password_reset_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_verification_code" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'password_reset_request' is set
        if ('password_reset_request' not in params) or (params['password_reset_request'] is None):
            raise ValueError("Missing the required parameter `password_reset_request` when calling `send_verification_code`")

        resource_path = '/password/reset'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'password_reset_request' in params:
            body_params = params['password_reset_request']

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
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
