"""Módulo para la validación del CIF de la empresa"""
import re
from uc3m_consulting.attributes.attribute import Attribute
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException

class CompanyCif(Attribute):
    """Clase para validar el CIF con lógica matemática"""
    def __init__(self, attr_value):
        super().__init__()
        # 1. Validación básica de formato
        self._validation_pattern = r"^[ABCDEFGHJKNPQRSUVW]\d{7}[0-9A-J]$"
        self._error_message = "Invalid CIF format"
        self._attr_value = self._validate(attr_value)

    def _validate(self, value):
        # Primero comprobamos que sea un string (como hacía el manager)
        if not isinstance(value, str):
            raise EnterpriseManagementException("CIF code must be a string")
        
        # Validación por regex (clase padre)
        super()._validate(value)

        # 2. Lógica matemática del CIF (extraída del manager)
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
        
        self._validate_control(cif_letter, remainder, control_char)
        return value

    def _validate_control(self, cif_letter, remainder, control_char):
        """Comprueba el dígito o letra de control"""
        control_letters = "JABCDEFGHI"
        if cif_letter in ('A', 'B', 'E', 'H'):
            if str(remainder) != control_char:
                raise EnterpriseManagementException("Invalid CIF character control number")
        elif cif_letter in ('P', 'Q', 'S', 'K'):
            if control_letters[remainder] != control_char:
                raise EnterpriseManagementException("Invalid CIF character control letter")
        elif cif_letter not in ('A', 'B', 'E', 'H', 'P', 'Q', 'S', 'K'):
            # Para el resto de letras aceptadas por el regex pero no validadas específicamente
            pass