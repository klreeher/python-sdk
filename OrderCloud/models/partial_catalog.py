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


class PartialCatalog(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, description=None, active=None, category_count=None, xp=None):
        """
        PartialCatalog - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'active': 'bool',
            'category_count': 'int',
            'xp': 'object'
        }

        self.attribute_map = {
            'id': 'ID',
            'name': 'Name',
            'description': 'Description',
            'active': 'Active',
            'category_count': 'CategoryCount',
            'xp': 'xp'
        }

        self._id = id
        self._name = name
        self._description = description
        self._active = active
        self._category_count = category_count
        self._xp = xp

    @property
    def id(self):
        """
        Gets the id of this PartialCatalog.


        :return: The id of this PartialCatalog.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PartialCatalog.


        :param id: The id of this PartialCatalog.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this PartialCatalog.


        :return: The name of this PartialCatalog.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PartialCatalog.


        :param name: The name of this PartialCatalog.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this PartialCatalog.


        :return: The description of this PartialCatalog.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PartialCatalog.


        :param description: The description of this PartialCatalog.
        :type: str
        """

        self._description = description

    @property
    def active(self):
        """
        Gets the active of this PartialCatalog.


        :return: The active of this PartialCatalog.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this PartialCatalog.


        :param active: The active of this PartialCatalog.
        :type: bool
        """

        self._active = active

    @property
    def category_count(self):
        """
        Gets the category_count of this PartialCatalog.


        :return: The category_count of this PartialCatalog.
        :rtype: int
        """
        return self._category_count

    @category_count.setter
    def category_count(self, category_count):
        """
        Sets the category_count of this PartialCatalog.


        :param category_count: The category_count of this PartialCatalog.
        :type: int
        """

        self._category_count = category_count

    @property
    def xp(self):
        """
        Gets the xp of this PartialCatalog.


        :return: The xp of this PartialCatalog.
        :rtype: object
        """
        return self._xp

    @xp.setter
    def xp(self, xp):
        """
        Sets the xp of this PartialCatalog.


        :param xp: The xp of this PartialCatalog.
        :type: object
        """

        self._xp = xp

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
