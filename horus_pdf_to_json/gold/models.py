from datetime import datetime
from typing import List, Dict
from pydantic import BaseModel

class TableData(BaseModel):
    headers: List[str]
    rows: List[List[str]]

    def to_dict(self) -> Dict:
        table_data = [
            dict(zip(self.headers, row)) for row in self.rows
        ]
        return {"line_items": table_data}

    def __str__(self) -> str:
        return f"Headers: {self.headers}\nRows: {self.rows}"

    
        
class TextData(BaseModel):
    content: str

    def __str__(self) -> str:
        return self.content
    

class TextToJson(BaseModel):
    horus_reference: str
    supplier: str
    vat_id: str
    issue_date: datetime
    payment_terms: str
    subtotal: float
    total: float
    line_items: List[Dict]

    def to_json(self) -> str:
        return self.model_dump_json(indent=4)