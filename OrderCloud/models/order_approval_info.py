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


class OrderApprovalInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, comments=None, allow_resubmit=None):
        """
        OrderApprovalInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'comments': 'str',
            'allow_resubmit': 'bool'
        }

        self.attribute_map = {
            'comments': 'Comments',
            'allow_resubmit': 'AllowResubmit'
        }

        self._comments = comments
        self._allow_resubmit = allow_resubmit

    @property
    def comments(self):
        """
        Gets the comments of this OrderApprovalInfo.


        :return: The comments of this OrderApprovalInfo.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this OrderApprovalInfo.


        :param comments: The comments of this OrderApprovalInfo.
        :type: str
        """

        self._comments = comments

    @property
    def allow_resubmit(self):
        """
        Gets the allow_resubmit of this OrderApprovalInfo.


        :return: The allow_resubmit of this OrderApprovalInfo.
        :rtype: bool
        """
        return self._allow_resubmit

    @allow_resubmit.setter
    def allow_resubmit(self, allow_resubmit):
        """
        Sets the allow_resubmit of this OrderApprovalInfo.


        :param allow_resubmit: The allow_resubmit of this OrderApprovalInfo.
        :type: bool
        """

        self._allow_resubmit = allow_resubmit

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
