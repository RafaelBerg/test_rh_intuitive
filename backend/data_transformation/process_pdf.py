import pdfplumber

def process_pdf(pdf_path):
    data = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_table()
            if tables:
                data.extend(tables)
    
    return data
