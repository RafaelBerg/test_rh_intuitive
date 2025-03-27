import os
import requests
from config import DOWNLOAD_FOLDER

def download_pdf(pdf_links):
    downloaded_files = []

    for idx, link in enumerate(pdf_links, start=1):
        pdf_url = link if link.startswith("http") else f"https://www.gov.br{link}"
        pdf_name = f"anexo_{idx}.pdf"
        pdf_path = os.path.join(DOWNLOAD_FOLDER, pdf_name)

        print(f"Baixando {pdf_name}...")

        pdf_response = requests.get(pdf_url)
        if pdf_response.status_code == 200:
            with open(pdf_path, "wb") as pdf_file:
                pdf_file.write(pdf_response.content)
                downloaded_files.append(pdf_path)
        else:
            print(f"Falha ao baixar {pdf_name}.")

    return downloaded_files