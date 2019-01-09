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

from logicmonitor_sdk.models.website_collector_info import WebsiteCollectorInfo  # noqa: F401,E501


class WebsiteLocation(object):
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
        'all': 'bool',
        'collector_ids': 'list[int]',
        'collectors': 'list[WebsiteCollectorInfo]',
        'smg_ids': 'list[int]'
    }

    attribute_map = {
        'all': 'all',
        'collector_ids': 'collectorIds',
        'collectors': 'collectors',
        'smg_ids': 'smgIds'
    }

    def __init__(self, all=None, collector_ids=None, collectors=None, smg_ids=None):  # noqa: E501
        """WebsiteLocation - a model defined in Swagger"""  # noqa: E501

        self._all = None
        self._collector_ids = None
        self._collectors = None
        self._smg_ids = None
        self.discriminator = None

        if all is not None:
            self.all = all
        if collector_ids is not None:
            self.collector_ids = collector_ids
        if collectors is not None:
            self.collectors = collectors
        if smg_ids is not None:
            self.smg_ids = smg_ids

    @property
    def all(self):
        """Gets the all of this WebsiteLocation.  # noqa: E501


        :return: The all of this WebsiteLocation.  # noqa: E501
        :rtype: bool
        """
        return self._all

    @all.setter
    def all(self, all):
        """Sets the all of this WebsiteLocation.


        :param all: The all of this WebsiteLocation.  # noqa: E501
        :type: bool
        """

        self._all = all

    @property
    def collector_ids(self):
        """Gets the collector_ids of this WebsiteLocation.  # noqa: E501


        :return: The collector_ids of this WebsiteLocation.  # noqa: E501
        :rtype: list[int]
        """
        return self._collector_ids

    @collector_ids.setter
    def collector_ids(self, collector_ids):
        """Sets the collector_ids of this WebsiteLocation.


        :param collector_ids: The collector_ids of this WebsiteLocation.  # noqa: E501
        :type: list[int]
        """

        self._collector_ids = collector_ids

    @property
    def collectors(self):
        """Gets the collectors of this WebsiteLocation.  # noqa: E501


        :return: The collectors of this WebsiteLocation.  # noqa: E501
        :rtype: list[WebsiteCollectorInfo]
        """
        return self._collectors

    @collectors.setter
    def collectors(self, collectors):
        """Sets the collectors of this WebsiteLocation.


        :param collectors: The collectors of this WebsiteLocation.  # noqa: E501
        :type: list[WebsiteCollectorInfo]
        """

        self._collectors = collectors

    @property
    def smg_ids(self):
        """Gets the smg_ids of this WebsiteLocation.  # noqa: E501


        :return: The smg_ids of this WebsiteLocation.  # noqa: E501
        :rtype: list[int]
        """
        return self._smg_ids

    @smg_ids.setter
    def smg_ids(self, smg_ids):
        """Sets the smg_ids of this WebsiteLocation.


        :param smg_ids: The smg_ids of this WebsiteLocation.  # noqa: E501
        :type: list[int]
        """

        self._smg_ids = smg_ids

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
        if issubclass(WebsiteLocation, dict):
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
        if not isinstance(other, WebsiteLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
