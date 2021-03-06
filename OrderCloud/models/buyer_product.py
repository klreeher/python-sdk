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

from pprint import pformat
from six import iteritems
import re


class BuyerProduct(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, price_schedule=None, id=None, name=None, description=None, quantity_multiplier=None, ship_weight=None, ship_height=None, ship_width=None, ship_length=None, active=None, spec_count=None, xp=None, variant_count=None, ship_from_address_id=None, inventory=None, auto_forward_supplier_id=None):
        """
        BuyerProduct - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'price_schedule': 'PriceSchedule',
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'quantity_multiplier': 'int',
            'ship_weight': 'float',
            'ship_height': 'float',
            'ship_width': 'float',
            'ship_length': 'float',
            'active': 'bool',
            'spec_count': 'int',
            'xp': 'object',
            'variant_count': 'int',
            'ship_from_address_id': 'str',
            'inventory': 'Inventory',
            'auto_forward_supplier_id': 'str'
        }

        self.attribute_map = {
            'price_schedule': 'PriceSchedule',
            'id': 'ID',
            'name': 'Name',
            'description': 'Description',
            'quantity_multiplier': 'QuantityMultiplier',
            'ship_weight': 'ShipWeight',
            'ship_height': 'ShipHeight',
            'ship_width': 'ShipWidth',
            'ship_length': 'ShipLength',
            'active': 'Active',
            'spec_count': 'SpecCount',
            'xp': 'xp',
            'variant_count': 'VariantCount',
            'ship_from_address_id': 'ShipFromAddressID',
            'inventory': 'Inventory',
            'auto_forward_supplier_id': 'AutoForwardSupplierID'
        }

        self._price_schedule = price_schedule
        self._id = id
        self._name = name
        self._description = description
        self._quantity_multiplier = quantity_multiplier
        self._ship_weight = ship_weight
        self._ship_height = ship_height
        self._ship_width = ship_width
        self._ship_length = ship_length
        self._active = active
        self._spec_count = spec_count
        self._xp = xp
        self._variant_count = variant_count
        self._ship_from_address_id = ship_from_address_id
        self._inventory = inventory
        self._auto_forward_supplier_id = auto_forward_supplier_id

    @property
    def price_schedule(self):
        """
        Gets the price_schedule of this BuyerProduct.


        :return: The price_schedule of this BuyerProduct.
        :rtype: PriceSchedule
        """
        return self._price_schedule

    @price_schedule.setter
    def price_schedule(self, price_schedule):
        """
        Sets the price_schedule of this BuyerProduct.


        :param price_schedule: The price_schedule of this BuyerProduct.
        :type: PriceSchedule
        """

        self._price_schedule = price_schedule

    @property
    def id(self):
        """
        Gets the id of this BuyerProduct.


        :return: The id of this BuyerProduct.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BuyerProduct.


        :param id: The id of this BuyerProduct.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this BuyerProduct.


        :return: The name of this BuyerProduct.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BuyerProduct.


        :param name: The name of this BuyerProduct.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this BuyerProduct.


        :return: The description of this BuyerProduct.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this BuyerProduct.


        :param description: The description of this BuyerProduct.
        :type: str
        """

        self._description = description

    @property
    def quantity_multiplier(self):
        """
        Gets the quantity_multiplier of this BuyerProduct.


        :return: The quantity_multiplier of this BuyerProduct.
        :rtype: int
        """
        return self._quantity_multiplier

    @quantity_multiplier.setter
    def quantity_multiplier(self, quantity_multiplier):
        """
        Sets the quantity_multiplier of this BuyerProduct.


        :param quantity_multiplier: The quantity_multiplier of this BuyerProduct.
        :type: int
        """

        self._quantity_multiplier = quantity_multiplier

    @property
    def ship_weight(self):
        """
        Gets the ship_weight of this BuyerProduct.


        :return: The ship_weight of this BuyerProduct.
        :rtype: float
        """
        return self._ship_weight

    @ship_weight.setter
    def ship_weight(self, ship_weight):
        """
        Sets the ship_weight of this BuyerProduct.


        :param ship_weight: The ship_weight of this BuyerProduct.
        :type: float
        """

        self._ship_weight = ship_weight

    @property
    def ship_height(self):
        """
        Gets the ship_height of this BuyerProduct.


        :return: The ship_height of this BuyerProduct.
        :rtype: float
        """
        return self._ship_height

    @ship_height.setter
    def ship_height(self, ship_height):
        """
        Sets the ship_height of this BuyerProduct.


        :param ship_height: The ship_height of this BuyerProduct.
        :type: float
        """

        self._ship_height = ship_height

    @property
    def ship_width(self):
        """
        Gets the ship_width of this BuyerProduct.


        :return: The ship_width of this BuyerProduct.
        :rtype: float
        """
        return self._ship_width

    @ship_width.setter
    def ship_width(self, ship_width):
        """
        Sets the ship_width of this BuyerProduct.


        :param ship_width: The ship_width of this BuyerProduct.
        :type: float
        """

        self._ship_width = ship_width

    @property
    def ship_length(self):
        """
        Gets the ship_length of this BuyerProduct.


        :return: The ship_length of this BuyerProduct.
        :rtype: float
        """
        return self._ship_length

    @ship_length.setter
    def ship_length(self, ship_length):
        """
        Sets the ship_length of this BuyerProduct.


        :param ship_length: The ship_length of this BuyerProduct.
        :type: float
        """

        self._ship_length = ship_length

    @property
    def active(self):
        """
        Gets the active of this BuyerProduct.


        :return: The active of this BuyerProduct.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this BuyerProduct.


        :param active: The active of this BuyerProduct.
        :type: bool
        """

        self._active = active

    @property
    def spec_count(self):
        """
        Gets the spec_count of this BuyerProduct.


        :return: The spec_count of this BuyerProduct.
        :rtype: int
        """
        return self._spec_count

    @spec_count.setter
    def spec_count(self, spec_count):
        """
        Sets the spec_count of this BuyerProduct.


        :param spec_count: The spec_count of this BuyerProduct.
        :type: int
        """

        self._spec_count = spec_count

    @property
    def xp(self):
        """
        Gets the xp of this BuyerProduct.


        :return: The xp of this BuyerProduct.
        :rtype: object
        """
        return self._xp

    @xp.setter
    def xp(self, xp):
        """
        Sets the xp of this BuyerProduct.


        :param xp: The xp of this BuyerProduct.
        :type: object
        """

        self._xp = xp

    @property
    def variant_count(self):
        """
        Gets the variant_count of this BuyerProduct.


        :return: The variant_count of this BuyerProduct.
        :rtype: int
        """
        return self._variant_count

    @variant_count.setter
    def variant_count(self, variant_count):
        """
        Sets the variant_count of this BuyerProduct.


        :param variant_count: The variant_count of this BuyerProduct.
        :type: int
        """

        self._variant_count = variant_count

    @property
    def ship_from_address_id(self):
        """
        Gets the ship_from_address_id of this BuyerProduct.


        :return: The ship_from_address_id of this BuyerProduct.
        :rtype: str
        """
        return self._ship_from_address_id

    @ship_from_address_id.setter
    def ship_from_address_id(self, ship_from_address_id):
        """
        Sets the ship_from_address_id of this BuyerProduct.


        :param ship_from_address_id: The ship_from_address_id of this BuyerProduct.
        :type: str
        """

        self._ship_from_address_id = ship_from_address_id

    @property
    def inventory(self):
        """
        Gets the inventory of this BuyerProduct.


        :return: The inventory of this BuyerProduct.
        :rtype: Inventory
        """
        return self._inventory

    @inventory.setter
    def inventory(self, inventory):
        """
        Sets the inventory of this BuyerProduct.


        :param inventory: The inventory of this BuyerProduct.
        :type: Inventory
        """

        self._inventory = inventory

    @property
    def auto_forward_supplier_id(self):
        """
        Gets the auto_forward_supplier_id of this BuyerProduct.


        :return: The auto_forward_supplier_id of this BuyerProduct.
        :rtype: str
        """
        return self._auto_forward_supplier_id

    @auto_forward_supplier_id.setter
    def auto_forward_supplier_id(self, auto_forward_supplier_id):
        """
        Sets the auto_forward_supplier_id of this BuyerProduct.


        :param auto_forward_supplier_id: The auto_forward_supplier_id of this BuyerProduct.
        :type: str
        """

        self._auto_forward_supplier_id = auto_forward_supplier_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
