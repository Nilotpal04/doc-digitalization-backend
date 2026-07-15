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
        row = 2

        for document in self.documents:
            worksheet.cell(row=row, column=1).value = document.id

            # Extracted data
            worksheet.cell(
                row=row,
                column=2,
            ).value = self._format_extracted_data(document.extracted_data)
            
            # Column 3 (Original Document)
            worksheet.cell(row=row, column=3).value = ""
            
            # Uploaded By
            worksheet.cell(
                row=row,
                column=4,
            ).value = document.uploader.username
            
            # Uploaded At
            worksheet.cell(
                row=row,
                column=5,
            ).value = document.uploaded_at.strftime("%d-%m-%Y %H:%M")
            
            # Status
            worksheet.cell(
                row=row,
                column=6,
            ).value = document.status.value.capitalize()
            
            worksheet.cell(
                row=row,
                column=2,
            ).alignment = Alignment(
                wrap_text=True,
                vertical="top",
            )
            
            worksheet.cell(
                row=row,
                column=3,
            ).alignment = Alignment(
                vertical="top",
            )
            
            worksheet.row_dimensions[row].height = 120
            
            row += 1
            
    def _format_extracted_data(self, data: dict | None) -> str:
        """
        Convert OCR JSON into a readable multiline string.
        """
        
        if not data:
            return ""
        
        lines = []
        
        for key, value in data.items():
            pretty_key = key.replace("_", " ").title()
            lines.append(f"{pretty_key}: {value}")
            
        return "\n".join(lines)