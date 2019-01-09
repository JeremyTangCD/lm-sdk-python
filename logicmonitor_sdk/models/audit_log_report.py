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

from logicmonitor_sdk.models.dynamic_column import DynamicColumn  # noqa: F401,E501
from logicmonitor_sdk.models.report_base import ReportBase  # noqa: F401,E501
from logicmonitor_sdk.models.report_recipient import ReportRecipient  # noqa: F401,E501


class AuditLogReport(ReportBase):
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
        'lastmodify_user_id': 'int',
        'delivery': 'str',
        'user_permission': 'str',
        'last_generate_on': 'int',
        'report_link_num': 'int',
        'group_id': 'int',
        'format': 'str',
        'description': 'str',
        'last_generate_size': 'int',
        'custom_report_type_id': 'int',
        'type': 'str',
        'last_generate_pages': 'int',
        'schedule': 'str',
        'recipients': 'list[ReportRecipient]',
        'custom_report_type_name': 'str',
        'name': 'str',
        'enable_view_as_other_user': 'bool',
        'lastmodify_user_name': 'str',
        'id': 'int',
        'schedule_timezone': 'str',
        'filter': 'str',
        'sorted_by': 'str',
        'date_range': 'str',
        'columns': 'list[DynamicColumn]',
        'username': 'str'
    }

    attribute_map = {
        'lastmodify_user_id': 'lastmodifyUserId',
        'delivery': 'delivery',
        'user_permission': 'userPermission',
        'last_generate_on': 'lastGenerateOn',
        'report_link_num': 'reportLinkNum',
        'group_id': 'groupId',
        'format': 'format',
        'description': 'description',
        'last_generate_size': 'lastGenerateSize',
        'custom_report_type_id': 'customReportTypeId',
        'type': 'type',
        'last_generate_pages': 'lastGeneratePages',
        'schedule': 'schedule',
        'recipients': 'recipients',
        'custom_report_type_name': 'customReportTypeName',
        'name': 'name',
        'enable_view_as_other_user': 'enableViewAsOtherUser',
        'lastmodify_user_name': 'lastmodifyUserName',
        'id': 'id',
        'schedule_timezone': 'scheduleTimezone',
        'filter': 'filter',
        'sorted_by': 'sortedBy',
        'date_range': 'dateRange',
        'columns': 'columns',
        'username': 'username'
    }

    def __init__(self, lastmodify_user_id=None, delivery=None, user_permission=None, last_generate_on=None, report_link_num=None, group_id=None, format=None, description=None, last_generate_size=None, custom_report_type_id=None, type=None, last_generate_pages=None, schedule=None, recipients=None, custom_report_type_name=None, name=None, enable_view_as_other_user=None, lastmodify_user_name=None, id=None, schedule_timezone=None, filter=None, sorted_by=None, date_range=None, columns=None, username=None):  # noqa: E501
        """AuditLogReport - a model defined in Swagger"""  # noqa: E501

        self._lastmodify_user_id = None
        self._delivery = None
        self._user_permission = None
        self._last_generate_on = None
        self._report_link_num = None
        self._group_id = None
        self._format = None
        self._description = None
        self._last_generate_size = None
        self._custom_report_type_id = None
        self._type = None
        self._last_generate_pages = None
        self._schedule = None
        self._recipients = None
        self._custom_report_type_name = None
        self._name = None
        self._enable_view_as_other_user = None
        self._lastmodify_user_name = None
        self._id = None
        self._schedule_timezone = None
        self._filter = None
        self._sorted_by = None
        self._date_range = None
        self._columns = None
        self._username = None
        self.discriminator = None

        if lastmodify_user_id is not None:
            self.lastmodify_user_id = lastmodify_user_id
        if delivery is not None:
            self.delivery = delivery
        if user_permission is not None:
            self.user_permission = user_permission
        if last_generate_on is not None:
            self.last_generate_on = last_generate_on
        if report_link_num is not None:
            self.report_link_num = report_link_num
        if group_id is not None:
            self.group_id = group_id
        if format is not None:
            self.format = format
        if description is not None:
            self.description = description
        if last_generate_size is not None:
            self.last_generate_size = last_generate_size
        if custom_report_type_id is not None:
            self.custom_report_type_id = custom_report_type_id
        self.type = type
        if last_generate_pages is not None:
            self.last_generate_pages = last_generate_pages
        if schedule is not None:
            self.schedule = schedule
        if recipients is not None:
            self.recipients = recipients
        if custom_report_type_name is not None:
            self.custom_report_type_name = custom_report_type_name
        self.name = name
        if enable_view_as_other_user is not None:
            self.enable_view_as_other_user = enable_view_as_other_user
        if lastmodify_user_name is not None:
            self.lastmodify_user_name = lastmodify_user_name
        if id is not None:
            self.id = id
        if schedule_timezone is not None:
            self.schedule_timezone = schedule_timezone
        if filter is not None:
            self.filter = filter
        if sorted_by is not None:
            self.sorted_by = sorted_by
        if date_range is not None:
            self.date_range = date_range
        if columns is not None:
            self.columns = columns
        if username is not None:
            self.username = username

    @property
    def lastmodify_user_id(self):
        """Gets the lastmodify_user_id of this AuditLogReport.  # noqa: E501

        The Id of the user that last modified the report  # noqa: E501

        :return: The lastmodify_user_id of this AuditLogReport.  # noqa: E501
        :rtype: int
        """
        return self._lastmodify_user_id

    @lastmodify_user_id.setter
    def lastmodify_user_id(self, lastmodify_user_id):
        """Sets the lastmodify_user_id of this AuditLogReport.

        The Id of the user that last modified the report  # noqa: E501

        :param lastmodify_user_id: The lastmodify_user_id of this AuditLogReport.  # noqa: E501
        :type: int
        """

        self._lastmodify_user_id = lastmodify_user_id

    @property
    def delivery(self):
        """Gets the delivery of this AuditLogReport.  # noqa: E501

        Whether or not the report is configured to be delivered via email. Acceptable values are: none, email  # noqa: E501

        :return: The delivery of this AuditLogReport.  # noqa: E501
        :rtype: str
        """
        return self._delivery

    @delivery.setter
    def delivery(self, delivery):
        """Sets the delivery of this AuditLogReport.

        Whether or not the report is configured to be delivered via email. Acceptable values are: none, email  # noqa: E501

        :param delivery: The delivery of this AuditLogReport.  # noqa: E501
        :type: str
        """

        self._delivery = delivery

    @property
    def user_permission(self):
        """Gets the user_permission of this AuditLogReport.  # noqa: E501

        The permissions associated with the user who made the API call  # noqa: E501

        :return: The user_permission of this AuditLogReport.  # noqa: E501
        :rtype: str
        """
        return self._user_permission

    @user_permission.setter
    def user_permission(self, user_permission):
        """Sets the user_permission of this AuditLogReport.

        The permissions associated with the user who made the API call  # noqa: E501

        :param user_permission: The user_permission of this AuditLogReport.  # noqa: E501
        :type: str
        """

        self._user_permission = user_permission

    @property
    def last_generate_on(self):
        """Gets the last_generate_on of this AuditLogReport.  # noqa: E501

        The time, in epoch format, that the report was last generated  # noqa: E501

        :return: The last_generate_on of this AuditLogReport.  # noqa: E501
        :rtype: int
        """
        return self._last_generate_on

    @last_generate_on.setter
    def last_generate_on(self, last_generate_on):
        """Sets the last_generate_on of this AuditLogReport.

        The time, in epoch format, that the report was last generated  # noqa: E501

        :param last_generate_on: The last_generate_on of this AuditLogReport.  # noqa: E501
        :type: int
        """

        self._last_generate_on = last_generate_on

    @property
    def report_link_num(self):
        """Gets the report_link_num of this AuditLogReport.  # noqa: E501

        The number of links associated with the report, where each link corresponds to a generated report  # noqa: E501

        :return: The report_link_num of this AuditLogReport.  # noqa: E501
        :rtype: int
        """
        return self._report_link_num

    @report_link_num.setter
    def report_link_num(self, report_link_num):
        """Sets the report_link_num of this AuditLogReport.

        The number of links associated with the report, where each link corresponds to a generated report  # noqa: E501

        :param report_link_num: The report_link_num of this AuditLogReport.  # noqa: E501
        :type: int
        """

        self._report_link_num = report_link_num

    @property
    def group_id(self):
        """Gets the group_id of this AuditLogReport.  # noqa: E501

        The Id of the group the report is in, where Id=0 is the root report group  # noqa: E501

        :return: The group_id of this AuditLogReport.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this AuditLogReport.

        The Id of the group the report is in, where Id=0 is the root report group  # noqa: E501

        :param group_id: The group_id of this AuditLogReport.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def format(self):
        """Gets the format of this AuditLogReport.  # noqa: E501

        The format of the report. Allowable values are: HTML, PDF, CSV, WORD  # noqa: E501

        :return: The format of this AuditLogReport.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this AuditLogReport.

        The format of the report. Allowable values are: HTML, PDF, CSV, WORD  # noqa: E501

        :param format: The format of this AuditLogReport.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def description(self):
        """Gets the description of this AuditLogReport.  # noqa: E501

        The description of the report  # noqa: E501

        :return: The description of this AuditLogReport.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AuditLogReport.

        The description of the report  # noqa: E501

        :param description: The description of this AuditLogReport.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def last_generate_size(self):
        """Gets the last_generate_size of this AuditLogReport.  # noqa: E501

        The size of the report, in Bytes, the last time it was generated  # noqa: E501

        :return: The last_generate_size of this AuditLogReport.  # noqa: E501
        :rtype: int
        """
        return self._last_generate_size

    @last_generate_size.setter
    def last_generate_size(self, last_generate_size):
        """Sets the last_generate_size of this AuditLogReport.

        The size of the report, in Bytes, the last time it was generated  # noqa: E501

        :param last_generate_size: The last_generate_size of this AuditLogReport.  # noqa: E501
        :type: int
        """

        self._last_generate_size = last_generate_size

    @property
    def custom_report_type_id(self):
        """Gets the custom_report_type_id of this AuditLogReport.  # noqa: E501

        The id of the custom report template, if the report is a custom report. An id of 0 indicates that the report is not a custom report  # noqa: E501

        :return: The custom_report_type_id of this AuditLogReport.  # noqa: E501
        :rtype: int
        """
        return self._custom_report_type_id

    @custom_report_type_id.setter
    def custom_report_type_id(self, custom_report_type_id):
        """Sets the custom_report_type_id of this AuditLogReport.

        The id of the custom report template, if the report is a custom report. An id of 0 indicates that the report is not a custom report  # noqa: E501

        :param custom_report_type_id: The custom_report_type_id of this AuditLogReport.  # noqa: E501
        :type: int
        """

        self._custom_report_type_id = custom_report_type_id

    @property
    def type(self):
        """Gets the type of this AuditLogReport.  # noqa: E501

        The report type. Acceptable values are: Alert,Alert SLA,Alert threshold,Alert trends,Host CPU,Host group inventory,Host inventory,Host metric trends,Interfaces Bandwidth,Netflow device metric,Service Level Agreement,Website Service Overview,Word template,Audit Log,Alert Forecasting,Dashboard,Website SLA,User,Role  # noqa: E501

        :return: The type of this AuditLogReport.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AuditLogReport.

        The report type. Acceptable values are: Alert,Alert SLA,Alert threshold,Alert trends,Host CPU,Host group inventory,Host inventory,Host metric trends,Interfaces Bandwidth,Netflow device metric,Service Level Agreement,Website Service Overview,Word template,Audit Log,Alert Forecasting,Dashboard,Website SLA,User,Role  # noqa: E501

        :param type: The type of this AuditLogReport.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def last_generate_pages(self):
        """Gets the last_generate_pages of this AuditLogReport.  # noqa: E501

        The number of pages in the report, the last time it was generated  # noqa: E501

        :return: The last_generate_pages of this AuditLogReport.  # noqa: E501
        :rtype: int
        """
        return self._last_generate_pages

    @last_generate_pages.setter
    def last_generate_pages(self, last_generate_pages):
        """Sets the last_generate_pages of this AuditLogReport.

        The number of pages in the report, the last time it was generated  # noqa: E501

        :param last_generate_pages: The last_generate_pages of this AuditLogReport.  # noqa: E501
        :type: int
        """

        self._last_generate_pages = last_generate_pages

    @property
    def schedule(self):
        """Gets the schedule of this AuditLogReport.  # noqa: E501

        A cron schedule that indicates when the report will be delivered via email  # noqa: E501

        :return: The schedule of this AuditLogReport.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this AuditLogReport.

        A cron schedule that indicates when the report will be delivered via email  # noqa: E501

        :param schedule: The schedule of this AuditLogReport.  # noqa: E501
        :type: str
        """

        self._schedule = schedule

    @property
    def recipients(self):
        """Gets the recipients of this AuditLogReport.  # noqa: E501

        If the report is configured to be delivered via email, this object provides the recipients that the report will be delivered to  # noqa: E501

        :return: The recipients of this AuditLogReport.  # noqa: E501
        :rtype: list[ReportRecipient]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this AuditLogReport.

        If the report is configured to be delivered via email, this object provides the recipients that the report will be delivered to  # noqa: E501

        :param recipients: The recipients of this AuditLogReport.  # noqa: E501
        :type: list[ReportRecipient]
        """

        self._recipients = recipients

    @property
    def custom_report_type_name(self):
        """Gets the custom_report_type_name of this AuditLogReport.  # noqa: E501

        The name of the custom report template  # noqa: E501

        :return: The custom_report_type_name of this AuditLogReport.  # noqa: E501
        :rtype: str
        """
        return self._custom_report_type_name

    @custom_report_type_name.setter
    def custom_report_type_name(self, custom_report_type_name):
        """Sets the custom_report_type_name of this AuditLogReport.

        The name of the custom report template  # noqa: E501

        :param custom_report_type_name: The custom_report_type_name of this AuditLogReport.  # noqa: E501
        :type: str
        """

        self._custom_report_type_name = custom_report_type_name

    @property
    def name(self):
        """Gets the name of this AuditLogReport.  # noqa: E501

        The name of the report  # noqa: E501

        :return: The name of this AuditLogReport.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AuditLogReport.

        The name of the report  # noqa: E501

        :param name: The name of this AuditLogReport.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def enable_view_as_other_user(self):
        """Gets the enable_view_as_other_user of this AuditLogReport.  # noqa: E501

        Whether or not other users are allowed to view the report as the user who last modified the report  # noqa: E501

        :return: The enable_view_as_other_user of this AuditLogReport.  # noqa: E501
        :rtype: bool
        """
        return self._enable_view_as_other_user

    @enable_view_as_other_user.setter
    def enable_view_as_other_user(self, enable_view_as_other_user):
        """Sets the enable_view_as_other_user of this AuditLogReport.

        Whether or not other users are allowed to view the report as the user who last modified the report  # noqa: E501

        :param enable_view_as_other_user: The enable_view_as_other_user of this AuditLogReport.  # noqa: E501
        :type: bool
        """

        self._enable_view_as_other_user = enable_view_as_other_user

    @property
    def lastmodify_user_name(self):
        """Gets the lastmodify_user_name of this AuditLogReport.  # noqa: E501

        The username of the user that last modified the report  # noqa: E501

        :return: The lastmodify_user_name of this AuditLogReport.  # noqa: E501
        :rtype: str
        """
        return self._lastmodify_user_name

    @lastmodify_user_name.setter
    def lastmodify_user_name(self, lastmodify_user_name):
        """Sets the lastmodify_user_name of this AuditLogReport.

        The username of the user that last modified the report  # noqa: E501

        :param lastmodify_user_name: The lastmodify_user_name of this AuditLogReport.  # noqa: E501
        :type: str
        """

        self._lastmodify_user_name = lastmodify_user_name

    @property
    def id(self):
        """Gets the id of this AuditLogReport.  # noqa: E501

        The id of the report  # noqa: E501

        :return: The id of this AuditLogReport.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuditLogReport.

        The id of the report  # noqa: E501

        :param id: The id of this AuditLogReport.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def schedule_timezone(self):
        """Gets the schedule_timezone of this AuditLogReport.  # noqa: E501

        The sepecific timezone for the scheduled report  # noqa: E501

        :return: The schedule_timezone of this AuditLogReport.  # noqa: E501
        :rtype: str
        """
        return self._schedule_timezone

    @schedule_timezone.setter
    def schedule_timezone(self, schedule_timezone):
        """Sets the schedule_timezone of this AuditLogReport.

        The sepecific timezone for the scheduled report  # noqa: E501

        :param schedule_timezone: The schedule_timezone of this AuditLogReport.  # noqa: E501
        :type: str
        """

        self._schedule_timezone = schedule_timezone

    @property
    def filter(self):
        """Gets the filter of this AuditLogReport.  # noqa: E501

        The filter setting for the report  # noqa: E501

        :return: The filter of this AuditLogReport.  # noqa: E501
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this AuditLogReport.

        The filter setting for the report  # noqa: E501

        :param filter: The filter of this AuditLogReport.  # noqa: E501
        :type: str
        """

        self._filter = filter

    @property
    def sorted_by(self):
        """Gets the sorted_by of this AuditLogReport.  # noqa: E501

        The sort option for the repor  # noqa: E501

        :return: The sorted_by of this AuditLogReport.  # noqa: E501
        :rtype: str
        """
        return self._sorted_by

    @sorted_by.setter
    def sorted_by(self, sorted_by):
        """Sets the sorted_by of this AuditLogReport.

        The sort option for the repor  # noqa: E501

        :param sorted_by: The sorted_by of this AuditLogReport.  # noqa: E501
        :type: str
        """

        self._sorted_by = sorted_by

    @property
    def date_range(self):
        """Gets the date_range of this AuditLogReport.  # noqa: E501

        The Time Range configured for the report: Last 2 hours | Last 24 hours | Last calendar day | Last 7 days | Last 14 days | Last 30 days | Last calendar month | Last 365 days | Any custom date range in this format: YYYY-MM-dd hh:mm TO YYYY-MM-dd hh:mm  # noqa: E501

        :return: The date_range of this AuditLogReport.  # noqa: E501
        :rtype: str
        """
        return self._date_range

    @date_range.setter
    def date_range(self, date_range):
        """Sets the date_range of this AuditLogReport.

        The Time Range configured for the report: Last 2 hours | Last 24 hours | Last calendar day | Last 7 days | Last 14 days | Last 30 days | Last calendar month | Last 365 days | Any custom date range in this format: YYYY-MM-dd hh:mm TO YYYY-MM-dd hh:mm  # noqa: E501

        :param date_range: The date_range of this AuditLogReport.  # noqa: E501
        :type: str
        """

        self._date_range = date_range

    @property
    def columns(self):
        """Gets the columns of this AuditLogReport.  # noqa: E501

        The columns displayed in the report  # noqa: E501

        :return: The columns of this AuditLogReport.  # noqa: E501
        :rtype: list[DynamicColumn]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this AuditLogReport.

        The columns displayed in the report  # noqa: E501

        :param columns: The columns of this AuditLogReport.  # noqa: E501
        :type: list[DynamicColumn]
        """

        self._columns = columns

    @property
    def username(self):
        """Gets the username of this AuditLogReport.  # noqa: E501

        The user name of the user filter setting for the report  # noqa: E501

        :return: The username of this AuditLogReport.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AuditLogReport.

        The user name of the user filter setting for the report  # noqa: E501

        :param username: The username of this AuditLogReport.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if issubclass(AuditLogReport, dict):
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
        if not isinstance(other, AuditLogReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
