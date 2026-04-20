"""Módulo para la validación del acrónimo del proyecto"""
from uc3m_consulting.attributes.attribute import Attribute

class ProjectAcronym(Attribute):
    """Clase hija para validar el acrónimo"""
    def __init__(self, attr_value):
        super().__init__()
        self._validation_pattern = r"^[a-zA-Z0-9]{5,10}$"
        self._error_message = "Invalid acronym"
        self._attr_value = self._validate(attr_value)