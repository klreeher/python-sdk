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
import base64
import urllib3


import requests

import sys
import logging
import json

from six import iteritems
from ..configuration import Configuration
from ..api_client import ApiClient


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

@singleton
class Impersonation(object):
    def start(self, access_token=None):
        config = Configuration()

        if not access_token and not config._impersonateToken:
            raise ValueError("You must provide an access token to use when impersonating. Use the UserApi.get_access_token method.")

        config._impersonating = True;
        config._impersonateToken = access_token;

    def stop(self):
        config = Configuration()
        config._impersonating = False;

@singleton
class Auth(object):
    """
    Auto-generated, custom made by Four51. 
    """
    def __init__(self):
        """
        Constructor
        """
        # Token url to authenticate
        self.tokenurl = "https://auth.ordercloud.io/oauth/token"

    def __body_to_string(self, body):
      # As found on http://codereview.stackexchange.com/questions/7953/flattening-a-dictionary-into-a-string
      return '&'.join("{!s}={!r}".format(key,val) for (key,val) in body.items()) 

    def __base_body_for_auth(self, client_id, grant_type, scopes, client_secret = None):
      body = {
        "client_id" : client_id,
        "grant_type" : grant_type,
        "scope" : "+".join(scopes)
      }

      if client_secret:
        body["client_secret"] = client_secret

      return body

    def _request_access_token(self, config, grant_type):
        
        payload = dict()
        payload["username"] = config.username
        payload['password'] = config.password
        payload['client_id'] = config.client_id
        payload['scope']= config.scopes
        payload['grant_type'] = grant_type


        headers = {'Content-Type': 'application/json'}
        resp =requests.post(self.tokenurl, data= payload, headers=headers)

        if not resp.json():
            raise ValueError("Empty response! Make sure you've set a Default User Context ID in the developer center. This is because the generated access token needs to be associated with some user.")

        data = resp.json()

        return data['access_token']

    #Supports the most common OAuth workflow, where you supply the user and pass and its gets and stores
    #the access token. Optionally supply a client secret for extra security
    def login(self, username, password, client_secret = None):
        config = Configuration()
        
        
        config.username = username
        config.password = password

        config.access_token = self._request_access_token(config, 'password')

    #Supports client_secret login for backend systems, as well as anonymous login with no client_secret
    def authenticate(self, client_secret = None):
        config = Configuration()
        if client_secret:
            config.client_secret = client_secret
       

        config.access_token = self._request_access_token(config, 'client_credentials')
