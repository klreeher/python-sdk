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

import os
import sys
import unittest

import OrderCloud
from OrderCloud.rest import ApiException
from OrderCloud.apis.me_api import MeApi


class TestMeApi(unittest.TestCase):
    """ MeApi unit test stubs """

    def setUp(self):
        self.api = OrderCloud.apis.me_api.MeApi()

    def tearDown(self):
        pass

    def test_create_address(self):
        """
        Test case for create_address

        
        """
        pass

    def test_create_credit_card(self):
        """
        Test case for create_credit_card

        
        """
        pass

    def test_delete_address(self):
        """
        Test case for delete_address

        
        """
        pass

    def test_delete_credit_card(self):
        """
        Test case for delete_credit_card

        
        """
        pass

    def test_get(self):
        """
        Test case for get

        
        """
        pass

    def test_get_address(self):
        """
        Test case for get_address

        
        """
        pass

    def test_get_catalog(self):
        """
        Test case for get_catalog

        
        """
        pass

    def test_get_credit_card(self):
        """
        Test case for get_credit_card

        
        """
        pass

    def test_get_product(self):
        """
        Test case for get_product

        
        """
        pass

    def test_get_promotion(self):
        """
        Test case for get_promotion

        
        """
        pass

    def test_get_shipment(self):
        """
        Test case for get_shipment

        
        """
        pass

    def test_get_spec(self):
        """
        Test case for get_spec

        
        """
        pass

    def test_get_spending_account(self):
        """
        Test case for get_spending_account

        
        """
        pass

    def test_list_addresses(self):
        """
        Test case for list_addresses

        
        """
        pass

    def test_list_approvable_orders(self):
        """
        Test case for list_approvable_orders

        
        """
        pass

    def test_list_catalogs(self):
        """
        Test case for list_catalogs

        
        """
        pass

    def test_list_categories(self):
        """
        Test case for list_categories

        
        """
        pass

    def test_list_cost_centers(self):
        """
        Test case for list_cost_centers

        
        """
        pass

    def test_list_credit_cards(self):
        """
        Test case for list_credit_cards

        
        """
        pass

    def test_list_orders(self):
        """
        Test case for list_orders

        
        """
        pass

    def test_list_products(self):
        """
        Test case for list_products

        
        """
        pass

    def test_list_promotions(self):
        """
        Test case for list_promotions

        
        """
        pass

    def test_list_shipment_items(self):
        """
        Test case for list_shipment_items

        
        """
        pass

    def test_list_shipments(self):
        """
        Test case for list_shipments

        
        """
        pass

    def test_list_specs(self):
        """
        Test case for list_specs

        
        """
        pass

    def test_list_spending_accounts(self):
        """
        Test case for list_spending_accounts

        
        """
        pass

    def test_list_user_groups(self):
        """
        Test case for list_user_groups

        
        """
        pass

    def test_patch(self):
        """
        Test case for patch

        
        """
        pass

    def test_patch_address(self):
        """
        Test case for patch_address

        
        """
        pass

    def test_patch_credit_card(self):
        """
        Test case for patch_credit_card

        
        """
        pass

    def test_register(self):
        """
        Test case for register

        
        """
        pass

    def test_reset_password_by_token(self):
        """
        Test case for reset_password_by_token

        
        """
        pass

    def test_transfer_anon_user_order(self):
        """
        Test case for transfer_anon_user_order

        
        """
        pass

    def test_update(self):
        """
        Test case for update

        
        """
        pass

    def test_update_address(self):
        """
        Test case for update_address

        
        """
        pass

    def test_update_credit_card(self):
        """
        Test case for update_credit_card

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
