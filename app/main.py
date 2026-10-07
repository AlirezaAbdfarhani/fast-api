# app/main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from app.database import engine, Base
from app import models  
from app.routers import customers, factor, products

app = FastAPI(
    redoc_url=None,
    description='this project written by Alireza abdfarhani',
    version='1.0.0'
)

Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(customers.router)
app.include_router(factor.router)
app.include_router(products.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Shop Management API"}

# @app.get("/offline-docs", response_class=HTMLResponse)
# async def offline_docs():
#     with open("app/offline_docs.html", "r", encoding="utf-8") as f:
#         return f.read()