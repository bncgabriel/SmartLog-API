from fastapi import FastAPI

#comando para entrar no venv "smartlog-venv\Scripts\activate.bat"

app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name': 'Benicio'}}

@app.get('/about')
def about():
    return {'data': {'name': 'about page'}}














