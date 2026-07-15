from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@order_router.get("/lista")
async def pedidos():
    return {"mensagem":"Rota pedidos"}