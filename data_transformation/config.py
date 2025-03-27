import os

# Caminho do pdf
PDF_PATH = "downloads/scraping/anexo_1.pdf"

DOWNLOAD_FOLDER = "downloads/data_processing"

ZIP_PATH = os.path.join(DOWNLOAD_FOLDER, "Teste_Rafael_Berg_Medeiros.zip")

CSV_PATH = os.path.join(DOWNLOAD_FOLDER, "Rol_de_Procedimentos.csv")

# Cria as pastas necessárias caso não existam
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)