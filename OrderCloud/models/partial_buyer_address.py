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


class PartialBuyerAddress(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, shipping=None, billing=None, editable=None, date_created=None, company_name=None, first_name=None, last_name=None, street1=None, street2=None, city=None, state=None, zip=None, country=None, phone=None, address_name=None, xp=None):
        """
        PartialBuyerAddress - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'shipping': 'bool',
            'billing': 'bool',
            'editable': 'bool',
            'date_created': 'str',
            'company_name': 'str',
            'first_name': 'str',
            'last_name': 'str',
            'street1': 'str',
            'street2': 'str',
            'city': 'str',
            'state': 'str',
            'zip': 'str',
            'country': 'str',
            'phone': 'str',
            'address_name': 'str',
            'xp': 'object'
        }

        self.attribute_map = {
            'id': 'ID',
            'shipping': 'Shipping',
            'billing': 'Billing',
            'editable': 'Editable',
            'date_created': 'DateCreated',
            'company_name': 'CompanyName',
            'first_name': 'FirstName',
            'last_name': 'LastName',
            'street1': 'Street1',
            'street2': 'Street2',
            'city': 'City',
            'state': 'State',
            'zip': 'Zip',
            'country': 'Country',
            'phone': 'Phone',
            'address_name': 'AddressName',
            'xp': 'xp'
        }

        self._id = id
        self._shipping = shipping
        self._billing = billing
        self._editable = editable
        self._date_created = date_created
        self._company_name = company_name
        self._first_name = first_name
        self._last_name = last_name
        self._street1 = street1
        self._street2 = street2
        self._city = city
        self._state = state
        self._zip = zip
        self._country = country
        self._phone = phone
        self._address_name = address_name
        self._xp = xp

    @property
    def id(self):
        """
        Gets the id of this PartialBuyerAddress.


        :return: The id of this PartialBuyerAddress.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PartialBuyerAddress.


        :param id: The id of this PartialBuyerAddress.
        :type: str
        """

        self._id = id

    @property
    def shipping(self):
        """
        Gets the shipping of this PartialBuyerAddress.


        :return: The shipping of this PartialBuyerAddress.
        :rtype: bool
        """
        return self._shipping

    @shipping.setter
    def shipping(self, shipping):
        """
        Sets the shipping of this PartialBuyerAddress.


        :param shipping: The shipping of this PartialBuyerAddress.
        :type: bool
        """

        self._shipping = shipping

    @property
    def billing(self):
        """
        Gets the billing of this PartialBuyerAddress.


        :return: The billing of this PartialBuyerAddress.
        :rtype: bool
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        """
        Sets the billing of this PartialBuyerAddress.


        :param billing: The billing of this PartialBuyerAddress.
        :type: bool
        """

        self._billing = billing

    @property
    def editable(self):
        """
        Gets the editable of this PartialBuyerAddress.


        :return: The editable of this PartialBuyerAddress.
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        """
        Sets the editable of this PartialBuyerAddress.


        :param editable: The editable of this PartialBuyerAddress.
        :type: bool
        """

        self._editable = editable

    @property
    def date_created(self):
        """
        Gets the date_created of this PartialBuyerAddress.


        :return: The date_created of this PartialBuyerAddress.
        :rtype: str
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this PartialBuyerAddress.


        :param date_created: The date_created of this PartialBuyerAddress.
        :type: str
        """

        self._date_created = date_created

    @property
    def company_name(self):
        """
        Gets the company_name of this PartialBuyerAddress.


        :return: The company_name of this PartialBuyerAddress.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """
        Sets the company_name of this PartialBuyerAddress.


        :param company_name: The company_name of this PartialBuyerAddress.
        :type: str
        """

        self._company_name = company_name

    @property
    def first_name(self):
        """
        Gets the first_name of this PartialBuyerAddress.


        :return: The first_name of this PartialBuyerAddress.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this PartialBuyerAddress.


        :param first_name: The first_name of this PartialBuyerAddress.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this PartialBuyerAddress.


        :return: The last_name of this PartialBuyerAddress.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this PartialBuyerAddress.


        :param last_name: The last_name of this PartialBuyerAddress.
        :type: str
        """

        self._last_name = last_name

    @property
    def street1(self):
        """
        Gets the street1 of this PartialBuyerAddress.


        :return: The street1 of this PartialBuyerAddress.
        :rtype: str
        """
        return self._street1

    @street1.setter
    def street1(self, street1):
        """
        Sets the street1 of this PartialBuyerAddress.


        :param street1: The street1 of this PartialBuyerAddress.
        :type: str
        """

        self._street1 = street1

    @property
    def street2(self):
        """
        Gets the street2 of this PartialBuyerAddress.


        :return: The street2 of this PartialBuyerAddress.
        :rtype: str
        """
        return self._street2

    @street2.setter
    def street2(self, street2):
        """
        Sets the street2 of this PartialBuyerAddress.


        :param street2: The street2 of this PartialBuyerAddress.
        :type: str
        """

        self._street2 = street2

    @property
    def city(self):
        """
        Gets the city of this PartialBuyerAddress.


        :return: The city of this PartialBuyerAddress.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this PartialBuyerAddress.


        :param city: The city of this PartialBuyerAddress.
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """
        Gets the state of this PartialBuyerAddress.


        :return: The state of this PartialBuyerAddress.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this PartialBuyerAddress.


        :param state: The state of this PartialBuyerAddress.
        :type: str
        """

        self._state = state

    @property
    def zip(self):
        """
        Gets the zip of this PartialBuyerAddress.


        :return: The zip of this PartialBuyerAddress.
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """
        Sets the zip of this PartialBuyerAddress.


        :param zip: The zip of this PartialBuyerAddress.
        :type: str
        """

        self._zip = zip

    @property
    def country(self):
        """
        Gets the country of this PartialBuyerAddress.


        :return: The country of this PartialBuyerAddress.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this PartialBuyerAddress.


        :param country: The country of this PartialBuyerAddress.
        :type: str
        """

        self._country = country

    @property
    def phone(self):
        """
        Gets the phone of this PartialBuyerAddress.


        :return: The phone of this PartialBuyerAddress.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this PartialBuyerAddress.


        :param phone: The phone of this PartialBuyerAddress.
        :type: str
        """

        self._phone = phone

    @property
    def address_name(self):
        """
        Gets the address_name of this PartialBuyerAddress.


        :return: The address_name of this PartialBuyerAddress.
        :rtype: str
        """
        return self._address_name

    @address_name.setter
    def address_name(self, address_name):
        """
        Sets the address_name of this PartialBuyerAddress.


        :param address_name: The address_name of this PartialBuyerAddress.
        :type: str
        """

        self._address_name = address_name

    @property
    def xp(self):
        """
        Gets the xp of this PartialBuyerAddress.


        :return: The xp of this PartialBuyerAddress.
        :rtype: object
        """
        return self._xp

    @xp.setter
    def xp(self, xp):
        """
        Sets the xp of this PartialBuyerAddress.


        :param xp: The xp of this PartialBuyerAddress.
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