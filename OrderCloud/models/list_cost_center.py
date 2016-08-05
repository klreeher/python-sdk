# coding: utf-8

"""
    OrderCloud

    A full ecommerce backend as a service.

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


class ListCostCenter(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, items=None, meta=None):
        """
        ListCostCenter - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'items': 'list[CostCenter]',
            'meta': 'Meta'
        }

        self.attribute_map = {
            'items': 'Items',
            'meta': 'Meta'
        }

        self._items = items
        self._meta = meta

    @property
    def items(self):
        """
        Gets the items of this ListCostCenter.


        :return: The items of this ListCostCenter.
        :rtype: list[CostCenter]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this ListCostCenter.


        :param items: The items of this ListCostCenter.
        :type: list[CostCenter]
        """

        self._items = items

    @property
    def meta(self):
        """
        Gets the meta of this ListCostCenter.


        :return: The meta of this ListCostCenter.
        :rtype: Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """
        Sets the meta of this ListCostCenter.


        :param meta: The meta of this ListCostCenter.
        :type: Meta
        """

        self._meta = meta

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
