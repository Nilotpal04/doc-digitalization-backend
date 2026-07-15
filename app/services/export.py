from io import BytesIO
from typing import Sequence

from openpyxl import Workbook

from app.models.document import Document

from openpyxl.styles import Font, PatternFill, Alignment

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
        headers = [
        "ID",
        "Extracted Data",
        "Original Document",
        "Uploaded By",
        "Uploaded At",
        "Status",
        ]

        header_fill = PatternFill(
            fill_type="solid",
            start_color="1F4E78",
            end_color="1F4E78",
        )

        header_font = Font(
            bold=True,
            color="FFFFFF",
        )

        for col, title in enumerate(headers, start=1):
            cell = worksheet.cell(row=1, column=col)

            cell.value = title
            cell.font = header_font
            cell.fill = header_fill

            cell.alignment = Alignment(
                horizontal="center",
                vertical="center",
            )

        worksheet.freeze_panes = "A2"

        worksheet.column_dimensions["A"].width = 10
        worksheet.column_dimensions["B"].width = 45
        worksheet.column_dimensions["C"].width = 35
        worksheet.column_dimensions["D"].width = 20
        worksheet.column_dimensions["E"].width = 20
        worksheet.column_dimensions["F"].width = 15
    
    def _populate_rows(self, worksheet):
        pass
    