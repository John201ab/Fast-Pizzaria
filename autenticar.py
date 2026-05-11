from fastapi import APIRouter

autenticador = APIRouter(prefix="/autenticacao", tags=["Autenticadores"])

@autenticador.get("/")
async def autenticacao():  
    """Teste monstro de decrição"""
    return {"Mensagem": "autenticado com sucesso"}
