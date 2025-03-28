import os
import zipfile

def extract_and_remove_zip(zip_path, extract_to):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print(f"Extração concluída: {zip_path}")

        # Remover o arquivo ZIP após a extração
        os.remove(zip_path)
        print(f"Arquivo ZIP removido: {zip_path}")
    except zipfile.BadZipFile:
        print(f"Erro: Arquivo ZIP corrompido ou inválido - {zip_path}")
