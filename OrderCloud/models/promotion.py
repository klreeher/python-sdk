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

from pprint import pformat
from six import iteritems
import re


class Promotion(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, code=None, name=None, usages_remaining=None, description=None, fine_print=None, start_date=None, expiration_date=None, eligible_expression=None, value_expression=None, can_combine=None, xp=None):
        """
        Promotion - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'code': 'str',
            'name': 'str',
            'usages_remaining': 'int',
            'description': 'str',
            'fine_print': 'str',
            'start_date': 'date',
            'expiration_date': 'date',
            'eligible_expression': 'str',
            'value_expression': 'str',
            'can_combine': 'bool',
            'xp': 'object'
        }

        self.attribute_map = {
            'id': 'ID',
            'code': 'Code',
            'name': 'Name',
            'usages_remaining': 'UsagesRemaining',
            'description': 'Description',
            'fine_print': 'FinePrint',
            'start_date': 'StartDate',
            'expiration_date': 'ExpirationDate',
            'eligible_expression': 'EligibleExpression',
            'value_expression': 'ValueExpression',
            'can_combine': 'CanCombine',
            'xp': 'xp'
        }

        self._id = id
        self._code = code
        self._name = name
        self._usages_remaining = usages_remaining
        self._description = description
        self._fine_print = fine_print
        self._start_date = start_date
        self._expiration_date = expiration_date
        self._eligible_expression = eligible_expression
        self._value_expression = value_expression
        self._can_combine = can_combine
        self._xp = xp

    @property
    def id(self):
        """
        Gets the id of this Promotion.


        :return: The id of this Promotion.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Promotion.


        :param id: The id of this Promotion.
        :type: str
        """

        self._id = id

    @property
    def code(self):
        """
        Gets the code of this Promotion.


        :return: The code of this Promotion.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this Promotion.


        :param code: The code of this Promotion.
        :type: str
        """

        self._code = code

    @property
    def name(self):
        """
        Gets the name of this Promotion.


        :return: The name of this Promotion.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Promotion.


        :param name: The name of this Promotion.
        :type: str
        """

        self._name = name

    @property
    def usages_remaining(self):
        """
        Gets the usages_remaining of this Promotion.


        :return: The usages_remaining of this Promotion.
        :rtype: int
        """
        return self._usages_remaining

    @usages_remaining.setter
    def usages_remaining(self, usages_remaining):
        """
        Sets the usages_remaining of this Promotion.


        :param usages_remaining: The usages_remaining of this Promotion.
        :type: int
        """

        self._usages_remaining = usages_remaining

    @property
    def description(self):
        """
        Gets the description of this Promotion.


        :return: The description of this Promotion.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Promotion.


        :param description: The description of this Promotion.
        :type: str
        """

        self._description = description

    @property
    def fine_print(self):
        """
        Gets the fine_print of this Promotion.


        :return: The fine_print of this Promotion.
        :rtype: str
        """
        return self._fine_print

    @fine_print.setter
    def fine_print(self, fine_print):
        """
        Sets the fine_print of this Promotion.


        :param fine_print: The fine_print of this Promotion.
        :type: str
        """

        self._fine_print = fine_print

    @property
    def start_date(self):
        """
        Gets the start_date of this Promotion.


        :return: The start_date of this Promotion.
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this Promotion.


        :param start_date: The start_date of this Promotion.
        :type: date
        """

        self._start_date = start_date

    @property
    def expiration_date(self):
        """
        Gets the expiration_date of this Promotion.


        :return: The expiration_date of this Promotion.
        :rtype: date
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """
        Sets the expiration_date of this Promotion.


        :param expiration_date: The expiration_date of this Promotion.
        :type: date
        """

        self._expiration_date = expiration_date

    @property
    def eligible_expression(self):
        """
        Gets the eligible_expression of this Promotion.


        :return: The eligible_expression of this Promotion.
        :rtype: str
        """
        return self._eligible_expression

    @eligible_expression.setter
    def eligible_expression(self, eligible_expression):
        """
        Sets the eligible_expression of this Promotion.


        :param eligible_expression: The eligible_expression of this Promotion.
        :type: str
        """

        self._eligible_expression = eligible_expression

    @property
    def value_expression(self):
        """
        Gets the value_expression of this Promotion.


        :return: The value_expression of this Promotion.
        :rtype: str
        """
        return self._value_expression

    @value_expression.setter
    def value_expression(self, value_expression):
        """
        Sets the value_expression of this Promotion.


        :param value_expression: The value_expression of this Promotion.
        :type: str
        """

        self._value_expression = value_expression

    @property
    def can_combine(self):
        """
        Gets the can_combine of this Promotion.


        :return: The can_combine of this Promotion.
        :rtype: bool
        """
        return self._can_combine

    @can_combine.setter
    def can_combine(self, can_combine):
        """
        Sets the can_combine of this Promotion.


        :param can_combine: The can_combine of this Promotion.
        :type: bool
        """

        self._can_combine = can_combine

    @property
    def xp(self):
        """
        Gets the xp of this Promotion.


        :return: The xp of this Promotion.
        :rtype: object
        """
        return self._xp

    @xp.setter
    def xp(self, xp):
        """
        Sets the xp of this Promotion.


        :param xp: The xp of this Promotion.
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
