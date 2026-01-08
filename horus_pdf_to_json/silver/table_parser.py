
from typing import List
from pydantic import BaseModel
from gold.models import TableData


class TableParser(BaseModel):
    raw_tables: List[List[List[str]]]

    def extract_tables_fields(self) -> List[TableData]:
        tables_data = []

        for table in self.raw_tables:
            if not table:
                continue

            headers = table[0]
            rows = table[1:]

            table_data = TableData(headers=headers, rows=rows)
            tables_data.append(table_data)

        return tables_data