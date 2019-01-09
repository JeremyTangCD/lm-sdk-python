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

from logicmonitor_sdk.models.authentication import Authentication  # noqa: F401,E501


class WebCheckStep(object):
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
        'schema': 'str',
        'resp_type': 'str',
        'http_headers': 'str',
        'auth': 'Authentication',
        'match_type': 'str',
        'description': 'str',
        'type': 'str',
        'timeout': 'int',
        'use_default_root': 'bool',
        'path': 'str',
        'http_method': 'str',
        'enable': 'bool',
        'http_version': 'str',
        'keyword': 'str',
        'resp_script': 'str',
        'label': 'str',
        'url': 'str',
        'invert_match': 'bool',
        'req_script': 'str',
        'http_body': 'str',
        'follow_redirection': 'bool',
        'post_data_edit_type': 'str',
        'name': 'str',
        'require_auth': 'bool',
        'req_type': 'str',
        'fullpage_load': 'bool',
        'status_code': 'str'
    }

    attribute_map = {
        'schema': 'schema',
        'resp_type': 'respType',
        'http_headers': 'HTTPHeaders',
        'auth': 'auth',
        'match_type': 'matchType',
        'description': 'description',
        'type': 'type',
        'timeout': 'timeout',
        'use_default_root': 'useDefaultRoot',
        'path': 'path',
        'http_method': 'HTTPMethod',
        'enable': 'enable',
        'http_version': 'HTTPVersion',
        'keyword': 'keyword',
        'resp_script': 'respScript',
        'label': 'label',
        'url': 'url',
        'invert_match': 'invertMatch',
        'req_script': 'reqScript',
        'http_body': 'HTTPBody',
        'follow_redirection': 'followRedirection',
        'post_data_edit_type': 'postDataEditType',
        'name': 'name',
        'require_auth': 'requireAuth',
        'req_type': 'reqType',
        'fullpage_load': 'fullpageLoad',
        'status_code': 'statusCode'
    }

    def __init__(self, schema=None, resp_type=None, http_headers=None, auth=None, match_type=None, description=None, type=None, timeout=None, use_default_root=None, path=None, http_method=None, enable=None, http_version=None, keyword=None, resp_script=None, label=None, url=None, invert_match=None, req_script=None, http_body=None, follow_redirection=None, post_data_edit_type=None, name=None, require_auth=None, req_type=None, fullpage_load=None, status_code=None):  # noqa: E501
        """WebCheckStep - a model defined in Swagger"""  # noqa: E501

        self._schema = None
        self._resp_type = None
        self._http_headers = None
        self._auth = None
        self._match_type = None
        self._description = None
        self._type = None
        self._timeout = None
        self._use_default_root = None
        self._path = None
        self._http_method = None
        self._enable = None
        self._http_version = None
        self._keyword = None
        self._resp_script = None
        self._label = None
        self._url = None
        self._invert_match = None
        self._req_script = None
        self._http_body = None
        self._follow_redirection = None
        self._post_data_edit_type = None
        self._name = None
        self._require_auth = None
        self._req_type = None
        self._fullpage_load = None
        self._status_code = None
        self.discriminator = None

        if schema is not None:
            self.schema = schema
        if resp_type is not None:
            self.resp_type = resp_type
        if http_headers is not None:
            self.http_headers = http_headers
        if auth is not None:
            self.auth = auth
        if match_type is not None:
            self.match_type = match_type
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if timeout is not None:
            self.timeout = timeout
        if use_default_root is not None:
            self.use_default_root = use_default_root
        if path is not None:
            self.path = path
        if http_method is not None:
            self.http_method = http_method
        if enable is not None:
            self.enable = enable
        if http_version is not None:
            self.http_version = http_version
        if keyword is not None:
            self.keyword = keyword
        if resp_script is not None:
            self.resp_script = resp_script
        if label is not None:
            self.label = label
        if url is not None:
            self.url = url
        if invert_match is not None:
            self.invert_match = invert_match
        if req_script is not None:
            self.req_script = req_script
        if http_body is not None:
            self.http_body = http_body
        if follow_redirection is not None:
            self.follow_redirection = follow_redirection
        if post_data_edit_type is not None:
            self.post_data_edit_type = post_data_edit_type
        if name is not None:
            self.name = name
        if require_auth is not None:
            self.require_auth = require_auth
        if req_type is not None:
            self.req_type = req_type
        if fullpage_load is not None:
            self.fullpage_load = fullpage_load
        if status_code is not None:
            self.status_code = status_code

    @property
    def schema(self):
        """Gets the schema of this WebCheckStep.  # noqa: E501


        :return: The schema of this WebCheckStep.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this WebCheckStep.


        :param schema: The schema of this WebCheckStep.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def resp_type(self):
        """Gets the resp_type of this WebCheckStep.  # noqa: E501


        :return: The resp_type of this WebCheckStep.  # noqa: E501
        :rtype: str
        """
        return self._resp_type

    @resp_type.setter
    def resp_type(self, resp_type):
        """Sets the resp_type of this WebCheckStep.


        :param resp_type: The resp_type of this WebCheckStep.  # noqa: E501
        :type: str
        """

        self._resp_type = resp_type

    @property
    def http_headers(self):
        """Gets the http_headers of this WebCheckStep.  # noqa: E501


        :return: The http_headers of this WebCheckStep.  # noqa: E501
        :rtype: str
        """
        return self._http_headers

    @http_headers.setter
    def http_headers(self, http_headers):
        """Sets the http_headers of this WebCheckStep.


        :param http_headers: The http_headers of this WebCheckStep.  # noqa: E501
        :type: str
        """

        self._http_headers = http_headers

    @property
    def auth(self):
        """Gets the auth of this WebCheckStep.  # noqa: E501


        :return: The auth of this WebCheckStep.  # noqa: E501
        :rtype: Authentication
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """Sets the auth of this WebCheckStep.


        :param auth: The auth of this WebCheckStep.  # noqa: E501
        :type: Authentication
        """

        self._auth = auth

    @property
    def match_type(self):
        """Gets the match_type of this WebCheckStep.  # noqa: E501


        :return: The match_type of this WebCheckStep.  # noqa: E501
        :rtype: str
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        """Sets the match_type of this WebCheckStep.


        :param match_type: The match_type of this WebCheckStep.  # noqa: E501
        :type: str
        """

        self._match_type = match_type

    @property
    def description(self):
        """Gets the description of this WebCheckStep.  # noqa: E501


        :return: The description of this WebCheckStep.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WebCheckStep.


        :param description: The description of this WebCheckStep.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def type(self):
        """Gets the type of this WebCheckStep.  # noqa: E501


        :return: The type of this WebCheckStep.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WebCheckStep.


        :param type: The type of this WebCheckStep.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def timeout(self):
        """Gets the timeout of this WebCheckStep.  # noqa: E501


        :return: The timeout of this WebCheckStep.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this WebCheckStep.


        :param timeout: The timeout of this WebCheckStep.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

    @property
    def use_default_root(self):
        """Gets the use_default_root of this WebCheckStep.  # noqa: E501


        :return: The use_default_root of this WebCheckStep.  # noqa: E501
        :rtype: bool
        """
        return self._use_default_root

    @use_default_root.setter
    def use_default_root(self, use_default_root):
        """Sets the use_default_root of this WebCheckStep.


        :param use_default_root: The use_default_root of this WebCheckStep.  # noqa: E501
        :type: bool
        """

        self._use_default_root = use_default_root

    @property
    def path(self):
        """Gets the path of this WebCheckStep.  # noqa: E501


        :return: The path of this WebCheckStep.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this WebCheckStep.


        :param path: The path of this WebCheckStep.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def http_method(self):
        """Gets the http_method of this WebCheckStep.  # noqa: E501


        :return: The http_method of this WebCheckStep.  # noqa: E501
        :rtype: str
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        """Sets the http_method of this WebCheckStep.


        :param http_method: The http_method of this WebCheckStep.  # noqa: E501
        :type: str
        """

        self._http_method = http_method

    @property
    def enable(self):
        """Gets the enable of this WebCheckStep.  # noqa: E501


        :return: The enable of this WebCheckStep.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this WebCheckStep.


        :param enable: The enable of this WebCheckStep.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def http_version(self):
        """Gets the http_version of this WebCheckStep.  # noqa: E501


        :return: The http_version of this WebCheckStep.  # noqa: E501
        :rtype: str
        """
        return self._http_version

    @http_version.setter
    def http_version(self, http_version):
        """Sets the http_version of this WebCheckStep.


        :param http_version: The http_version of this WebCheckStep.  # noqa: E501
        :type: str
        """

        self._http_version = http_version

    @property
    def keyword(self):
        """Gets the keyword of this WebCheckStep.  # noqa: E501


        :return: The keyword of this WebCheckStep.  # noqa: E501
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this WebCheckStep.


        :param keyword: The keyword of this WebCheckStep.  # noqa: E501
        :type: str
        """

        self._keyword = keyword

    @property
    def resp_script(self):
        """Gets the resp_script of this WebCheckStep.  # noqa: E501


        :return: The resp_script of this WebCheckStep.  # noqa: E501
        :rtype: str
        """
        return self._resp_script

    @resp_script.setter
    def resp_script(self, resp_script):
        """Sets the resp_script of this WebCheckStep.


        :param resp_script: The resp_script of this WebCheckStep.  # noqa: E501
        :type: str
        """

        self._resp_script = resp_script

    @property
    def label(self):
        """Gets the label of this WebCheckStep.  # noqa: E501


        :return: The label of this WebCheckStep.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this WebCheckStep.


        :param label: The label of this WebCheckStep.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def url(self):
        """Gets the url of this WebCheckStep.  # noqa: E501


        :return: The url of this WebCheckStep.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WebCheckStep.


        :param url: The url of this WebCheckStep.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def invert_match(self):
        """Gets the invert_match of this WebCheckStep.  # noqa: E501


        :return: The invert_match of this WebCheckStep.  # noqa: E501
        :rtype: bool
        """
        return self._invert_match

    @invert_match.setter
    def invert_match(self, invert_match):
        """Sets the invert_match of this WebCheckStep.


        :param invert_match: The invert_match of this WebCheckStep.  # noqa: E501
        :type: bool
        """

        self._invert_match = invert_match

    @property
    def req_script(self):
        """Gets the req_script of this WebCheckStep.  # noqa: E501


        :return: The req_script of this WebCheckStep.  # noqa: E501
        :rtype: str
        """
        return self._req_script

    @req_script.setter
    def req_script(self, req_script):
        """Sets the req_script of this WebCheckStep.


        :param req_script: The req_script of this WebCheckStep.  # noqa: E501
        :type: str
        """

        self._req_script = req_script

    @property
    def http_body(self):
        """Gets the http_body of this WebCheckStep.  # noqa: E501


        :return: The http_body of this WebCheckStep.  # noqa: E501
        :rtype: str
        """
        return self._http_body

    @http_body.setter
    def http_body(self, http_body):
        """Sets the http_body of this WebCheckStep.


        :param http_body: The http_body of this WebCheckStep.  # noqa: E501
        :type: str
        """

        self._http_body = http_body

    @property
    def follow_redirection(self):
        """Gets the follow_redirection of this WebCheckStep.  # noqa: E501


        :return: The follow_redirection of this WebCheckStep.  # noqa: E501
        :rtype: bool
        """
        return self._follow_redirection

    @follow_redirection.setter
    def follow_redirection(self, follow_redirection):
        """Sets the follow_redirection of this WebCheckStep.


        :param follow_redirection: The follow_redirection of this WebCheckStep.  # noqa: E501
        :type: bool
        """

        self._follow_redirection = follow_redirection

    @property
    def post_data_edit_type(self):
        """Gets the post_data_edit_type of this WebCheckStep.  # noqa: E501


        :return: The post_data_edit_type of this WebCheckStep.  # noqa: E501
        :rtype: str
        """
        return self._post_data_edit_type

    @post_data_edit_type.setter
    def post_data_edit_type(self, post_data_edit_type):
        """Sets the post_data_edit_type of this WebCheckStep.


        :param post_data_edit_type: The post_data_edit_type of this WebCheckStep.  # noqa: E501
        :type: str
        """

        self._post_data_edit_type = post_data_edit_type

    @property
    def name(self):
        """Gets the name of this WebCheckStep.  # noqa: E501


        :return: The name of this WebCheckStep.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WebCheckStep.


        :param name: The name of this WebCheckStep.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def require_auth(self):
        """Gets the require_auth of this WebCheckStep.  # noqa: E501


        :return: The require_auth of this WebCheckStep.  # noqa: E501
        :rtype: bool
        """
        return self._require_auth

    @require_auth.setter
    def require_auth(self, require_auth):
        """Sets the require_auth of this WebCheckStep.


        :param require_auth: The require_auth of this WebCheckStep.  # noqa: E501
        :type: bool
        """

        self._require_auth = require_auth

    @property
    def req_type(self):
        """Gets the req_type of this WebCheckStep.  # noqa: E501


        :return: The req_type of this WebCheckStep.  # noqa: E501
        :rtype: str
        """
        return self._req_type

    @req_type.setter
    def req_type(self, req_type):
        """Sets the req_type of this WebCheckStep.


        :param req_type: The req_type of this WebCheckStep.  # noqa: E501
        :type: str
        """

        self._req_type = req_type

    @property
    def fullpage_load(self):
        """Gets the fullpage_load of this WebCheckStep.  # noqa: E501


        :return: The fullpage_load of this WebCheckStep.  # noqa: E501
        :rtype: bool
        """
        return self._fullpage_load

    @fullpage_load.setter
    def fullpage_load(self, fullpage_load):
        """Sets the fullpage_load of this WebCheckStep.


        :param fullpage_load: The fullpage_load of this WebCheckStep.  # noqa: E501
        :type: bool
        """

        self._fullpage_load = fullpage_load

    @property
    def status_code(self):
        """Gets the status_code of this WebCheckStep.  # noqa: E501


        :return: The status_code of this WebCheckStep.  # noqa: E501
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this WebCheckStep.


        :param status_code: The status_code of this WebCheckStep.  # noqa: E501
        :type: str
        """

        self._status_code = status_code

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
        if issubclass(WebCheckStep, dict):
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
        if not isinstance(other, WebCheckStep):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
