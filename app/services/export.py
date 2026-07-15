from io import BytesIO
from typing import Sequence

from openpyxl import Workbook

from app.models.document import Document

class ExcelExporter:
    """
    Builds Excel workbooks for document export
    """
    
    def __init__(self, documents: Sequence[Document]):
        self.documents = documents
        
    def build(self) -> BytesIO:
        """
        Build the workbook and return it as an in-memory stream.
        """
        workbook = Workbook()
        worksheet = workbook.active
        worksheet.title = "Documents"
        
        self._build_header(worksheet)
        self._populate_rows(worksheet)
        
        output = BytesIO()
        workbook.save(output)
        output.seek(0)
        
        return output
    
    def _build_header(self, worksheet):
        pass
    
    def _populate_rows(self, worksheet):
        pass
    