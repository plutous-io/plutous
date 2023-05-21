from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Plutous API",
    version="0.0.1",
)
apps = []

try:
    from plutous.trade.app import main as trade
    apps.append(trade.app)
except ImportError:
    pass

try:
    from plutous.trade.crypto.app import main as trade_crypto
    apps.append(trade_crypto.app)
except ImportError:
    pass

for a in apps:
    app.include_router(a)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello from Plutous API"}