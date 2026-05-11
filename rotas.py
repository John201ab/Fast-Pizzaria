from fastapi import APIRouter

rotas = APIRouter(prefix="/routes", tags=["Rotas"])

@rotas.get("/")
async def pedidos():
    return {"mensagem": "Você acessou a rota 'rotas'"}
    #dominio/auth/ 