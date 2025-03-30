from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, text
from .config import settings
from .api.routes.operadoras import router as api_router

app = FastAPI()

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.on_event("startup")
async def startup():
    try:
        engine = create_engine(settings.db_url)

        with engine.connect() as connection:
            print("Conexão com o banco de dados bem-sucedida!")

            result = connection.execute(text("SELECT 1"))
            test_value = result.scalar()

            if test_value == 1:
                print("Conexão confirmada com o banco de dados!")

    except Exception as e:
        print(f"Erro na conexão com o banco de dados: {str(e)}")
        
@app.on_event("shutdown")
async def shutdown():
    print("O servidor está sendo encerrado.")