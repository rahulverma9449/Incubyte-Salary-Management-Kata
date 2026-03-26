from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./employees.db"
    # DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/incubyte_salary_db
    

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()