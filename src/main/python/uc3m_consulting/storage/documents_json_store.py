import json
from datetime import datetime, timezone
from freezegun import freeze_time
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException
from uc3m_consulting.enterprise_manager_config import TEST_DOCUMENTS_STORE_FILE, TEST_NUMDOCS_STORE_FILE
from uc3m_consulting.project_document import ProjectDocument

class DocumentsJsonStore:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DocumentsJsonStore, cls).__new__(cls)
            cls._instance._input_file = TEST_DOCUMENTS_STORE_FILE
            cls._instance._output_file = TEST_NUMDOCS_STORE_FILE
        return cls._instance

    def count_and_report(self, date_str):
        documents_list = self._load_documents()
        document_count = 0

        for document in documents_list:
            timestamp = document["register_date"]
            document_date_str = datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y")

            if document_date_str == date_str:
                document_datetime = datetime.fromtimestamp(timestamp, tz=timezone.utc)
                with freeze_time(document_datetime):
                    document_obj = ProjectDocument(document["project_id"], document["file_name"])
                    if document_obj.document_signature == document["document_signature"]:
                        document_count += 1
                    else:
                        raise EnterpriseManagementException("Inconsistent document signature")

        if document_count == 0:
            raise EnterpriseManagementException("No documents found")

        self._save_report(date_str, document_count)
        return document_count

    def _load_documents(self):
        try:
            with open(self._input_file, "r", encoding="utf-8", newline="") as file:
                return json.load(file)
        except FileNotFoundError as ex:
            raise EnterpriseManagementException("Wrong file  or file path") from ex

    def _save_report(self, date_str, count):
        report_entry = {
            "Querydate": date_str,
            "ReportDate": datetime.now(timezone.utc).timestamp(),
            "Numfiles": count
        }
        try:
            with open(self._output_file, "r", encoding="utf-8", newline="") as file:
                reports_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            reports_list = []
        
        reports_list.append(report_entry)
        
        try:
            with open(self._output_file, "w", encoding="utf-8", newline="") as file:
                json.dump(reports_list, file, indent=2)
        except FileNotFoundError as ex:
            raise EnterpriseManagementException("Wrong file  or file path") from ex