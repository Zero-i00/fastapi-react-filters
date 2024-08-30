from enum import Enum
from typing import Optional

from src.api_v1.base import PaginationScheme
from src.core.models import PlatformEnum


class GameSortEnum(Enum):
    LOW_PRICE = 'LOW_PRICE'
    HIGH_PRICE = 'HIGH_PRICE'
    OLDEST = 'OLDEST'
    NEWEST = 'NEWEST'


class GameSortScheme(PaginationScheme):
    sort: Optional[GameSortEnum] = None
    search_term: Optional[str] = None
    genres: Optional[str] = None
    platform: Optional[PlatformEnum] = None
    rating: Optional[float] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None
