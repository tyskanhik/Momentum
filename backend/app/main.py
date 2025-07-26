from fastapi import FastAPI
from app.api.routers.cards import router as cards_router
from app.api.routers.users import router as users_router
from app.core.config import Config
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.mount("/static", StaticFiles(directory=Config.STATIC_DIR), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=Config.ALLOWED_ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cards_router, prefix="/cards")
app.include_router(users_router, prefix="/users")

@app.get("/")
def hello():
    return {"message": "Hello, FastAPI!"}