
from bronze.pdf_reader import PDFParser
from silver.text_parser import TextParser
from silver.table_parser import TableParser
from gold.models import TextData, TextToJson

class DocumentParser:
    def __init__(self, path: str):
        self.path = path

    
    def parse_output(self) -> dict:
        parser = PDFParser(path=self.path)

        pdf_parsed = parser.parse()

        text = pdf_parsed["text"]
        text_data = TextData(content=text)
        text_fields = TextParser(raw_text=text).extract_text_fields()

        tables = pdf_parsed["tables"]
        tables = TableParser(raw_tables=tables).extract_tables_fields()
        
        if len(tables) > 0:
            for table in tables:
                table_fields = table.to_dict()
                text_fields.update(table_fields)

        text_fields_parsed = TextToJson(**text_fields)
        print(text_fields_parsed.to_json())

        return {
            "text": text_data,
            "tables": tables,
            "Results": text_fields_parsed.to_json()
        }
