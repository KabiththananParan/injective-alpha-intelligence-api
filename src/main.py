from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello World"}

@app.get("/market/health/{symbol}")
def get_Health(symbol: str):
    return {
        "Symbol": symbol,
        "liquidity_score": 80,
        "spread": 0.25,
        "volatility": 0.05
        }