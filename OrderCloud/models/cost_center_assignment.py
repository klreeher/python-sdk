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


class CostCenterAssignment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, cost_center_id=None, user_id=None, user_group_id=None):
        """
        CostCenterAssignment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cost_center_id': 'str',
            'user_id': 'str',
            'user_group_id': 'str'
        }

        self.attribute_map = {
            'cost_center_id': 'CostCenterID',
            'user_id': 'UserID',
            'user_group_id': 'UserGroupID'
        }

        self._cost_center_id = cost_center_id
        self._user_id = user_id
        self._user_group_id = user_group_id

    @property
    def cost_center_id(self):
        """
        Gets the cost_center_id of this CostCenterAssignment.


        :return: The cost_center_id of this CostCenterAssignment.
        :rtype: str
        """
        return self._cost_center_id

    @cost_center_id.setter
    def cost_center_id(self, cost_center_id):
        """
        Sets the cost_center_id of this CostCenterAssignment.


        :param cost_center_id: The cost_center_id of this CostCenterAssignment.
        :type: str
        """

        self._cost_center_id = cost_center_id

    @property
    def user_id(self):
        """
        Gets the user_id of this CostCenterAssignment.


        :return: The user_id of this CostCenterAssignment.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this CostCenterAssignment.


        :param user_id: The user_id of this CostCenterAssignment.
        :type: str
        """

        self._user_id = user_id

    @property
    def user_group_id(self):
        """
        Gets the user_group_id of this CostCenterAssignment.


        :return: The user_group_id of this CostCenterAssignment.
        :rtype: str
        """
        return self._user_group_id

    @user_group_id.setter
    def user_group_id(self, user_group_id):
        """
        Sets the user_group_id of this CostCenterAssignment.


        :param user_group_id: The user_group_id of this CostCenterAssignment.
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
