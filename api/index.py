from fastapi import FastAPI, Request
from fastapi.middleware.cors import CorsMiddleware

app = FastAPI ()

app.add_middleware (
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return {"message": "Hello, World!"
    }

@app.get ("/api/params")
def search (request: Request):
    parameters = list ()
    parameter_value = list()


    for parameter_name in request.query_params.keys ():
        parameter_name = request.query_params.getlist (parameter_name)
        for value in parameter_values:
            parameters.append({
                "name": parameter_name,
                "value": value
            })
            
            

        print (parameters)

        return{
            "parameters": parameters,
        }