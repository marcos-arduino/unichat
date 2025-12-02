from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = ""
    
    # JWT
    SECRET_KEY: str = "tu-secret-key-aqui-cambiar-en-produccion"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # WebSocket
    WS_HEARTBEAT_INTERVAL: int = 30
    
    # CORS
    ALLOWED_ORIGINS: list = ["http://localhost:5173", "http://localhost:3000"]
    
    # Redis (opcional, para producción)
    REDIS_URL: Optional[str] = None
    
    class Config:
        env_file = ".env"

settings = Settings()
