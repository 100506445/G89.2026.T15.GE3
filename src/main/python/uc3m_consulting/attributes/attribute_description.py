"""Módulo para la validación de la descripción del proyecto"""
from uc3m_consulting.attributes.attribute import Attribute

class ProjectDescription(Attribute):
    """Clase hija para validar la descripción"""
    def __init__(self, attr_value):
        super().__init__()
        self._validation_pattern = r"^.{10,30}$"
        self._error_message = "Invalid description format"
        self._attr_value = self._validate(attr_value)