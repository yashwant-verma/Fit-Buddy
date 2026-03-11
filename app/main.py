from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routes import router

app = FastAPI(title="FitBuddy AI")

# static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# include router
app.include_router(router)