import mysql.connector
from mysql.connector import Error
import os
import re
from dotenv import load_dotenv

def log(message):
    print(f"[INFO] {message}")

def execute_sql_file(cursor, file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        content = re.sub(r'--.*?$', '', content, flags=re.MULTILINE)
        content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
        
        commands = []
        current = ""
        in_string = False
        string_char = None
        
        for char in content:
            if char in ("'", '"') and not in_string:
                in_string = True
                string_char = char
            elif char == string_char and in_string:
                in_string = False
                string_char = None
            
            current += char
            
            if char == ';' and not in_string:
                cmd = current.strip()
                if cmd:
                    commands.append(cmd)
                current = ""
        
        if current.strip():
            commands.append(current.strip())
        
        grouped_commands = []
        current_group = []

        for cmd in commands:
            current_group.append(cmd)
            if '; ' in cmd:
                grouped_commands.append(current_group)
                current_group = []
        
        if current_group:
            grouped_commands.append(current_group)

        for group in grouped_commands:
            for cmd in group:
                try:
                    log(f"Executando: {cmd[:100]}...")
                    cursor.execute(cmd)
                    
                    if cmd.strip().upper().startswith("SELECT"):
                        result = cursor.fetchall()
                        if result:
                            log(f"Resultado da consulta: {result}")
                        else:
                            log("Sem resultados para a consulta.")
                except Error as e:
                    log(f"ERRO no comando: {e}")
                    log(f"Comando completo: {cmd[:200]}...")
                    return False
        return True
    except Exception as e:
        log(f"ERRO ao processar arquivo: {e}") 
        return False
    
def main():
    try:
        load_dotenv()

        db_host = os.getenv("DB_HOST")
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_name = os.getenv("DB_NAME")

        conn = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name,
            allow_local_infile=True
        )
        cursor = conn.cursor()
        
        cursor.execute("CREATE DATABASE IF NOT EXISTS test_rh_intuitive")
        cursor.execute("USE test_rh_intuitive")
        log("Banco de dados configurado")
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        scripts = [
            'sql/init_db.sql',
            'sql/import_data.sql',
            'sql/top_operators_quarter.sql',
            'sql/top_operators_year.sql'
        ]
        
        for script in scripts:
            script_path = os.path.join(script_dir, script)
            log(f"Processando: {script_path}")
            
            if not os.path.exists(script_path):
                log(f"Arquivo não encontrado: {script_path}")
                continue
                
            if not execute_sql_file(cursor, script_path):
                raise Exception(f"Falha no script: {script}")
        
        conn.commit()
        log("Processo concluído com sucesso!")
        
    except Exception as e:
        log(f"ERRO FATAL: {e}")
        if 'conn' in locals():
            conn.rollback()
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    main()