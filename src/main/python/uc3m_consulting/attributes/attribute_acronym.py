"""Module containing the ProjectAcronym class"""
from uc3m_consulting.attributes.attribute import Attribute


#pylint: disable=too-few-public-methods
class ProjectAcronym(Attribute):
    """Class for validating project acronym"""

    def __init__(self, attr_value):
        """Initializes and validates the project acronym"""
        super().__init__()
        self._validation_pattern = r"^[a-zA-Z0-9]{5,10}$"
        self._error_message = "Invalid acronym"
        self._attr_value = self._validate(attr_value)