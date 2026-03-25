from fastapi import FastAPI
from app.database import Base, engine
from app.api.employee_routes import router as employee_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Incubyte Salary Management API")

app.include_router(employee_router)