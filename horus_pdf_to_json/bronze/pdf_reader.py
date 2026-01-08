import pdfplumber
from typing import List, Dict
from pydantic import BaseModel


class PDFParser(BaseModel):
    """ Bronze: class to parse PDF files and extract text and tables ."""

    path: str


    def _extract_table(self,table_obj: List) -> List[List[str]]:
        """ 
        Extract table data from a pdfplumber Table object. 
        Args:
            table_obj (List): pdfplumber Table object.
            
        Returns:
            List[List[str]]: Extracted table data as a list of rows."""

        if not table_obj:
            return []
        table_data = table_obj.extract()
        return table_data

    def _extract_text_from_pdf(self,path: str) -> str:
        """
        Extract text from a PDF file.
        Args:
            path (str): Path to the PDF file.
        Returns:
            str: Extracted text from the PDF.   
        """

        with pdfplumber.open(path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text

    def _extract_tables_from_pdf(self,path: str) -> List[List[List[str]]]:
        """
        Extract tables from a PDF file.
        Args:
            path (str): Path to the PDF file.   
        Returns:
            List[List[List[str]]]: Extracted tables from the PDF.
        """

        tables = []
        with pdfplumber.open(path) as pdf:
           for page in pdf.pages:
               page_tables = page.find_tables()
               if page_tables:
                   for idx,table in enumerate(page_tables):
                       table_data = self._extract_table(table)
                       if table_data:
                           tables.append(table_data)

        return tables

    def parse(self) -> Dict:
        """
        Main method to parse the PDF and extract text and tables.
        Returns:        
            Dict: Dictionary containing extracted text and tables.
        """

        text = self._extract_text_from_pdf(self.path)
        tables = self._extract_tables_from_pdf(self.path)

        return {
            "text": text,
            "tables": tables
        }