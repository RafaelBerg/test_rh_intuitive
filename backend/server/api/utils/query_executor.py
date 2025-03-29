from sqlalchemy import create_engine, text
from ...config import settings

async def execute_query(sql_query: str, params: dict = None):
    engine = create_engine(settings.db_url)
    with engine.connect() as connection:
        result = connection.execute(text(sql_query), params)
        columns = result.keys() 
        data = result.fetchall()
        return [dict(zip(columns, row)) for row in data]