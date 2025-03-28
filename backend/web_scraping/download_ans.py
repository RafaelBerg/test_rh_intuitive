import os
import requests
from bs4 import BeautifulSoup
from config import DATABASE_FOLDER
from extract import extract_and_remove_zip

def get_latest_years(base_url, categoria):
    response = requests.get(f"{base_url}/{categoria}/")
    if response.status_code != 200:
        print(f"Erro ao acessar {base_url}/{categoria}/")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    pastas = [a.text.strip('/') for a in soup.find_all('a') if a.text.strip('/').isdigit()]
    pastas.sort(reverse=True)
    
    return pastas[:2] if pastas else [""]

def download_ans():
    base_url = "https://dadosabertos.ans.gov.br/FTP/PDA"
    
    arquivos = {
        "demonstracoes_contabeis": {"arquivos": ["1T", "2T", "3T", "4T"], "is_zip": True},
        "operadoras_de_plano_de_saude_ativas": {"arquivos": ["Relatorio_cadop.csv"], "is_zip": False}
    }

    for categoria, dados in arquivos.items():
        anos = get_latest_years(base_url, categoria)
        
        for ano in anos:
            for arquivo in dados["arquivos"]:
                if dados["is_zip"]:
                    url = f"{base_url}/{categoria}/{ano}/{arquivo}{ano}.zip"
                    file_name = f"{arquivo}_{ano}.zip"
                else:
                    url = f"{base_url}/{categoria}/{arquivo}"
                    file_name = arquivo  
                
                ano_dir = os.path.join(DATABASE_FOLDER, categoria, ano if ano else "")
                os.makedirs(ano_dir, exist_ok=True)
                file_path = os.path.join(ano_dir, file_name)

                print(f"Baixando {file_path}...")

                try:
                    response = requests.get(url)
                    response.raise_for_status()

                    with open(file_path, "wb") as f:
                        f.write(response.content)
                    
                    print(f"Download concluído: {file_path}")

                    if dados["is_zip"]:
                        extract_and_remove_zip(file_path, ano_dir)

                except requests.exceptions.RequestException as e:
                    print(f"Erro ao baixar {url}: {e}")