from fastapi import APIRouter

order_router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@order_router.get("/lista")
async def funcao():
    return {"mensagem":"rota pedidos acessada"}