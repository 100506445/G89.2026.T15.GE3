"""Module containing the base Attribute class"""
import re
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException


#pylint: disable=too-few-public-methods
class Attribute:
    """Base class for validating attributes"""

    def __init__(self):
        """Initializes the Attribute with default values"""
        self._attr_value = ""
        self._error_message = ""
        self._validation_pattern = r""

    def _validate(self, value):
        """Validates the value against the regex pattern"""
        myregex = re.compile(self._validation_pattern)
        res = myregex.fullmatch(value)
        if not res:
            raise EnterpriseManagementException(self._error_message)
        return value

    @property
    def value(self):
        """Returns the validated value"""
        return self._attr_value

    @value.setter
    def value(self, attr_value):
        """Sets the attribute value"""
        self._attr_value = attr_value