import contextlib
from typing import AsyncIterator

import uvicorn
from fastapi import FastAPI

from src.api_v1.game.controllers import router as game_router
from src.core.db.database import db_manager
from config import config


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    db_manager.init(config.DATABASE_URL)
    # await db_manager.create_tables()
    # async with db_manager.session() as session:
    #     await seed_games(session)

    yield
    await db_manager.close()


app = FastAPI(title='Site Filters', lifespan=lifespan)

app.include_router(prefix='/api/v1', router=game_router)


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)