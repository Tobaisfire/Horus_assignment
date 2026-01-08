
from gold.models import TextToJson
from pydantic import BaseModel
from typing import Dict

class TextParser(BaseModel):

    raw_text: str


    def extract_text_fields(self) -> Dict:
        field_map = {
            "Horus Reference": "horus_reference",
            "Supplier": "supplier",
            "VAT ID": "vat_id",
            "Issue Date": "issue_date",
            "Payment Terms": "payment_terms",
            "Subtotal": "subtotal",
            "TOTAL AMOUNT DUE (USD)": "total"
        }
        data = {}
        for line in self.raw_text.splitlines():
            line = line.strip()
            if ":" not in line:
                continue
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if key in field_map:
                field_name = field_map[key]
                data[field_name] = value

        data["subtotal"] = float(data["subtotal"].replace("$", "").replace(",", ""))
        data["total"] = float(data["total"].replace("$", "").replace(",", ""))
        extracted_data = data
        return extracted_data