# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DeviceGroupAlertThresholdInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'user_permission': 'str',
        'group_id': 'int',
        'alert_enabled': 'bool',
        'group_full_path': 'str',
        'alert_expr': 'str'
    }

    attribute_map = {
        'user_permission': 'userPermission',
        'group_id': 'groupId',
        'alert_enabled': 'alertEnabled',
        'group_full_path': 'groupFullPath',
        'alert_expr': 'alertExpr'
    }

    def __init__(self, user_permission=None, group_id=None, alert_enabled=None, group_full_path=None, alert_expr=None):
        """
        DeviceGroupAlertThresholdInfo - a model defined in Swagger
        """

        self._user_permission = None
        self._group_id = None
        self._alert_enabled = None
        self._group_full_path = None
        self._alert_expr = None

        if user_permission is not None:
          self.user_permission = user_permission
        if group_id is not None:
          self.group_id = group_id
        if alert_enabled is not None:
          self.alert_enabled = alert_enabled
        if group_full_path is not None:
          self.group_full_path = group_full_path
        if alert_expr is not None:
          self.alert_expr = alert_expr

    @property
    def user_permission(self):
        """
        Gets the user_permission of this DeviceGroupAlertThresholdInfo.

        :return: The user_permission of this DeviceGroupAlertThresholdInfo.
        :rtype: str
        """
        return self._user_permission

    @user_permission.setter
    def user_permission(self, user_permission):
        """
        Sets the user_permission of this DeviceGroupAlertThresholdInfo.

        :param user_permission: The user_permission of this DeviceGroupAlertThresholdInfo.
        :type: str
        """

        self._user_permission = user_permission

    @property
    def group_id(self):
        """
        Gets the group_id of this DeviceGroupAlertThresholdInfo.

        :return: The group_id of this DeviceGroupAlertThresholdInfo.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this DeviceGroupAlertThresholdInfo.

        :param group_id: The group_id of this DeviceGroupAlertThresholdInfo.
        :type: int
        """

        self._group_id = group_id

    @property
    def alert_enabled(self):
        """
        Gets the alert_enabled of this DeviceGroupAlertThresholdInfo.

        :return: The alert_enabled of this DeviceGroupAlertThresholdInfo.
        :rtype: bool
        """
        return self._alert_enabled

    @alert_enabled.setter
    def alert_enabled(self, alert_enabled):
        """
        Sets the alert_enabled of this DeviceGroupAlertThresholdInfo.

        :param alert_enabled: The alert_enabled of this DeviceGroupAlertThresholdInfo.
        :type: bool
        """

        self._alert_enabled = alert_enabled

    @property
    def group_full_path(self):
        """
        Gets the group_full_path of this DeviceGroupAlertThresholdInfo.

        :return: The group_full_path of this DeviceGroupAlertThresholdInfo.
        :rtype: str
        """
        return self._group_full_path

    @group_full_path.setter
    def group_full_path(self, group_full_path):
        """
        Sets the group_full_path of this DeviceGroupAlertThresholdInfo.

        :param group_full_path: The group_full_path of this DeviceGroupAlertThresholdInfo.
        :type: str
        """

        self._group_full_path = group_full_path

    @property
    def alert_expr(self):
        """
        Gets the alert_expr of this DeviceGroupAlertThresholdInfo.

        :return: The alert_expr of this DeviceGroupAlertThresholdInfo.
        :rtype: str
        """
        return self._alert_expr

    @alert_expr.setter
    def alert_expr(self, alert_expr):
        """
        Sets the alert_expr of this DeviceGroupAlertThresholdInfo.

        :param alert_expr: The alert_expr of this DeviceGroupAlertThresholdInfo.
        :type: str
        """

        self._alert_expr = alert_expr

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
        if not isinstance(other, DeviceGroupAlertThresholdInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other