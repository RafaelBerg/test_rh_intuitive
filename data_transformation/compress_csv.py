import os
import zipfile

def compress_csv(csv_path, zip_path):
    if not os.path.exists(csv_path):
        print("Erro: Arquivo CSV não encontrado para compactação.")
        return
    
    with zipfile.ZipFile(zip_path, "w") as zipf:
        zipf.write(csv_path, os.path.basename(csv_path))
    
    print(f"CSV compactado em: {zip_path}")
