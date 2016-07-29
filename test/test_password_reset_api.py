# coding: utf-8

"""
    OrderCloud

    A full ecommerce backend as a service.

    OpenAPI spec version: 0.1
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

import os
import sys
import unittest

import OrderCloud
from OrderCloud.rest import ApiException
from OrderCloud.apis.password_reset_api import PasswordResetApi


class TestPasswordResetApi(unittest.TestCase):
    """ PasswordResetApi unit test stubs """

    def setUp(self):
        self.api = OrderCloud.apis.password_reset_api.PasswordResetApi()

    def tearDown(self):
        pass

    def test_reset_password(self):
        """
        Test case for reset_password

        
        """
        pass

    def test_send_verification_code(self):
        """
        Test case for send_verification_code

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
