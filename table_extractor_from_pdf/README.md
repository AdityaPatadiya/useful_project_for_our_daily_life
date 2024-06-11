# PDF Table Extractor

This project extracts tables from a PDF file and combines them into a single Excel file. It uses `pdfplumber` for PDF parsing and `pandas` for data manipulation.

# Purpose of making this project
The main reason why I made this project is to only extract the tables from the pdf that make the excel more .
Whenever the table in the pdf has contain more number of lines for one row, then it consider two lines whenever we extract the data from the pdf in excel and it's becoming headache to mearge the rows when the pdf contain large amount data.

## Features

- Extracts tables from each page of a PDF file.
- Combines the extracted data of multiple pages into a single DataFrame.
- Exports the combined data to an Excel file.

## Requirements

- Python 3.x
- `pdfplumber` library
- `pandas` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/AdityaPatadiya/pdf-table-extractor.git
    cd pdf-table-extractor
    ```

2. Install the required packages:
    ```bash
    pip install pdfplumber pandas
    ```

## Usage

1. Place the PDF file you want to extract data from in the project directory.

2. Update the `pdf_path` variable in the script to the name of your PDF file:
    ```python
    pdf_path = 'your_pdf_file.pdf'
    ```

3. Run the script:
    ```bash
    python extract_tables.py
    ```

4. The extracted data will be saved in an Excel file named `combined_output.xlsx` in the project directory.

> [!NOTE]
> **PDFs must contains the header line for each table in every page.**

## Example

Here's an example of the main script (`extract_tables.py`):

```python
import pdfplumber
import pandas as pd

# Open the PDF file
pdf_path = 'your_pdf_file.pdf'
all_data = []

with pdfplumber.open(pdf_path) as pdf:
    for page_number in range(len(pdf.pages)):
        page = pdf.pages[page_number]
        tables = page.extract_table()

        if tables:
            # Create DataFrame for the current page
            df = pd.DataFrame(tables[1:], columns=tables[0])
            all_data.append(df)

# Concatenate all DataFrames
if all_data:
    combined_df = pd.concat(all_data, ignore_index=True)
    combined_df.to_excel('combined_output.xlsx', index=False)

print("Data extraction and export complete.")
