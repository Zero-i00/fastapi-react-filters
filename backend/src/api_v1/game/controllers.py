from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from src.api_v1.game import GameService
from src.api_v1.game.filters import GameSortScheme
from src.api_v1.game.schemes import GameScheme
from src.core.db.database import get_session

router = APIRouter(
    prefix='/games',
    tags=['games'],
)


@router.get('/', response_model=List[GameScheme], status_code=status.HTTP_200_OK)
async def get_game_list(
    session: AsyncSession = Depends(get_session),
    filters: GameSortScheme = Depends(),
):
    games_result = await GameService(session).get_game_list(filters)
    response_data = [
        GameScheme.model_validate(game).model_dump() for game in games_result
    ]

    return response_data

