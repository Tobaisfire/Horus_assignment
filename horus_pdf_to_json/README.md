# Horus PDF to JSON Converter

A Python-based document processing pipeline that extracts structured data from PDF invoices and converts them to JSON format. The project follows a Bronze-Silver-Gold data architecture pattern for robust data extraction and validation.

## Overview

This project processes PDF invoices and extracts key information.

## Project Structure

```
horus_pdf_to_json/
├── bronze/              # Raw data extraction layer
│   └── pdf_reader.py    # PDF parsing using pdfplumber
├── silver/              # Data transformation layer
│   ├── text_parser.py   # Extracts structured fields from text
│   └── table_parser.py  # Extracts structured data from tables
├── gold/                # Data validation and output layer
│   └── models.py        # Pydantic models for validation
├── pipeline/            # Pipeline orchestration
│   └── pipeline.py      # Main DocumentParser class
├── data/                # Sample PDF and output files
├── run_pipeline.py      # Main entry point
└── requirements.txt     # Python dependencies
```

## Architecture

The project uses a three-layer data pipeline:

1. **Bronze Layer** (`bronze/`): Extracts raw text and tables from PDF files
2. **Silver Layer** (`silver/`): Transforms raw data into structured fields
3. **Gold Layer** (`gold/`): Validates and converts data to final JSON format

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd horus_pdf_to_json
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Run the pipeline on a PDF file:

```bash
python run_pipeline.py
```

The script processes the PDF located at `data/Logistics_Invoice_IN-horus-987103 (1).pdf` and generates a JSON output file.



## Key Components

### Bronze Layer (`bronze/pdf_reader.py`)
- Uses `pdfplumber` to extract raw text and tables from PDF files
- Returns unstructured data for further processing

### Silver Layer
- **`text_parser.py`**: Extracts key-value pairs from text (supplier, dates, amounts, etc.)
- **`table_parser.py`**: Converts PDF tables into structured line items

### Gold Layer (`gold/models.py`)
- **`TextToJson`**: Pydantic model that validates and structures the final output
- **`TableData`**: Model for table data with headers and rows
- **`TextData`**: Model for raw text content

### Pipeline (`pipeline/pipeline.py`)
- Orchestrates the entire extraction process
- Includes logging with audit IDs for tracking
- Handles errors and saves output to JSON files

## Dependencies

Main dependencies:
- `pdfplumber`: PDF text and table extraction
- `pydantic`: Data validation and serialization
- `pandas`: Data manipulation (if needed)

See `requirements.txt` for the complete list.

## Features

- ✅ Extracts text and tables from PDF invoices
- ✅ Structured field extraction (supplier, dates, amounts)
- ✅ Table parsing for line items
- ✅ Data validation using Pydantic models
- ✅ Audit logging with unique IDs
- ✅ JSON output generation



