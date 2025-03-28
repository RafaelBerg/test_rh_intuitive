import os

# URLs e pastas de download
URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
BASE_URL_ANS = "https://dadosabertos.ans.gov.br/FTP/PDA"

DOWNLOAD_FOLDER = "downloads"

SCRAPING_FOLDER = os.path.join(DOWNLOAD_FOLDER, "scraping")

DATABASE_FOLDER = os.path.join(DOWNLOAD_FOLDER, "database")

ZIP_PATH = os.path.join(SCRAPING_FOLDER, "anexos.zip")

# Cria as pastas caso não existam
os.makedirs(SCRAPING_FOLDER, exist_ok=True)
os.makedirs(DATABASE_FOLDER, exist_ok=True)

os.makedirs(os.path.join(DATABASE_FOLDER, "demonstracoes_contabeis"), exist_ok=True)
os.makedirs(os.path.join(DATABASE_FOLDER, "operadoras_de_plano_de_saude_ativas"), exist_ok=True)