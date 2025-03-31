import subprocess
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SCRIPTS = [
    os.path.join(BASE_DIR, "web_scraping", "main.py"),
    os.path.join(BASE_DIR, "data_transformation", "main.py"),
    os.path.join(BASE_DIR, "database", "config.py"),
]

def run_script(script):
    print(f"Executando {script}...")
    result = subprocess.run(["python", script], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"{script} executado com sucesso!\n")
    else:
        print(f"Erro ao executar {script}:\n{result.stderr}\n")
        return False
    return True

if __name__ == "__main__":
    for script in SCRIPTS:
        if not run_script(script): 
            print("Erro ao executar os scripts, não iniciando o servidor.")
            exit(1)
    print("Todos os scripts executados com sucesso. Iniciando o servidor...")
    subprocess.run(["python", "-m", "uvicorn", "backend.server.app:app", "--reload"])