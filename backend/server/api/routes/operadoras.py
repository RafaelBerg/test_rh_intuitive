from fastapi import APIRouter
from ..controllers.search_operadoras import search_operadoras
from ..controllers.top_operators_quarter import top_operators_quarter
from ..controllers.top_operators_year import top_operators_year

router = APIRouter()

@router.get("/operadoras")
async def search_operators(search: str):
    return await search_operadoras(search)

@router.get("/operadoras/top-trimestre")
async def get_top_operators_quarter():
    return await top_operators_quarter()

@router.get("/operadoras/top-ano")
async def get_top_operators_year():
    return await top_operators_year()