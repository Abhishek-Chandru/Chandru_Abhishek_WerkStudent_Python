

## Task Details

1. **Data Extraction**:
    - Extract specific values from three sample invoices.
    - For Sample 1, extract the value shown in the provided image.
    - <img width="289" alt="image" src="https://github.com/user-attachments/assets/0cf000ff-c305-4ffe-beb4-1c02a04d06b6" />
    - For Samples 2, extract the value shown in the provided image.
    - <img width="497" alt="image" src="https://github.com/user-attachments/assets/ea6eb368-604d-4dd4-9235-fbc8ec36d275" />

2. **Excel File Creation**:
    - Create an Excel file with two sheets:
        - **Sheet 1**: Contains three columns - File Name, Date (scraped from the document), and Value.
        - **Sheet 2**: Contains a pivot table with the date and value sum, and also by document name.

3. **CSV File Creation**:
    - Create a CSV file with all the data, including headers, and use a semicolon (;) as the separator.

4. **Executable File**:
    - Provide an executable file (.exe) that can run the code if the files are in the same folder.

5. **Fork Creation**:
    - Create a fork of this repository named `LastName_FirstName_WerkStudent_Python` (e.g., `Shovon_Golam_WerkStudent_Python`).
    - Upload your code to this branch. No need to submit a pull request; the fork will be checked directly.

6. **Documentation**:
    - Include an explanation in the README file that a non-technical person can understand.
    - Ensure the code is documented so that a technical person can understand it.

7. **Problem Reporting**:
    - If you face any problems or find it impossible to complete a task, document the issue in the README file of your branch. Explain what the problem was and why you were unable to complete it.
   
## How It Works
This Script processes two invoices to extract dates and amounts, generating an Excel file with a summary and pivot table and a CSV file with the extracted data.

## Overview
Imports Required Libraries:
	-pdfplumber: Reads and extracts text from PDF files.
	-re: Performs pattern matching for extracting specific information.
	-pandas: Handles data organization and creation of Excel and CSV files.
	-os: Handles file paths and directory operations.

Functions to Extract Data
	-extract_date_from_pdf(pdf_path, date_pattern):
		Searches for specific date patterns in the PDF text using regular expressions.
		Supports flexible date formats like 1. März 2024 or Nov 26, 2016.
	-extract_gross_amount(pdf_path):
		Extract the "Gross Amount incl. VAT" from the PDF text.
		Converts the amount to a numerical format for calculations.
	-extract_total_value(pdf_path):
		Extract the "Total USD" value from the PDF text.
		Handles decimal formatting and ensures the value is converted to a number

Extracting Data from Sample Invoices
	-The script checks the directory for  (sample_invoice_1.pdf and sample_invoice_2.pdf) for processing.
	-It applies the functions above to extract:
		Invoice dates.
		Gross amount (for sample_invoice_1.pdf).
		Total USD value (for sample_invoice_2.pdf).

Organizing Data into a DataFrame
	-DataFrame: A table-like structure created using pandas to hold the extracted data.
		Columns:
			File Name: Name of the PDF file.
			Date: Extracted date from the invoice.
			Value: Extracted amount (either Gross Amount incl. VAT or Total USD).
Creating a Pivot Table
	-A pivot table is generated to summarize the data:
		Rows: Invoice dates.
		Columns: File names.
		Values: Summed amounts from the invoices.
		Includes a "Total" row and column for overall sums.
Saving Data to Files
	-Excel File (Output_excel.xlsx):
		Sheet 1: Contains the raw extracted data.
		Sheet 2: Contains the pivot table summarizing the data.
	-CSV File (Output_csv.csv):
		Contains the raw extracted data in a simple, plain-text format with semicolon separators.




