import zipfile
import os
from config import ZIP_PATH

def compress_files(files):
    with zipfile.ZipFile(ZIP_PATH, "w") as zipf:
        for file in files:
            zipf.write(file, os.path.basename(file))
    
    print(f"Arquivos compactados em {ZIP_PATH}")
