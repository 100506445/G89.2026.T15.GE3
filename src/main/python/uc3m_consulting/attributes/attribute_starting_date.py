"""Module containing the StartingDate class"""
from datetime import datetime, timezone
from uc3m_consulting.attributes.attribute_date import Date
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException


#pylint: disable=too-few-public-methods
class StartingDate(Date):
    """Class for validating project starting date"""

    def __init__(self, attr_value):
        """Initializes and validates the project starting date"""
        super().__init__(attr_value)
        self._attr_value = self._validate_future(attr_value)

    def _validate_future(self, value):
        """Validates that the date is in the future"""
        try:
            parsed_date = datetime.strptime(value, "%d/%m/%Y").date()
        except ValueError as ex:
            raise EnterpriseManagementException("Invalid date format") from ex

        if parsed_date < datetime.now(timezone.utc).date():
            raise EnterpriseManagementException("Project's date must be today or later.")

        if parsed_date.year < 2025 or parsed_date.year > 2050:
            raise EnterpriseManagementException("Invalid date format")

        return value