from glob import glob # Import glob to find files matching a specified pattern
from pathlib import Path # Import Path for handling file paths
import fpdf # Import FPDF for creating PDF files


filepaths = glob("animals_project/*.txt") # glob to find all .txt files in the animals directory and store them in a list
pdf = fpdf.FPDF(orientation="P", unit="mm", format="A4") # Create a new PDF object
for filepath in filepaths: # Iterate over each file path in the list
    filename = Path(filepath).stem # Extract the file name without the extension
    pdf.add_page() # Add a new page to the PDF
    pdf.set_font("Times", size=16, style="B") # Set the font for the PDF
    pdf.cell(w=58, h=8, txt=f"{filename.title()}",) # Add a cell with the animal name

pdf.output("pdf_animals/output.pdf") # Save the PDF to the specified directory with the same name as the text file
        