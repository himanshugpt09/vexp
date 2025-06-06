from fastapi import FasrtAPI, Request

app = FastAPI ()

@app.get("/")
def index():
    return {"message": "Hello, World!"
    }

