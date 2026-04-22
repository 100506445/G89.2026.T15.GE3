from uc3m_consulting.attributes.attribute import Attribute
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException

class CompanyCif(Attribute):
    def __init__(self, attr_value):
        super().__init__()
        self._validation_pattern = r"^[ABCDEFGHJKNPQRSUVW]\d{7}[0-9A-J]$"
        self._error_message = "Invalid CIF format"
        self._attr_value = self._validate(attr_value)

    def _validate(self, value):
        if not isinstance(value, str):
            raise EnterpriseManagementException("CIF code must be a string")
        
        super()._validate(value)

        cif_letter = value[0]
        digits = value[1:8]
        control_char = value[8]

        odd_sum = 0
        even_sum = 0
        for i, digit in enumerate(digits):
            if i % 2 == 0:
                doubled = int(digit) * 2
                odd_sum += (doubled // 10) + (doubled % 10) if doubled > 9 else doubled
            else:
                even_sum += int(digit)

        total = odd_sum + even_sum
        remainder = (10 - (total % 10)) % 10
        
        control_letters = "JABCDEFGHI"
        if cif_letter in ('A', 'B', 'E', 'H'):
            if str(remainder) != control_char:
                raise EnterpriseManagementException("Invalid CIF character control number")
        elif cif_letter in ('P', 'Q', 'S', 'K'):
            if control_letters[remainder] != control_char:
                raise EnterpriseManagementException("Invalid CIF character control letter")
                
        return value