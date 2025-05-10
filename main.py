from fastapi import FastAPI
from routes.empresa import router as empresa_router
from routes.role import router as role_router
from routes.funcionario import router as funcionario_router
from routes.motorista_empresa import router as motorista_router
from routes.veiculo_empresa import router as veiculo_router
from routes.operacao import router as operacao_router
from routes.carga_descarga import router as carga_descarga_router
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(empresa_router, prefix="/empresas", tags=["empresas"])
app.include_router(role_router, prefix="/permissoes", tags=["permissoes"])
app.include_router(funcionario_router, prefix="/funcionarios", tags=["funcionarios"])
app.include_router(motorista_router, prefix="/motoristas", tags=["motoristas"])
app.include_router(veiculo_router, prefix="/veiculos", tags=["veiculos"])
app.include_router(operacao_router, prefix="/operacoes", tags=["operacoes"])
app.include_router(carga_descarga_router, prefix="/cargasdescargas", tags=["cargasdescargas"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)