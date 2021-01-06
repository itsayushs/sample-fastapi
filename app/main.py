from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"data": "Hey World! This is a sample fastAPI GET Response."}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    #  http://127.0.0.1/items/5?q=somequery
    return {"item_id": item_id, "q": q}
