from typing import List
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from src.core.models import GenreEnum, PlatformEnum, AgeRatingEnum


class GameScheme(BaseModel):
    title: str
    image: str

    released_date: datetime
    price: float
    rating: float
    age_rating: AgeRatingEnum
    developer: str
    publisher: str

    genres: List[GenreEnum]
    platforms: List[PlatformEnum]

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
