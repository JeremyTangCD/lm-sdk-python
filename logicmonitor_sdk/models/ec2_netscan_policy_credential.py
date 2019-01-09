# coding: utf-8

"""
    LogicMonitor REST API

    LogicMonitor is a SaaS-based performance monitoring platform that provides full visibility into complex, hybrid infrastructures, offering granular performance monitoring and actionable data and insights. logicmonitor_sdk enables you to manage your LogicMonitor account programmatically.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EC2NetscanPolicyCredential(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'device_group_id': 'int',
        'custom': 'dict(str, str)',
        'device_group_name': 'str'
    }

    attribute_map = {
        'device_group_id': 'deviceGroupId',
        'custom': 'custom',
        'device_group_name': 'deviceGroupName'
    }

    def __init__(self, device_group_id=None, custom=None, device_group_name=None):  # noqa: E501
        """EC2NetscanPolicyCredential - a model defined in Swagger"""  # noqa: E501

        self._device_group_id = None
        self._custom = None
        self._device_group_name = None
        self.discriminator = None

        if device_group_id is not None:
            self.device_group_id = device_group_id
        if custom is not None:
            self.custom = custom
        if device_group_name is not None:
            self.device_group_name = device_group_name

    @property
    def device_group_id(self):
        """Gets the device_group_id of this EC2NetscanPolicyCredential.  # noqa: E501

        The ID of the device group that credentials should be inherited from, for this scan  # noqa: E501

        :return: The device_group_id of this EC2NetscanPolicyCredential.  # noqa: E501
        :rtype: int
        """
        return self._device_group_id

    @device_group_id.setter
    def device_group_id(self, device_group_id):
        """Sets the device_group_id of this EC2NetscanPolicyCredential.

        The ID of the device group that credentials should be inherited from, for this scan  # noqa: E501

        :param device_group_id: The device_group_id of this EC2NetscanPolicyCredential.  # noqa: E501
        :type: int
        """

        self._device_group_id = device_group_id

    @property
    def custom(self):
        """Gets the custom of this EC2NetscanPolicyCredential.  # noqa: E501

        Custom credentials that should be used for this scan  # noqa: E501

        :return: The custom of this EC2NetscanPolicyCredential.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """Sets the custom of this EC2NetscanPolicyCredential.

        Custom credentials that should be used for this scan  # noqa: E501

        :param custom: The custom of this EC2NetscanPolicyCredential.  # noqa: E501
        :type: dict(str, str)
        """

        self._custom = custom

    @property
    def device_group_name(self):
        """Gets the device_group_name of this EC2NetscanPolicyCredential.  # noqa: E501

        The name of the device group that credentials should be inherited from, for this scan  # noqa: E501

        :return: The device_group_name of this EC2NetscanPolicyCredential.  # noqa: E501
        :rtype: str
        """
        return self._device_group_name

    @device_group_name.setter
    def device_group_name(self, device_group_name):
        """Sets the device_group_name of this EC2NetscanPolicyCredential.

        The name of the device group that credentials should be inherited from, for this scan  # noqa: E501

        :param device_group_name: The device_group_name of this EC2NetscanPolicyCredential.  # noqa: E501
        :type: str
        """

        self._device_group_name = device_group_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(EC2NetscanPolicyCredential, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EC2NetscanPolicyCredential):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
