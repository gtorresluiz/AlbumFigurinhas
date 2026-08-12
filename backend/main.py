from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import glob

app = FastAPI()

# Configura o middleware CORS para aceitar requisições de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define caminhos absolutos para a pasta de imagens
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Lista chamada figurinhas com 30 figurinhas.
# Apenas as figurinhas cujas imagens existem na pasta figurinhas/ estão ativas.
# (As imagens 1 a 29 existem no diretório, então estão ativas)
figurinhas = [
    {"id": 1, "nome": "Alan Turing", "categoria": "IA", "imagem_url": "/figurinhas/1/imagem"},
    {"id": 2, "nome": "John McCarthy", "categoria": "IA", "imagem_url": "/figurinhas/2/imagem"},
    {"id": 3, "nome": "Sam", "categoria": "IA", "imagem_url": "/figurinhas/3/imagem"},
    {"id": 4, "nome": "Geoffrey", "categoria": "IA", "imagem_url": "/figurinhas/4/imagem"},
    {"id": 5, "nome": "Yann", "categoria": "IA", "imagem_url": "/figurinhas/5/imagem"},
    {"id": 6, "nome": "Guido", "categoria": "Linguagens", "imagem_url": "/figurinhas/6/imagem"},
    {"id": 7, "nome": "Tim", "categoria": "Web", "imagem_url": "/figurinhas/7/imagem"},
    {"id": 8, "nome": "Ray", "categoria": "IA", "imagem_url": "/figurinhas/8/imagem"},
    {"id": 9, "nome": "Travis", "categoria": "Dados", "imagem_url": "/figurinhas/9/imagem"},
    {"id": 10, "nome": "Wes", "categoria": "Dados", "imagem_url": "/figurinhas/10/imagem"},
    {"id": 11, "nome": "Edgar", "categoria": "Dados", "imagem_url": "/figurinhas/11/imagem"},
    {"id": 12, "nome": "Larry", "categoria": "Web", "imagem_url": "/figurinhas/12/imagem"},
    {"id": 13, "nome": "Michael", "categoria": "História", "imagem_url": "/figurinhas/13/imagem"},
    {"id": 14, "nome": "Salvatore", "categoria": "Dados", "imagem_url": "/figurinhas/14/imagem"},
    {"id": 15, "nome": "Eliot", "categoria": "IA", "imagem_url": "/figurinhas/15/imagem"},
    {"id": 16, "nome": "Linus", "categoria": "Sistemas", "imagem_url": "/figurinhas/16/imagem"},
    {"id": 17, "nome": "Dennis", "categoria": "Sistemas", "imagem_url": "/figurinhas/17/imagem"},
    {"id": 18, "nome": "Richard", "categoria": "Sistemas", "imagem_url": "/figurinhas/18/imagem"},
    {"id": 19, "nome": "Bill", "categoria": "Sistemas", "imagem_url": "/figurinhas/19/imagem"},
    {"id": 20, "nome": "Steve", "categoria": "Sistemas", "imagem_url": "/figurinhas/20/imagem"},
    {"id": 21, "nome": "Paulo", "categoria": "Alura", "imagem_url": "/figurinhas/21/imagem"},
    {"id": 22, "nome": "Guilherme", "categoria": "Alura", "imagem_url": "/figurinhas/22/imagem"},
    {"id": 23, "nome": "Gus", "categoria": "Alura", "imagem_url": "/figurinhas/23/imagem"},
    {"id": 24, "nome": "Mauricio", "categoria": "Alura", "imagem_url": "/figurinhas/24/imagem"},
    {"id": 25, "nome": "Andre", "categoria": "Alura", "imagem_url": "/figurinhas/25/imagem"},
    {"id": 26, "nome": "Guilherme", "categoria": "Alura", "imagem_url": "/figurinhas/26/imagem"},
    {"id": 27, "nome": "Gi", "categoria": "Alura", "imagem_url": "/figurinhas/27/imagem"},
    {"id": 28, "nome": "Vinicius", "categoria": "Alura", "imagem_url": "/figurinhas/28/imagem"},
    {"id": 29, "nome": "Rafa", "categoria": "Alura", "imagem_url": "/figurinhas/29/imagem"},
    # Comentando figurinhas que ainda não estão disponíveis (exemplo da 30 que não existe)
    # {"id": 30, "nome": "Em Breve...", "categoria": "Mistério", "imagem_url": "/figurinhas/30/imagem"}
]

# Endpoint GET "/figurinhas" que retorna a lista
@app.get("/figurinhas")
def listar_figurinhas():
    return figurinhas

# Endpoint GET "/figurinhas/{id}/imagem" que retorna o arquivo de imagem
@app.get("/figurinhas/{id}/imagem")
def obter_imagem(id: int):
    # Usa glob para encontrar o arquivo com prefixo "{id:02d}[!0-9]*" na pasta figurinhas/
    padrao = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")
    arquivos_encontrados = glob.glob(padrao)
    
    # Retorna 404 se não encontrar
    if not arquivos_encontrados:
        raise HTTPException(status_code=404, detail="Imagem não encontrada")
    
    # Retorna FileResponse com o primeiro arquivo encontrado
    return FileResponse(arquivos_encontrados[0])