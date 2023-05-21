from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/contador/[quant]")
def cont(quant: int):
    lista = []
    for i in range(1, quant+1):
        lista.append(i)
    return {"contei até":quant, "resultado": lista}

if __name__ == "__main__":
    uvicorn.run(app, host="localhosst", port=8000)