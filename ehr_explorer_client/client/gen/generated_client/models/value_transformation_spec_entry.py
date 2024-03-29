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


class ValueTransformationSpecEntry(object):
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
        'entity': 'str',
        '_property': 'str',
        'transform': 'Transform'
    }

    attribute_map = {
        'entity': 'entity',
        '_property': 'property',
        'transform': 'transform'
    }

    def __init__(self, entity=None, _property=None, transform=None, local_vars_configuration=None):  # noqa: E501
        """ValueTransformationSpecEntry - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._entity = None
        self.__property = None
        self._transform = None
        self.discriminator = None

        self.entity = entity
        self._property = _property
        self.transform = transform

    @property
    def entity(self):
        """Gets the entity of this ValueTransformationSpecEntry.  # noqa: E501


        :return: The entity of this ValueTransformationSpecEntry.  # noqa: E501
        :rtype: str
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this ValueTransformationSpecEntry.


        :param entity: The entity of this ValueTransformationSpecEntry.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and entity is None:  # noqa: E501
            raise ValueError("Invalid value for `entity`, must not be `None`")  # noqa: E501

        self._entity = entity

    @property
    def _property(self):
        """Gets the _property of this ValueTransformationSpecEntry.  # noqa: E501


        :return: The _property of this ValueTransformationSpecEntry.  # noqa: E501
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this ValueTransformationSpecEntry.


        :param _property: The _property of this ValueTransformationSpecEntry.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and _property is None:  # noqa: E501
            raise ValueError("Invalid value for `_property`, must not be `None`")  # noqa: E501

        self.__property = _property

    @property
    def transform(self):
        """Gets the transform of this ValueTransformationSpecEntry.  # noqa: E501


        :return: The transform of this ValueTransformationSpecEntry.  # noqa: E501
        :rtype: Transform
        """
        return self._transform

    @transform.setter
    def transform(self, transform):
        """Sets the transform of this ValueTransformationSpecEntry.


        :param transform: The transform of this ValueTransformationSpecEntry.  # noqa: E501
        :type: Transform
        """
        if self.local_vars_configuration.client_side_validation and transform is None:  # noqa: E501
            raise ValueError("Invalid value for `transform`, must not be `None`")  # noqa: E501

        self._transform = transform

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
        if not isinstance(other, ValueTransformationSpecEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ValueTransformationSpecEntry):
            return True

        return self.to_dict() != other.to_dict()
