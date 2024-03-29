# coding: utf-8

"""
    EHR Explorer Processor API

    API for the EHR Explorer Processor microservice  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: vivod.jernej@gmail.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from generated_client.configuration import Configuration


class PropertyStats(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'property_name': 'str',
        'num_null': 'int',
        'num_unique': 'int'
    }

    attribute_map = {
        'property_name': 'propertyName',
        'num_null': 'numNull',
        'num_unique': 'numUnique'
    }

    def __init__(self, property_name=None, num_null=None, num_unique=None, local_vars_configuration=None):  # noqa: E501
        """PropertyStats - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._property_name = None
        self._num_null = None
        self._num_unique = None
        self.discriminator = None

        if property_name is not None:
            self.property_name = property_name
        if num_null is not None:
            self.num_null = num_null
        if num_unique is not None:
            self.num_unique = num_unique

    @property
    def property_name(self):
        """Gets the property_name of this PropertyStats.  # noqa: E501


        :return: The property_name of this PropertyStats.  # noqa: E501
        :rtype: str
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name):
        """Sets the property_name of this PropertyStats.


        :param property_name: The property_name of this PropertyStats.  # noqa: E501
        :type: str
        """

        self._property_name = property_name

    @property
    def num_null(self):
        """Gets the num_null of this PropertyStats.  # noqa: E501


        :return: The num_null of this PropertyStats.  # noqa: E501
        :rtype: int
        """
        return self._num_null

    @num_null.setter
    def num_null(self, num_null):
        """Sets the num_null of this PropertyStats.


        :param num_null: The num_null of this PropertyStats.  # noqa: E501
        :type: int
        """

        self._num_null = num_null

    @property
    def num_unique(self):
        """Gets the num_unique of this PropertyStats.  # noqa: E501


        :return: The num_unique of this PropertyStats.  # noqa: E501
        :rtype: int
        """
        return self._num_unique

    @num_unique.setter
    def num_unique(self, num_unique):
        """Sets the num_unique of this PropertyStats.


        :param num_unique: The num_unique of this PropertyStats.  # noqa: E501
        :type: int
        """

        self._num_unique = num_unique

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PropertyStats):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PropertyStats):
            return True

        return self.to_dict() != other.to_dict()
