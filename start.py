import subprocess
import webbrowser

def run_command(command, cwd=None):
    process = subprocess.Popen(command, shell=True, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    for line in process.stdout:
        print(line, end="")

    for line in process.stderr:
        print(line, end="")

    process.wait()
    if process.returncode != 0:
        print(f"Erro ao executar: {' '.join(command)}")
        exit(1)

# 1️⃣ Instalar dependências do backend
print("\n🔹 Instalando dependências do backend...")
run_command(["pip", "install", "-r", "backend/requirements.txt"])

# 2️⃣ Instalar dependências do frontend
print("\n🔹 Instalando dependências do frontend...")
run_command(["npm", "install"], cwd="frontend")

# 3️⃣ Rodar o backend
print("\n🚀 Iniciando o backend...")
backend_process = subprocess.Popen(["python", "backend/start_backend.py"])

# 4️⃣ Rodar o frontend (apenas após o backend terminar)
print("\n🚀 Iniciando o frontend...")
run_command(["npm", "run", "dev"], cwd="frontend")

# 5️⃣ Abrir a página do Postman após finalizar tudo
print("\n🌐 Abrindo a documentação do Postman...")
webbrowser.open("https://documenter.getpostman.com/view/33303998/2sB2cPjkPS")