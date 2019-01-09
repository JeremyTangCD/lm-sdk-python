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


class SlaMetric(object):
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
        'website_name': 'str',
        'group_name': 'str',
        'exclude_sdt': 'bool'
    }

    attribute_map = {
        'website_name': 'websiteName',
        'group_name': 'groupName',
        'exclude_sdt': 'excludeSDT'
    }

    def __init__(self, website_name=None, group_name=None, exclude_sdt=None):  # noqa: E501
        """SlaMetric - a model defined in Swagger"""  # noqa: E501

        self._website_name = None
        self._group_name = None
        self._exclude_sdt = None
        self.discriminator = None

        if website_name is not None:
            self.website_name = website_name
        if group_name is not None:
            self.group_name = group_name
        if exclude_sdt is not None:
            self.exclude_sdt = exclude_sdt

    @property
    def website_name(self):
        """Gets the website_name of this SlaMetric.  # noqa: E501


        :return: The website_name of this SlaMetric.  # noqa: E501
        :rtype: str
        """
        return self._website_name

    @website_name.setter
    def website_name(self, website_name):
        """Sets the website_name of this SlaMetric.


        :param website_name: The website_name of this SlaMetric.  # noqa: E501
        :type: str
        """

        self._website_name = website_name

    @property
    def group_name(self):
        """Gets the group_name of this SlaMetric.  # noqa: E501


        :return: The group_name of this SlaMetric.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this SlaMetric.


        :param group_name: The group_name of this SlaMetric.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    @property
    def exclude_sdt(self):
        """Gets the exclude_sdt of this SlaMetric.  # noqa: E501


        :return: The exclude_sdt of this SlaMetric.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_sdt

    @exclude_sdt.setter
    def exclude_sdt(self, exclude_sdt):
        """Sets the exclude_sdt of this SlaMetric.


        :param exclude_sdt: The exclude_sdt of this SlaMetric.  # noqa: E501
        :type: bool
        """

        self._exclude_sdt = exclude_sdt

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
        if issubclass(SlaMetric, dict):
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
        if not isinstance(other, SlaMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
