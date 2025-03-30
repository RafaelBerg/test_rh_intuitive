from ..utils.query_executor import execute_query

async def search_operadoras(search: str):
    try:
        if not search.strip():
            return {"message": "O campo de busca não pode estar vazio."}

        sql_query = """
            SELECT * FROM operadoras 
            WHERE nome_fantasia LIKE :search OR razao_social LIKE :search
        """
        params = {"search": f"%{search}%"}
        
        operadoras = await execute_query(sql_query, params)

        if not operadoras:
            return {"message": "Nenhuma operadora encontrada."}

        return {"operadoras": operadoras}

    except Exception as e:
        print(f"Erro ao buscar operadoras: {str(e)}")
        return {"error": "Erro interno ao buscar operadoras. Tente novamente mais tarde."}