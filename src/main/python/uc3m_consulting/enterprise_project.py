"""Module containing the EnterpriseProject class"""
import hashlib
import json
from datetime import datetime, timezone
from uc3m_consulting.attributes.attribute_acronym import ProjectAcronym
from uc3m_consulting.attributes.attribute_description import ProjectDescription
from uc3m_consulting.attributes.attribute_department import ProjectDepartment
from uc3m_consulting.attributes.attribute_budget import ProjectBudget
from uc3m_consulting.attributes.attribute_cif import CompanyCif
from uc3m_consulting.attributes.attribute_starting_date import StartingDate


class EnterpriseProject:
    """Class representing a project"""

    #pylint: disable=too-many-arguments, too-many-positional-arguments
    def __init__(self,
                 company_cif: str,
                 project_acronym: str,
                 project_description: str,
                 department: str,
                 starting_date: str,
                 project_budget: float):
        """Initializes a new EnterpriseProject instance"""
        self.__company_cif = CompanyCif(company_cif).value
        self.__project_description = ProjectDescription(project_description).value
        self.__project_achronym = ProjectAcronym(project_acronym).value
        self.__department = ProjectDepartment(department).value
        self.__starting_date = StartingDate(starting_date).value
        self.__project_budget = ProjectBudget(project_budget).value
        justnow = datetime.now(timezone.utc)
        self.__time_stamp = datetime.timestamp(justnow)

    def __str__(self):
        """Returns string representation of the project"""
        return "Project:" + json.dumps(self.__dict__)

    def to_json(self):
        """Returns the object information in json format"""
        return {
            "company_cif": self.__company_cif,
            "project_description": self.__project_description,
            "project_acronym": self.__project_achronym,
            "project_budget": self.__project_budget,
            "department": self.__department,
            "starting_date": self.__starting_date,
            "time_stamp": self.__time_stamp,
            "project_id": self.project_id
        }

    @property
    def project_id(self):
        """Returns the md5 signature of the project"""
        return hashlib.md5(str(self).encode()).hexdigest()

    @property
    def company_cif(self):
        """Property representing the company CIF"""
        return self.__company_cif

    @property
    def starting_date(self):
        """Property representing the project starting date"""
        return self.__starting_date
