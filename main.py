import pandas as pd # Import pandas for data manipulation and analysis
import glob # Import glob to find files matching a specified pattern
from fpdf import FPDF # Import FPDF for creating PDF files
from pathlib import Path # Import Path for handling file paths

""" Find all Excel files in the 'invoices' directory and convert them to PDF invoices
 and store them in to the list filepaths."""
filepaths = glob.glob("invoices/*.xlsx") 
for filepath in filepaths: # Iterate over each file path in the list
    
    pdf = FPDF(orientation="P", unit="mm", format="A4") # Create a new PDF object
    pdf.add_page() # Add a new page to the PDF
    
    filename = Path(filepath).stem # Extract the file name without the extension

    """ Split the filename into invoice number and date based on the hyphen"""
    invoice_nr, date = filename.split("-") 

    pdf.set_font("Times", size=16, style="B") # Set the font for the PDF

    """ Add a cell with the invoice number and date,"""
    pdf.cell(w=58,h=8, txt=f"Invoice nr. {invoice_nr}", ln=1) 
   
    pdf.set_font("Times", size=16, style="B") # Set the font for the PDF
    pdf.cell(w=58,h=8, txt=f"Date: {date}", ln=1) # Add a cell with the date and move to the next line

    """ Read the Excel file into a pandas DataFrame,
    specifying the sheet name to read from."""
    df = pd.read_excel(filepath, sheet_name="Sheet 1") 
    

    """ Add a header row to the PDF with the column names, 
    setting the font and text color."""
    columns = df.columns # get the column names from the DataFrame
    columns = [col.replace("_", " ").title() for col in columns] # Format the column names
    pdf.set_font("Times", size=10, style="B") # Set the font for the header row
    pdf.set_text_color(80, 80, 80) # Set the text color for the header row
    pdf.cell(w=30, h=8, txt=columns[0], border=1) 
    pdf.cell(w=70, h=8, txt=columns[1], border=1) 
    pdf.cell(w=30, h=8, txt=columns[2], border=1) 
    pdf.cell(w=30, h=8, txt=columns[3], border=1) 
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1) 

    """ Iterate over each row in the DataFrame and add the data to the PDF, 
    without the header."""
    for index, row in df.iterrows(): # Iterate over each row in the DataFrame
        pdf.set_font("Times", size=10) # Set the font for the PDF
        pdf.set_text_color(80, 80, 80) # Set the text color for the PDF
        """        Add a cell for each column in the DataFrame with specified
          width, height, and border."""
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1) 
        pdf.cell(w=70, h=8, txt=str(row["product_name"]), border=1) 
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]), border=1) 
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1) 
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1) 
   
    pdf.output(f"pdfs/{filename}.pdf") # Save the PDF to the specified directory with the same name as the Excel file