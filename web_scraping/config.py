import os

# URL da página de onde os PDFs serão baixados
URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

DOWNLOAD_FOLDER = "downloads/scraping"

ZIP_PATH = os.path.join(DOWNLOAD_FOLDER, "anexos.zip")

# Cria as pastas caso não existam
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)