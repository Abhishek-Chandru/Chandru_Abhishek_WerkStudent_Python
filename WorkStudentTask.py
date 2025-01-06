#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pdfplumber
import re
import pandas as pd
import os

# Get the current directory where the script/executable is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Function to extract dates from PDF
def extract_date_from_pdf(pdf_path, date_pattern):
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                match = re.search(date_pattern, text)
                if match:
                    return match.group(1)  # Return the matched date
    return None


# Function to extract Gross Amount incl. VAT
def extract_gross_amount(pdf_path):
    pattern = r"Gross Amount incl\. VAT\s+([\d,.]+) €"  # Regex to capture the amount
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                match = re.search(pattern, text)
                if match:
                    # Replace comma with dot to correctly handle the decimal point
                    value = match.group(1).replace(",", ".")
                    return float(value)  # Convert to float
    return None


# Function to extract Total USD value
def extract_total_value(pdf_path):
    pattern = r"Total\s*USD\s*\$([\d,.]+)"  # Regex to match the Total value
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                match = re.search(pattern, text)
                if match:
                    # Replace comma with dot to correctly handle decimal point
                    value = match.group(1).replace(",", ".")
                    return float(value)  # Convert to float
    return None


# Paths to PDF files (files should be in the same directory as the script)
pdf_1_path = os.path.join(current_dir, "sample_invoice_1.pdf")
pdf_2_path = os.path.join(current_dir, "sample_invoice_2.pdf")

# Define patterns for extracting dates
date_pattern_1 = r"(\d+\.\s*\w+\s*\d{4})"  # Matches '1. März 2024'
date_pattern_2 = r"Invoice date:\s*(\w+\s+\d{1,2},\s+\d{4})"  # Matches 'Nov 26, 2016'

# Extract dates and values from PDFs
date_1 = extract_date_from_pdf(pdf_1_path, date_pattern_1)
date_2 = extract_date_from_pdf(pdf_2_path, date_pattern_2)
gross_amount = extract_gross_amount(pdf_1_path)
total_value = extract_total_value(pdf_2_path)

# Prepare data for Excel and CSV
data = [
    {"File Name": "sample_invoice_1.pdf", "Date": date_1, "Value": gross_amount},
    {"File Name": "sample_invoice_2.pdf", "Date": date_2, "Value": total_value},
]

# Create a DataFrame
df = pd.DataFrame(data)

# Create a pivot table for the Excel file
pivot_table = pd.pivot_table(
    df,
    values="Value",
    index="Date",
    columns="File Name",
    aggfunc="sum",
    fill_value=0,
    margins=True,  # Adds a "Total" row and column
    margins_name="Total"  # Customize name of margins
)

# Save to Excel file with two sheets in the same directory
output_excel_file = os.path.join(current_dir, "Output_excel.xlsx")
with pd.ExcelWriter(output_excel_file, engine="openpyxl") as writer:
    # Write Sheet 1
    df.to_excel(writer, index=False, sheet_name="Sheet1")
    # Write Pivot Table to Sheet 2
    pivot_table.to_excel(writer, sheet_name="Sheet2")

print(f"Excel file '{output_excel_file}' created successfully.")

# Save the data to a CSV file with semicolon (;) as the separator in the same directory
output_csv_file = os.path.join(current_dir, "Output_csv.csv")
df.to_csv(output_csv_file, sep=";", index=False)

print(f"CSV file '{output_csv_file}' created successfully.")


# In[ ]:




