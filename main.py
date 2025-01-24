import pandas as pd
import glob #To read the files of specific format...
from  fpdf import FPDF
import pathlib
filepaths = glob.glob('invoices/*.xlsx')
# print(filepaths)

for filepath in filepaths:
    df = pd.read_excel(filepath,sheet_name="Sheet 1")
    # print(df)
    pdf = FPDF(orientation="p", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font(family="Times",style="B",size=12)
    filename = pathlib.Path(filepath).stem
    Invoice_no = filename.split('-')[0]
    pdf.cell(w=50, h=8, txt=f"Invoice no: {Invoice_no} ")
    pdf.output(f"PDFs/{filename}.pdf")

    # for index,row in df.iterrows():
    #     row[""]




