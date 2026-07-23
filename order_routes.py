from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import pegar_sessao
from schemas import PedidoSchemas
from models import Pedidos

order_router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@order_router.get("/lista")
async def funcao():
    return {"mensagem":"rota pedidos acessada"}

@order_router.post("/pedidos")
async def criar_pedido(pedido_schemas: PedidoSchemas, session: Session = Depends(pegar_sessao)):
    novo_pedido = Pedidos(usuario=pedido_schemas.id_usuario)
    session.add(novo_pedido)
    session.commit()
    return {"mensagem":"Pedido feito com sucesso!!"}
