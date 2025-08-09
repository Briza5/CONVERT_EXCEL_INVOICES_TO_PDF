import pandas as pd # Import pandas for data manipulation and analysis
import glob # Import glob to find files matching a specified pattern

filepaths = glob.glob("invoices/*.xlsx") # glob to find all .xlsx files in the invoices directory and store them in a list

for filepath in filepaths: # Iterate over each file path in the list
    df = pd.read_excel(filepath, sheet_name="Sheet 1") # Read the Excel file into a DataFrame and specify the sheet name
    print(df)