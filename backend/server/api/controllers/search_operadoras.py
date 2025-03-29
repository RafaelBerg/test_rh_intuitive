from ..utils.query_executor import execute_query

async def search_operadoras(query: str):
    try:
        sql_query = """
            SELECT * FROM operadoras 
            WHERE nome_fantasia LIKE :query OR razao_social LIKE :query
        """
        return await execute_query(sql_query, {"query": f"%{query}%"})
    except Exception as e:
        print(f"Erro ao buscar operadoras: {str(e)}")
        return {"error": "Erro ao buscar operadoras"}