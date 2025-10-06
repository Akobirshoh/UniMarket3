from fastapi import FastAPI 
app = FastAPI(title="UniMarket", 
version="0.1.0") 
@app.get("/health") 
def health(): 
    return {"status": "ok ya inoyatov akobir"}