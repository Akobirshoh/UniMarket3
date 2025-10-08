from fastapi import FastAPI,  Query
from pydantic import BaseModel, Field
app = FastAPI(title="UniMarket", 
version="0.1.0") 
@app.get("/health") 
def health(): 
    return {"status": "ok ya inoyatov akobir"}
class HelloResponse(BaseModel):
 message: str = Field(..., examples=["Hello, Alice!"])
@app.get("/hello", response_model=HelloResponse)
def hello(name: str = Query("world", min_length=1, max_length=50)):
 return HelloResponse(message=f"Hello, {name}!")
@app.get("/") 
def root(): 
    return {"Это сайт": "ok Этот сайт работает"}