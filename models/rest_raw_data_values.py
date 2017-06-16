# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RestRawDataValues(object):
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
        'values': 'list[list[float]]',
        'time': 'list[int]'
    }

    attribute_map = {
        'values': 'values',
        'time': 'time'
    }

    def __init__(self, values=None, time=None):
        """
        RestRawDataValues - a model defined in Swagger
        """

        self._values = None
        self._time = None

        if values is not None:
          self.values = values
        if time is not None:
          self.time = time

    @property
    def values(self):
        """
        Gets the values of this RestRawDataValues.

        :return: The values of this RestRawDataValues.
        :rtype: list[list[float]]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this RestRawDataValues.

        :param values: The values of this RestRawDataValues.
        :type: list[list[float]]
        """

        self._values = values

    @property
    def time(self):
        """
        Gets the time of this RestRawDataValues.

        :return: The time of this RestRawDataValues.
        :rtype: list[int]
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this RestRawDataValues.

        :param time: The time of this RestRawDataValues.
        :type: list[int]
        """

        self._time = time

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
        if not isinstance(other, RestRawDataValues):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
