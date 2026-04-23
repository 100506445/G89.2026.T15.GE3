"""Module containing the EnterpriseManager class"""
from uc3m_consulting.enterprise_project import EnterpriseProject
from uc3m_consulting.attributes.attribute_date import Date
from uc3m_consulting.storage.projects_json_store import ProjectsJsonStore
from uc3m_consulting.storage.documents_json_store import DocumentsJsonStore


class EnterpriseManager:
    """Class for managing enterprise projects and documents"""

    _instance = None

    def __new__(cls):
        """Creates a single instance of EnterpriseManager (Singleton)"""
        if cls._instance is None:
            cls._instance = super(EnterpriseManager, cls).__new__(cls)
        return cls._instance

    #pylint: disable=too-many-arguments, too-many-positional-arguments
    def register_project(self, company_cif, project_acronym, project_description,
                         department, date, budget):
        """Registers a new project in the system"""
        new_project = EnterpriseProject(company_cif, project_acronym, project_description,
                                        department, date, budget)
        storage = ProjectsJsonStore()
        storage.add_project(new_project)
        return new_project.project_id

    def find_docs(self, date_str):
        """Finds and counts documents for a specific date"""
        Date(date_str)
        storage = DocumentsJsonStore()
        return storage.count_and_report(date_str)
