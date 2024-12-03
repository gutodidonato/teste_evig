from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str 
    ALGORITHM: str = "HS256"
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    LLM_MODEL: str
    LLM_URL: str
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()