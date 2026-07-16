from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/lista")
async def autenticar():
    return {"mensagem":"Rota autenticação pedidos acessada!"}