from typing import List

from src.core.models import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum as SQLEnum, ARRAY, DateTime, func
from datetime import datetime
from enum import Enum

class AgeRatingEnum(Enum):
    EVERYONE = "Everyone"
    TEEN = "Teen"
    MATURE = "Mature"
    ADULTS_ONLY = "Adults Only"
    NOT_RATED = "Not Rated"


class PlatformEnum(Enum):
    PC = "PC"
    PLAYSTATION = "PlayStation"
    XBOX = "Xbox"
    NINTENDO = "Nintendo"
    MOBILE = "Mobile"


class GenreEnum(Enum):
    ACTION = "Action"
    ADVENTURE = "Adventure"
    RPG = "RPG"
    STRATEGY = "Strategy"
    SPORTS = "Sports"
    PUZZLE = "Puzzle"
    HORROR = "Horror"


class Game(Base):
    title: Mapped[str]
    image: Mapped[str]

    released_date: Mapped[datetime]
    price: Mapped[float]
    rating: Mapped[float]
    age_rating: Mapped[AgeRatingEnum] = mapped_column(SQLEnum(AgeRatingEnum))
    developer: Mapped[str]
    publisher: Mapped[str]

    genres: Mapped[List[GenreEnum]] = mapped_column(ARRAY(SQLEnum(GenreEnum)))
    platforms: Mapped[List[PlatformEnum]] = mapped_column(ARRAY(SQLEnum(PlatformEnum)))

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
