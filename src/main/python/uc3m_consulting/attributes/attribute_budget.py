"""Module containing the ProjectBudget class"""
from uc3m_consulting.attributes.attribute import Attribute
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException


#pylint: disable=too-few-public-methods
class ProjectBudget(Attribute):
    """Class for validating project budget"""

    def __init__(self, attr_value):
        """Initializes and validates the project budget"""
        super().__init__()
        self._attr_value = self._validate(attr_value)

    def _validate(self, value):
        """Validates the budget amount"""
        try:
            budget_float = float(value)
        except ValueError as exc:
            raise EnterpriseManagementException("Invalid budget amount") from exc

        budget_str = str(budget_float)
        if '.' in budget_str and len(budget_str.split('.')[1]) > 2:
            raise EnterpriseManagementException("Invalid budget amount")
        if budget_float < 50000 or budget_float > 1000000:
            raise EnterpriseManagementException("Invalid budget amount")
        return budget_float
