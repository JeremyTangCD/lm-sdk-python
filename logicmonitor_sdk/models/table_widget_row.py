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

from logicmonitor_sdk.models.table_widget_instance_cell import TableWidgetInstanceCell  # noqa: F401,E501


class TableWidgetRow(object):
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
        'instances': 'list[TableWidgetInstanceCell]',
        'group_id': 'int',
        'label': 'str',
        'device_id': 'int',
        'device_display_name': 'str',
        'group_full_path': 'str'
    }

    attribute_map = {
        'instances': 'instances',
        'group_id': 'groupId',
        'label': 'label',
        'device_id': 'deviceId',
        'device_display_name': 'deviceDisplayName',
        'group_full_path': 'groupFullPath'
    }

    def __init__(self, instances=None, group_id=None, label=None, device_id=None, device_display_name=None, group_full_path=None):  # noqa: E501
        """TableWidgetRow - a model defined in Swagger"""  # noqa: E501

        self._instances = None
        self._group_id = None
        self._label = None
        self._device_id = None
        self._device_display_name = None
        self._group_full_path = None
        self.discriminator = None

        if instances is not None:
            self.instances = instances
        if group_id is not None:
            self.group_id = group_id
        if label is not None:
            self.label = label
        self.device_id = device_id
        if device_display_name is not None:
            self.device_display_name = device_display_name
        if group_full_path is not None:
            self.group_full_path = group_full_path

    @property
    def instances(self):
        """Gets the instances of this TableWidgetRow.  # noqa: E501


        :return: The instances of this TableWidgetRow.  # noqa: E501
        :rtype: list[TableWidgetInstanceCell]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this TableWidgetRow.


        :param instances: The instances of this TableWidgetRow.  # noqa: E501
        :type: list[TableWidgetInstanceCell]
        """

        self._instances = instances

    @property
    def group_id(self):
        """Gets the group_id of this TableWidgetRow.  # noqa: E501


        :return: The group_id of this TableWidgetRow.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this TableWidgetRow.


        :param group_id: The group_id of this TableWidgetRow.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def label(self):
        """Gets the label of this TableWidgetRow.  # noqa: E501


        :return: The label of this TableWidgetRow.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this TableWidgetRow.


        :param label: The label of this TableWidgetRow.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def device_id(self):
        """Gets the device_id of this TableWidgetRow.  # noqa: E501


        :return: The device_id of this TableWidgetRow.  # noqa: E501
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this TableWidgetRow.


        :param device_id: The device_id of this TableWidgetRow.  # noqa: E501
        :type: int
        """
        if device_id is None:
            raise ValueError("Invalid value for `device_id`, must not be `None`")  # noqa: E501

        self._device_id = device_id

    @property
    def device_display_name(self):
        """Gets the device_display_name of this TableWidgetRow.  # noqa: E501


        :return: The device_display_name of this TableWidgetRow.  # noqa: E501
        :rtype: str
        """
        return self._device_display_name

    @device_display_name.setter
    def device_display_name(self, device_display_name):
        """Sets the device_display_name of this TableWidgetRow.


        :param device_display_name: The device_display_name of this TableWidgetRow.  # noqa: E501
        :type: str
        """

        self._device_display_name = device_display_name

    @property
    def group_full_path(self):
        """Gets the group_full_path of this TableWidgetRow.  # noqa: E501


        :return: The group_full_path of this TableWidgetRow.  # noqa: E501
        :rtype: str
        """
        return self._group_full_path

    @group_full_path.setter
    def group_full_path(self, group_full_path):
        """Sets the group_full_path of this TableWidgetRow.


        :param group_full_path: The group_full_path of this TableWidgetRow.  # noqa: E501
        :type: str
        """

        self._group_full_path = group_full_path

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
        if issubclass(TableWidgetRow, dict):
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
        if not isinstance(other, TableWidgetRow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other