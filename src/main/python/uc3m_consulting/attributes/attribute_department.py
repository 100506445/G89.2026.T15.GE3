"""Module containing the ProjectDepartment class"""
from uc3m_consulting.attributes.attribute import Attribute


#pylint: disable=too-few-public-methods
class ProjectDepartment(Attribute):
    """Class for validating project department"""

    def __init__(self, attr_value):
        """Initializes and validates the project department"""
        super().__init__()
        self._validation_pattern = r"(HR|FINANCE|LEGAL|LOGISTICS)"
        self._error_message = "Invalid department"
        self._attr_value = self._validate(attr_value)
