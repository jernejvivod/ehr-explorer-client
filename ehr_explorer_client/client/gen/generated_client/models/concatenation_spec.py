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


class ConcatenationSpec(object):
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
        'concatenation_scheme': 'str'
    }

    attribute_map = {
        'concatenation_scheme': 'concatenationScheme'
    }

    def __init__(self, concatenation_scheme=None, local_vars_configuration=None):  # noqa: E501
        """ConcatenationSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._concatenation_scheme = None
        self.discriminator = None

        self.concatenation_scheme = concatenation_scheme

    @property
    def concatenation_scheme(self):
        """Gets the concatenation_scheme of this ConcatenationSpec.  # noqa: E501


        :return: The concatenation_scheme of this ConcatenationSpec.  # noqa: E501
        :rtype: str
        """
        return self._concatenation_scheme

    @concatenation_scheme.setter
    def concatenation_scheme(self, concatenation_scheme):
        """Sets the concatenation_scheme of this ConcatenationSpec.


        :param concatenation_scheme: The concatenation_scheme of this ConcatenationSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and concatenation_scheme is None:  # noqa: E501
            raise ValueError("Invalid value for `concatenation_scheme`, must not be `None`")  # noqa: E501
        allowed_values = ["ZERO", "ONE", "TWO"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and concatenation_scheme not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `concatenation_scheme` ({0}), must be one of {1}"  # noqa: E501
                .format(concatenation_scheme, allowed_values)
            )

        self._concatenation_scheme = concatenation_scheme

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
        if not isinstance(other, ConcatenationSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConcatenationSpec):
            return True

        return self.to_dict() != other.to_dict()
