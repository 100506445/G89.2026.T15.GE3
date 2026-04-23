"""Module containing the Date class"""
from uc3m_consulting.attributes.attribute import Attribute


#pylint: disable=too-few-public-methods
class Date(Attribute):
    """Class for validating date format"""

    def __init__(self, attr_value):
        """Initializes and validates the date"""
        super().__init__()
        self._validation_pattern = r"^(([0-2]\d|3[0-1])\/(0\d|1[0-2])\/\d\d\d\d)$"
        self._error_message = "Invalid date format"
        self._attr_value = self._validate(attr_value)