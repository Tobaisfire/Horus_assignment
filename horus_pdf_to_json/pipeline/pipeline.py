# horus_pdf_to_json/pipeline/pipeline.py
from bronze.pdf_reader import PDFParser
from silver.text_parser import TextParser
from silver.table_parser import TableParser
from gold.models import TextData, TextToJson
import logging
from typing import Dict
import uuid
from time import sleep



class DocumentParser:
    """
    Docstring for DocumentParser.
    Bronze-Silver-Gold pipeline to parse PDF documents and extract structured data.
    """
    def __init__(self, path: str):
        self.path = path

    def _log(self, audit_id, message: str, level: str = "info") -> None:


        logging.basicConfig(level=logging.INFO)
        log_message = f"[Audit ID: {audit_id}] {message}"

        if level == "info":
            logging.info(log_message)
        elif level == "warning":
            logging.warning(log_message)
        elif level == "error":
            logging.error(log_message)
        else:
            logging.debug(log_message)

    
    def process_document(self) -> Dict:
        """
        Main method to process the document through the Bronze, Silver, and Gold stages.
        Returns:        
            Dict: Dictionary containing extracted text data, tables, and final JSON results.
        """

        audit_id = str(uuid.uuid4())   

        self._log(audit_id, message=f"Starting document processing for {self.path}", level="info")

        try:
            # Initialize PDFParser
            self._log(audit_id, message=f"Initializing PDFParser for {self.path}", level="info")
            parser = PDFParser(path=self.path)
            pdf_parsed = parser.parse()
            self._log(audit_id, message=f"PDF parsing completed for {self.path}", level="info")

            # Raw text extraction (Bronze)
            raw_text = pdf_parsed["text"]

            try:
                # Extract text fields and tables fields (Silver)
                sleep(1)  # Simulate processing time
                self._log(audit_id, message="Extracting text fields and tables fields", level="info")
                text_data = TextData(content=raw_text)
                text_fields = TextParser(raw_text=raw_text).extract_text_fields() # Extract text fields (Silver)

                tables = pdf_parsed["tables"]
                tables = TableParser(raw_tables=tables).extract_tables_fields() # Extract table fields (Silver)
                
                # Combine mutliple tables if more than one table is found
                if len(tables) > 0:
                    for table in tables:
                        table_fields = table.to_dict()
                        text_fields.update(table_fields) # Merge table fields into text fields

                self._log(audit_id, message="Text fields and tables fields extraction completed", level="info")

                # Validate and convert to final JSON (Gold)
                sleep(1)  # Simulate processing time
                self._log(audit_id, message="Validating and converting to final JSON", level="info")
                text_fields_parsed = TextToJson(**text_fields)
                self._log(audit_id, message="Final JSON conversion completed", level="info")

                print(text_fields_parsed.to_json()) # For debugging purposes (Final JSON output)

            except Exception as e:  
                self._log(audit_id, message=f"Error extracting text fields and tables fields: {e}", level="error")
                raise e
            
        except Exception as e:
            self._log(audit_id, message=f"Error initializing PDFParser: {e}", level="error")
            raise e
        
        sleep(1)  # Simulate processing time
        self._log(audit_id, message=f"Document processing completed for {self.path}", level="info")

        # Save Extracted Data to JSON File

        with open(f"extracted_data_{audit_id}.json", "w", encoding="utf-8") as json_file:
            json_file.write(text_fields_parsed.to_json())

        return {
            "text": text_data,
            "tables": tables,
            "Results": text_fields_parsed.to_json()
        }
