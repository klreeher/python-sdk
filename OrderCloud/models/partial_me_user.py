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


class PartialMeUser(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, buyer=None, id=None, username=None, password=None, first_name=None, last_name=None, email=None, phone=None, terms_accepted=None, active=None, xp=None, available_roles=None):
        """
        PartialMeUser - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'buyer': 'MeBuyer',
            'id': 'str',
            'username': 'str',
            'password': 'str',
            'first_name': 'str',
            'last_name': 'str',
            'email': 'str',
            'phone': 'str',
            'terms_accepted': 'str',
            'active': 'bool',
            'xp': 'object',
            'available_roles': 'list[str]'
        }

        self.attribute_map = {
            'buyer': 'Buyer',
            'id': 'ID',
            'username': 'Username',
            'password': 'Password',
            'first_name': 'FirstName',
            'last_name': 'LastName',
            'email': 'Email',
            'phone': 'Phone',
            'terms_accepted': 'TermsAccepted',
            'active': 'Active',
            'xp': 'xp',
            'available_roles': 'AvailableRoles'
        }

        self._buyer = buyer
        self._id = id
        self._username = username
        self._password = password
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._phone = phone
        self._terms_accepted = terms_accepted
        self._active = active
        self._xp = xp
        self._available_roles = available_roles

    @property
    def buyer(self):
        """
        Gets the buyer of this PartialMeUser.


        :return: The buyer of this PartialMeUser.
        :rtype: MeBuyer
        """
        return self._buyer

    @buyer.setter
    def buyer(self, buyer):
        """
        Sets the buyer of this PartialMeUser.


        :param buyer: The buyer of this PartialMeUser.
        :type: MeBuyer
        """

        self._buyer = buyer

    @property
    def id(self):
        """
        Gets the id of this PartialMeUser.


        :return: The id of this PartialMeUser.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PartialMeUser.


        :param id: The id of this PartialMeUser.
        :type: str
        """

        self._id = id

    @property
    def username(self):
        """
        Gets the username of this PartialMeUser.


        :return: The username of this PartialMeUser.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this PartialMeUser.


        :param username: The username of this PartialMeUser.
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """
        Gets the password of this PartialMeUser.


        :return: The password of this PartialMeUser.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this PartialMeUser.


        :param password: The password of this PartialMeUser.
        :type: str
        """

        self._password = password

    @property
    def first_name(self):
        """
        Gets the first_name of this PartialMeUser.


        :return: The first_name of this PartialMeUser.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this PartialMeUser.


        :param first_name: The first_name of this PartialMeUser.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this PartialMeUser.


        :return: The last_name of this PartialMeUser.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this PartialMeUser.


        :param last_name: The last_name of this PartialMeUser.
        :type: str
        """

        self._last_name = last_name

    @property
    def email(self):
        """
        Gets the email of this PartialMeUser.


        :return: The email of this PartialMeUser.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this PartialMeUser.


        :param email: The email of this PartialMeUser.
        :type: str
        """

        self._email = email

    @property
    def phone(self):
        """
        Gets the phone of this PartialMeUser.


        :return: The phone of this PartialMeUser.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this PartialMeUser.


        :param phone: The phone of this PartialMeUser.
        :type: str
        """

        self._phone = phone

    @property
    def terms_accepted(self):
        """
        Gets the terms_accepted of this PartialMeUser.


        :return: The terms_accepted of this PartialMeUser.
        :rtype: str
        """
        return self._terms_accepted

    @terms_accepted.setter
    def terms_accepted(self, terms_accepted):
        """
        Sets the terms_accepted of this PartialMeUser.


        :param terms_accepted: The terms_accepted of this PartialMeUser.
        :type: str
        """

        self._terms_accepted = terms_accepted

    @property
    def active(self):
        """
        Gets the active of this PartialMeUser.


        :return: The active of this PartialMeUser.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this PartialMeUser.


        :param active: The active of this PartialMeUser.
        :type: bool
        """

        self._active = active

    @property
    def xp(self):
        """
        Gets the xp of this PartialMeUser.


        :return: The xp of this PartialMeUser.
        :rtype: object
        """
        return self._xp

    @xp.setter
    def xp(self, xp):
        """
        Sets the xp of this PartialMeUser.


        :param xp: The xp of this PartialMeUser.
        :type: object
        """

        self._xp = xp

    @property
    def available_roles(self):
        """
        Gets the available_roles of this PartialMeUser.


        :return: The available_roles of this PartialMeUser.
        :rtype: list[str]
        """
        return self._available_roles

    @available_roles.setter
    def available_roles(self, available_roles):
        """
        Sets the available_roles of this PartialMeUser.


        :param available_roles: The available_roles of this PartialMeUser.
        :type: list[str]
        """

        self._available_roles = available_roles

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