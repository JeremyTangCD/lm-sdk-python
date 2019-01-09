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


class GcpAccountTestResult(object):
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
        'no_permission_services': 'list[str]',
        'detail_link': 'str'
    }

    attribute_map = {
        'no_permission_services': 'noPermissionServices',
        'detail_link': 'detailLink'
    }

    def __init__(self, no_permission_services=None, detail_link=None):  # noqa: E501
        """GcpAccountTestResult - a model defined in Swagger"""  # noqa: E501

        self._no_permission_services = None
        self._detail_link = None
        self.discriminator = None

        if no_permission_services is not None:
            self.no_permission_services = no_permission_services
        if detail_link is not None:
            self.detail_link = detail_link

    @property
    def no_permission_services(self):
        """Gets the no_permission_services of this GcpAccountTestResult.  # noqa: E501


        :return: The no_permission_services of this GcpAccountTestResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._no_permission_services

    @no_permission_services.setter
    def no_permission_services(self, no_permission_services):
        """Sets the no_permission_services of this GcpAccountTestResult.


        :param no_permission_services: The no_permission_services of this GcpAccountTestResult.  # noqa: E501
        :type: list[str]
        """

        self._no_permission_services = no_permission_services

    @property
    def detail_link(self):
        """Gets the detail_link of this GcpAccountTestResult.  # noqa: E501


        :return: The detail_link of this GcpAccountTestResult.  # noqa: E501
        :rtype: str
        """
        return self._detail_link

    @detail_link.setter
    def detail_link(self, detail_link):
        """Sets the detail_link of this GcpAccountTestResult.


        :param detail_link: The detail_link of this GcpAccountTestResult.  # noqa: E501
        :type: str
        """

        self._detail_link = detail_link

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
        if issubclass(GcpAccountTestResult, dict):
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
        if not isinstance(other, GcpAccountTestResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other