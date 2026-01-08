from pathlib import Path
from pipeline.pipeline import DocumentParser
import json

BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)
PDF_PATH = BASE_DIR / "data" / "Logistics_Invoice_IN-horus-987103 (1).pdf"

print(PDF_PATH)
parser = DocumentParser(str(PDF_PATH))
result = parser.parse_output()

