import json
from uc3m_consulting.enterprise_project import EnterpriseProject
from uc3m_consulting.attributes.attribute_date import Date
from uc3m_consulting.storage.projects_json_store import ProjectsJsonStore
from uc3m_consulting.storage.documents_json_store import DocumentsJsonStore

class EnterpriseManager:
    def __init__(self):
        pass

    def register_project(self, company_cif, project_acronym, project_description,
                         department, date, budget):
        new_project = EnterpriseProject(company_cif, project_acronym, project_description,
                                        department, date, budget)
        storage = ProjectsJsonStore()
        storage.add_project(new_project)
        return new_project.project_id

    def find_docs(self, date_str):
        Date(date_str)
        storage = DocumentsJsonStore()
        return storage.count_and_report(date_str)