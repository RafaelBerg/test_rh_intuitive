from config import PDF_PATH, ZIP_PATH, CSV_PATH
from process_pdf import process_pdf
from transform import transform
from compress_csv import compress_csv

def main():
    data = process_pdf(PDF_PATH)
    
    if data:
        transform(data, CSV_PATH)
        compress_csv(CSV_PATH, ZIP_PATH)

if __name__ == "__main__":
    main()