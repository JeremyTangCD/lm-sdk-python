# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RestAlertPagination(object):
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
        'total': 'int',
        'search_id': 'str',
        'items': 'list[RestAlert]'
    }

    attribute_map = {
        'total': 'total',
        'search_id': 'searchId',
        'items': 'items'
    }

    def __init__(self, total=None, search_id=None, items=None):
        """
        RestAlertPagination - a model defined in Swagger
        """

        self._total = None
        self._search_id = None
        self._items = None

        if total is not None:
          self.total = total
        if search_id is not None:
          self.search_id = search_id
        if items is not None:
          self.items = items

    @property
    def total(self):
        """
        Gets the total of this RestAlertPagination.

        :return: The total of this RestAlertPagination.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this RestAlertPagination.

        :param total: The total of this RestAlertPagination.
        :type: int
        """

        self._total = total

    @property
    def search_id(self):
        """
        Gets the search_id of this RestAlertPagination.

        :return: The search_id of this RestAlertPagination.
        :rtype: str
        """
        return self._search_id

    @search_id.setter
    def search_id(self, search_id):
        """
        Sets the search_id of this RestAlertPagination.

        :param search_id: The search_id of this RestAlertPagination.
        :type: str
        """

        self._search_id = search_id

    @property
    def items(self):
        """
        Gets the items of this RestAlertPagination.

        :return: The items of this RestAlertPagination.
        :rtype: list[RestAlert]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this RestAlertPagination.

        :param items: The items of this RestAlertPagination.
        :type: list[RestAlert]
        """

        self._items = items

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
        if not isinstance(other, RestAlertPagination):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
