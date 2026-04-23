"""Module containing the ProjectsJsonStore class"""
import json
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException
from uc3m_consulting.enterprise_manager_config import PROJECTS_STORE_FILE


class ProjectsJsonStore:
    """Class for managing projects JSON storage"""

    _instance = None

    def __init__(self):
        """Initializes ProjectsJsonStore instance variables"""
        self._file_path = PROJECTS_STORE_FILE

    def __new__(cls):
        """Creates a single instance of ProjectsJsonStore (Singleton)"""
        if cls._instance is None:
            cls._instance = super(ProjectsJsonStore, cls).__new__(cls)
            cls._instance._file_path = PROJECTS_STORE_FILE
        return cls._instance

    def add_project(self, project):
        """Adds a new project to the JSON store"""
        data_list = self._load_data()
        for item in data_list:
            if item["project_id"] == project.project_id:
                raise EnterpriseManagementException("Duplicated project in projects list")
        data_list.append(project.to_json())
        self._save_data(data_list)

    def _load_data(self):
        """Loads the projects list from the JSON store file"""
        try:
            with open(self._file_path, "r", encoding="utf-8", newline="") as file:
                data_list = json.load(file)
        except FileNotFoundError:
            data_list = []
        except json.JSONDecodeError as ex:
            raise EnterpriseManagementException("JSON Decode Error - Wrong JSON Format") from ex
        return data_list

    def _save_data(self, data_list):
        """Saves the projects list to the JSON store file"""
        try:
            with open(self._file_path, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise EnterpriseManagementException("Wrong file or file path") from ex
