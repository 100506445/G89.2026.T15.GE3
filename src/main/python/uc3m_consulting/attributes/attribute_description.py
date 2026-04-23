"""Module containing the ProjectDescription class"""
from uc3m_consulting.attributes.attribute import Attribute


#pylint: disable=too-few-public-methods
class ProjectDescription(Attribute):
    """Class for validating project description"""

    def __init__(self, attr_value):
        """Initializes and validates the project description"""
        super().__init__()
        self._validation_pattern = r"^.{10,30}$"
        self._error_message = "Invalid description format"
        self._attr_value = self._validate(attr_value)
