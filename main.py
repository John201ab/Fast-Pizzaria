from fastapi import FastAPI
 
app = FastAPI()

from rotas import rotas
from autenticar import autenticador

app.include_router(rotas)
app.include_router(autenticador)

#para rodar o código: unicorn main:app --reload

#endpoint
#dominio.com/pedidos/lista

#get ->ler informações
#set -> criar informaçoes
#put/patch -> editar informações
#delete -> deletar informações
# sqlite viwer