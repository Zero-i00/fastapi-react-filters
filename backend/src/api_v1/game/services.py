from typing import Sequence, Optional

from sqlalchemy.ext.asyncio import AsyncSession

from src.api_v1.base.pagination import GetPagination
from src.api_v1.game.filters import GameSortScheme, GameSortEnum
from src.api_v1.game.filters.filters import GenerateGameFilters
from src.core.models import Game
from sqlalchemy import select, UnaryExpression, asc, desc


class GameService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    @staticmethod
    def __get_sort_option(sort: GameSortEnum) -> UnaryExpression:
        match sort:
            case GameSortEnum.LOW_PRICE:
                return asc(Game.price)
            case GameSortEnum.HIGH_PRICE:
                return desc(Game.price)
            case GameSortEnum.OLDEST:
                return asc(Game.released_date)
            case _:
                return desc(Game.released_date)


    async def get_game_list(self, filters: Optional[GameSortScheme] = None) -> Sequence[Game]:
        query = select(Game)
        if filters:
            pagination = GetPagination()(filters)
            current_filters = GenerateGameFilters()(filters)

            query = query.where(current_filters)
            query = query.order_by(self.__get_sort_option(filters.sort))
            query = query.offset(pagination.skip)
            query = query.limit(pagination.per_page)


        games_result = await self.session.scalars(query)
        return games_result.all()
