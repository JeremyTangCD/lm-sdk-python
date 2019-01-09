# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RestRole(object):
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
        'enable_remote_session_in_company_level': 'bool',
        'custom_help_label': 'str',
        'custom_help_url': 'str',
        'privileges': 'list[RestPrivilege]',
        'associated_user_count': 'int',
        'name': 'str',
        'description': 'str',
        'id': 'int',
        'two_fa_required': 'bool',
        'require_eula': 'bool'
    }

    attribute_map = {
        'enable_remote_session_in_company_level': 'enableRemoteSessionInCompanyLevel',
        'custom_help_label': 'customHelpLabel',
        'custom_help_url': 'customHelpURL',
        'privileges': 'privileges',
        'associated_user_count': 'associatedUserCount',
        'name': 'name',
        'description': 'description',
        'id': 'id',
        'two_fa_required': 'twoFARequired',
        'require_eula': 'requireEULA'
    }

    def __init__(self, enable_remote_session_in_company_level=None, custom_help_label=None, custom_help_url=None, privileges=None, associated_user_count=None, name=None, description=None, id=None, two_fa_required=None, require_eula=None):
        """
        RestRole - a model defined in Swagger
        """

        self._enable_remote_session_in_company_level = None
        self._custom_help_label = None
        self._custom_help_url = None
        self._privileges = None
        self._associated_user_count = None
        self._name = None
        self._description = None
        self._id = None
        self._two_fa_required = None
        self._require_eula = None

        if enable_remote_session_in_company_level is not None:
          self.enable_remote_session_in_company_level = enable_remote_session_in_company_level
        if custom_help_label is not None:
          self.custom_help_label = custom_help_label
        if custom_help_url is not None:
          self.custom_help_url = custom_help_url
        self.privileges = privileges
        if associated_user_count is not None:
          self.associated_user_count = associated_user_count
        self.name = name
        if description is not None:
          self.description = description
        if id is not None:
          self.id = id
        if two_fa_required is not None:
          self.two_fa_required = two_fa_required
        if require_eula is not None:
          self.require_eula = require_eula

    @property
    def enable_remote_session_in_company_level(self):
        """
        Gets the enable_remote_session_in_company_level of this RestRole.

        :return: The enable_remote_session_in_company_level of this RestRole.
        :rtype: bool
        """
        return self._enable_remote_session_in_company_level

    @enable_remote_session_in_company_level.setter
    def enable_remote_session_in_company_level(self, enable_remote_session_in_company_level):
        """
        Sets the enable_remote_session_in_company_level of this RestRole.

        :param enable_remote_session_in_company_level: The enable_remote_session_in_company_level of this RestRole.
        :type: bool
        """

        self._enable_remote_session_in_company_level = enable_remote_session_in_company_level

    @property
    def custom_help_label(self):
        """
        Gets the custom_help_label of this RestRole.

        :return: The custom_help_label of this RestRole.
        :rtype: str
        """
        return self._custom_help_label

    @custom_help_label.setter
    def custom_help_label(self, custom_help_label):
        """
        Sets the custom_help_label of this RestRole.

        :param custom_help_label: The custom_help_label of this RestRole.
        :type: str
        """

        self._custom_help_label = custom_help_label

    @property
    def custom_help_url(self):
        """
        Gets the custom_help_url of this RestRole.

        :return: The custom_help_url of this RestRole.
        :rtype: str
        """
        return self._custom_help_url

    @custom_help_url.setter
    def custom_help_url(self, custom_help_url):
        """
        Sets the custom_help_url of this RestRole.

        :param custom_help_url: The custom_help_url of this RestRole.
        :type: str
        """

        self._custom_help_url = custom_help_url

    @property
    def privileges(self):
        """
        Gets the privileges of this RestRole.

        :return: The privileges of this RestRole.
        :rtype: list[RestPrivilege]
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        """
        Sets the privileges of this RestRole.

        :param privileges: The privileges of this RestRole.
        :type: list[RestPrivilege]
        """
        if privileges is None:
            raise ValueError("Invalid value for `privileges`, must not be `None`")

        self._privileges = privileges

    @property
    def associated_user_count(self):
        """
        Gets the associated_user_count of this RestRole.

        :return: The associated_user_count of this RestRole.
        :rtype: int
        """
        return self._associated_user_count

    @associated_user_count.setter
    def associated_user_count(self, associated_user_count):
        """
        Sets the associated_user_count of this RestRole.

        :param associated_user_count: The associated_user_count of this RestRole.
        :type: int
        """

        self._associated_user_count = associated_user_count

    @property
    def name(self):
        """
        Gets the name of this RestRole.

        :return: The name of this RestRole.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RestRole.

        :param name: The name of this RestRole.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this RestRole.

        :return: The description of this RestRole.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this RestRole.

        :param description: The description of this RestRole.
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """
        Gets the id of this RestRole.

        :return: The id of this RestRole.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RestRole.

        :param id: The id of this RestRole.
        :type: int
        """

        self._id = id

    @property
    def two_fa_required(self):
        """
        Gets the two_fa_required of this RestRole.

        :return: The two_fa_required of this RestRole.
        :rtype: bool
        """
        return self._two_fa_required

    @two_fa_required.setter
    def two_fa_required(self, two_fa_required):
        """
        Sets the two_fa_required of this RestRole.

        :param two_fa_required: The two_fa_required of this RestRole.
        :type: bool
        """

        self._two_fa_required = two_fa_required

    @property
    def require_eula(self):
        """
        Gets the require_eula of this RestRole.

        :return: The require_eula of this RestRole.
        :rtype: bool
        """
        return self._require_eula

    @require_eula.setter
    def require_eula(self, require_eula):
        """
        Sets the require_eula of this RestRole.

        :param require_eula: The require_eula of this RestRole.
        :type: bool
        """

        self._require_eula = require_eula

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
        if not isinstance(other, RestRole):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other