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


    filename = pathlib.Path(filepath).stem
    Invoice_no = filename.split('-')
    Actual_invoice_no = Invoice_no[0]
    date = Invoice_no[1]

    pdf.set_font(family="Times", style="B", size=12)
    pdf.cell(w=50, h=8, txt=f"Invoice no: {Actual_invoice_no}",ln=1)
    pdf.cell(w=50, h=8, txt=f"Date: {date} ")

    # filename = pathlib.Path(filepath).name
    # date = filename.split('-')[1]



    pdf.output(f"PDFs/{filename}.pdf")

    # for index,row in df.iterrows():
    #     row[""]




