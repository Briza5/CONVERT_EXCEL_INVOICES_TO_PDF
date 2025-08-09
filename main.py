import pandas as pd # Import pandas for data manipulation and analysis
import glob # Import glob to find files matching a specified pattern
from fpdf import FPDF # Import FPDF for creating PDF files
from pathlib import Path # Import Path for handling file paths

filepaths = glob.glob("invoices/*.xlsx") # glob to find all .xlsx files in the invoices directory and store them in a list

for filepath in filepaths: # Iterate over each file path in the list
    df = pd.read_excel(filepath, sheet_name="Sheet 1") # Read the Excel file into a DataFrame and specify the sheet name
    pdf = FPDF(orientation="P", unit="mm", format="A4") # Create a new PDF object
    pdf.add_page() # Add a new page to the PDF
    filename = Path(filepath).stem # Extract the file name without the extension
    invoice_nr = filename.split("-")[0] # Split the file name to get the invoice number from the first part of the name
    pdf.set_font("Times", size=16, style="B") # Set the font for the PDF
    pdf.cell(w=58,h=8, txt=f"Invoice nr. {invoice_nr}") # Add a cell with the invoice number
    pdf.output(f"pdfs/{filename}.pdf") # Save the PDF to the specified directory with the same name as the Excel file