"""Módulo con la clase base Attribute"""
import re
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException

class Attribute:
    """Clase genérica para validar atributos"""
    def __init__(self):
        self._attr_value = ""
        self._error_message = ""
        self._validation_pattern = r""

    def _validate(self, value):
        """Valida el valor contra el patrón regex"""
        myregex = re.compile(self._validation_pattern)
        res = myregex.fullmatch(value)
        if not res:
            raise EnterpriseManagementException(self._error_message)
        return value

    @property
    def value(self):
        """Devuelve el valor validado"""
        return self._attr_value

    @value.setter
    def value(self, attr_value):
        self._attr_value = attr_value