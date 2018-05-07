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


class PromotionAssignment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, promotion_id=None, buyer_id=None, user_group_id=None):
        """
        PromotionAssignment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'promotion_id': 'str',
            'buyer_id': 'str',
            'user_group_id': 'str'
        }

        self.attribute_map = {
            'promotion_id': 'PromotionID',
            'buyer_id': 'BuyerID',
            'user_group_id': 'UserGroupID'
        }

        self._promotion_id = promotion_id
        self._buyer_id = buyer_id
        self._user_group_id = user_group_id

    @property
    def promotion_id(self):
        """
        Gets the promotion_id of this PromotionAssignment.


        :return: The promotion_id of this PromotionAssignment.
        :rtype: str
        """
        return self._promotion_id

    @promotion_id.setter
    def promotion_id(self, promotion_id):
        """
        Sets the promotion_id of this PromotionAssignment.


        :param promotion_id: The promotion_id of this PromotionAssignment.
        :type: str
        """

        self._promotion_id = promotion_id

    @property
    def buyer_id(self):
        """
        Gets the buyer_id of this PromotionAssignment.


        :return: The buyer_id of this PromotionAssignment.
        :rtype: str
        """
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, buyer_id):
        """
        Sets the buyer_id of this PromotionAssignment.


        :param buyer_id: The buyer_id of this PromotionAssignment.
        :type: str
        """

        self._buyer_id = buyer_id

    @property
    def user_group_id(self):
        """
        Gets the user_group_id of this PromotionAssignment.


        :return: The user_group_id of this PromotionAssignment.
        :rtype: str
        """
        return self._user_group_id

    @user_group_id.setter
    def user_group_id(self, user_group_id):
        """
        Sets the user_group_id of this PromotionAssignment.


        :param user_group_id: The user_group_id of this PromotionAssignment.
        :type: str
        """

        self._user_group_id = user_group_id

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
