from fastapi import FastAPI

app = FastAPI()

aluno = {
    "matricula": "2024118ISINF0024",
    "nome": "MARIA VALENTINA DA SILVA LEAL"
}

@app.get("/")
def inicio():
    return aluno
