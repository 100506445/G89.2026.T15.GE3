from uc3m_consulting.attributes.attribute import Attribute
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException

class ProjectBudget(Attribute):
    """Clase para validar el presupuesto (Budget)"""
    def __init__(self, attr_value):
        super().__init__()
        self._attr_value = self._validate(attr_value)

    def _validate(self, value):
        try:
            budget_float = float(value)
        except ValueError as exc:
            raise EnterpriseManagementException("Invalid budget amount") from exc
        
        # Validación de decimales y rango
        budget_str = str(budget_float)
        if '.' in budget_str and len(budget_str.split('.')[1]) > 2:
            raise EnterpriseManagementException("Invalid budget amount")
        if budget_float < 50000 or budget_float > 1000000:
            raise EnterpriseManagementException("Invalid budget amount")
        return budget_float