from ..utils.query_executor import execute_query
import os

async def top_operators_quarter():
    try:
        file_path = os.path.abspath("backend/database/sql/top_operators_quarter.sql")

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

        with open(file_path, 'r', encoding='utf-8') as file:
            sql_query = file.read()        

        return await execute_query(sql_query)
    
    except FileNotFoundError as e:
        print(str(e))
        return {"error": str(e)}
    except Exception as e:
        print(f"Erro ao executar query para o último trimestre: {str(e)}")
        return {"error": "Erro ao executar query para o último trimestre"}
