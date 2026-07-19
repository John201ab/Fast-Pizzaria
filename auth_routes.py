from fastapi import APIRouter, Depends, HTTPException
from models import Usuario
from dependencies import pegar_sessao
from main import bcrypt_context
from schemas import UsuarioSchemas
from sqlalchemy.orm import Session

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/lista")
async def home():
    return {"mensagem":"Rota autenticação pedidos acessada!"}

@auth_router.post("/criar_conta")
async def criar_conta(usuarioschemas: UsuarioSchemas, session: Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==usuarioschemas.email).first()
    if usuario:
        raise HTTPException(status_code=400, detail="e-mail já cadastrado")
    else:
        print(senha)
        senha_criptografada = bcrypt_context.hash(usuarioschemas.senha)
        novo_usuario = Usuario(usuarioschemas.nome, usuarioschemas.email, senha_criptografada)
    
        session.add(novo_usuario)
        session.commit()
        session.close()
        return{"mensagem":f"e-mail {usuarioschemas.email} cadastrado com sucesso!!"}
        