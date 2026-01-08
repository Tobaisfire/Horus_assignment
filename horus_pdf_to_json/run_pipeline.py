from pathlib import Path
from pipeline.pipeline import DocumentParser
import json

BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)
PDF_PATH = BASE_DIR / "data" / "Logistics_Invoice_IN-horus-987103 (1).pdf"
OUT_JSON_PATH = BASE_DIR / "output" / "output.json"

print(PDF_PATH)

if __name__ == "__main__":
    parser = DocumentParser(str(PDF_PATH),str(OUT_JSON_PATH))
    result = parser.process_document()

