from fastapi import APIRouter, Depends, FastAPI

from app.config import Settings, get_config
from app.version import __version__

app = FastAPI()


@app.get("/info")
async def info(config: Settings = Depends(get_config)) -> dict:
    return {
        "app_name": config.app_name,
        "admin_email": config.admin_email,
        "repo": config.repo,
        "version": __version__,
    }
