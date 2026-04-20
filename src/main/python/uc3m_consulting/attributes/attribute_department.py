"""Módulo para la validación del departamento"""
from uc3m_consulting.attributes.attribute import Attribute

class ProjectDepartment(Attribute):
    """Clase hija para validar el departamento"""
    def __init__(self, attr_value):
        super().__init__()
        self._validation_pattern = r"(HR|FINANCE|LEGAL|LOGISTICS)"
        self._error_message = "Invalid department"
        self._attr_value = self._validate(attr_value)