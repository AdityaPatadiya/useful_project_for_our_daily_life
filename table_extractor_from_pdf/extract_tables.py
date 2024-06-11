import pdfplumber
import pandas as pd

# Open the PDF file
pdf_path = '[Add_your_pdf_file_path_here]'
all_data = []

with pdfplumber.open(pdf_path) as pdf:
    for page_number in range(len(pdf.pages)):
        page = pdf.pages[page_number]
        tables = page.extract_table()
        # print(tables)

        if tables:
            # Create DataFrame for the current page
            df = pd.DataFrame(tables[1:], columns=tables[0])
            all_data.append(df)

# Concatenate all DataFrames
if all_data:
    combined_df = pd.concat(all_data, ignore_index=True)
    combined_df.to_excel('combined_output.xlsx', index=False)

print("Data extraction and export complete.")
