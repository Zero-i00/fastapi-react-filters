from typing import Optional, List

from src.api_v1.game.filters import GameSortEnum, GameSortScheme
from sqlalchemy import UnaryExpression, asc, desc, or_, and_, ColumnElement

from src.core.models import Game, GenreEnum, PlatformEnum


class GenerateGameFilters:

    def __call__(self, data: GameSortScheme) -> ColumnElement[bool]:
        filters = []

        if data.search_term:
            filters.append(self.__get_search_term_filter(data.search_term))

        if data.rating:
            filters.append(self.__get_rating_filters(data.rating))

        if data.min_price or data.max_price:
            filters.append(self.__get_price_filter(data.min_price, data.max_price))

        if data.genres:
            filters.append(self.__get_genre_filter(data.genres))

        if data.platform:
            filters.append(self.__get_platform_filter(data.platform))

        return and_(*filters)


    @staticmethod
    def __get_search_term_filter(search_term: str) -> ColumnElement[bool] | None:
        if not search_term:
            return None

        search_pattern = f"%{search_term}%"
        return or_(
            Game.title.ilike(search_pattern),
            Game.developer.ilike(search_pattern),
            Game.publisher.ilike(search_pattern)
        )

    @staticmethod
    def __get_rating_filters(rating: float) -> ColumnElement[bool]:
        return Game.rating >= rating

    @staticmethod
    def __get_price_filter(min_price: Optional[float], max_price: Optional[float]) -> ColumnElement[bool]:
        price_filter = []

        if min_price is not None:
            price_filter.append(Game.price >= min_price)

        if max_price is not None:
            price_filter.append(Game.price <= max_price)

        return and_(*price_filter)

    @staticmethod
    def __get_genre_filter(genres: str) -> ColumnElement[bool]:
        genres_list: List[GenreEnum] = [GenreEnum(genre) for genre in genres.split('|')]
        genre_filters = [Game.genres.contains([genre]) for genre in genres_list]
        return or_(*genre_filters)

    @staticmethod
    def __get_platform_filter(platform: PlatformEnum) -> ColumnElement[bool]:
        return or_(Game.platforms.contains([platform]))
