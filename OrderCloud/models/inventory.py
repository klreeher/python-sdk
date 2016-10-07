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


class Inventory(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, available=None, reserved=None, last_updated=None):
        """
        Inventory - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'available': 'int',
            'reserved': 'int',
            'last_updated': 'str'
        }

        self.attribute_map = {
            'id': 'ID',
            'name': 'Name',
            'available': 'Available',
            'reserved': 'Reserved',
            'last_updated': 'LastUpdated'
        }

        self._id = id
        self._name = name
        self._available = available
        self._reserved = reserved
        self._last_updated = last_updated

    @property
    def id(self):
        """
        Gets the id of this Inventory.


        :return: The id of this Inventory.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Inventory.


        :param id: The id of this Inventory.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Inventory.


        :return: The name of this Inventory.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Inventory.


        :param name: The name of this Inventory.
        :type: str
        """

        self._name = name

    @property
    def available(self):
        """
        Gets the available of this Inventory.


        :return: The available of this Inventory.
        :rtype: int
        """
        return self._available

    @available.setter
    def available(self, available):
        """
        Sets the available of this Inventory.


        :param available: The available of this Inventory.
        :type: int
        """

        self._available = available

    @property
    def reserved(self):
        """
        Gets the reserved of this Inventory.


        :return: The reserved of this Inventory.
        :rtype: int
        """
        return self._reserved

    @reserved.setter
    def reserved(self, reserved):
        """
        Sets the reserved of this Inventory.


        :param reserved: The reserved of this Inventory.
        :type: int
        """

        self._reserved = reserved

    @property
    def last_updated(self):
        """
        Gets the last_updated of this Inventory.


        :return: The last_updated of this Inventory.
        :rtype: str
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """
        Sets the last_updated of this Inventory.


        :param last_updated: The last_updated of this Inventory.
        :type: str
        """

        self._last_updated = last_updated

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
