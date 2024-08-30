from typing import List
from datetime import datetime
from src.core.models import PlatformEnum, GenreEnum, Game, AgeRatingEnum


GAMES: List[Game] = [
    Game(
        title='The Witcher 3: Wild Hunt',
        genres=[GenreEnum.RPG, GenreEnum.ACTION],
        platforms=[PlatformEnum.PC, PlatformEnum.PLAYSTATION, PlatformEnum.XBOX, PlatformEnum.NINTENDO],
        released_date=datetime(2015, 5, 19),
        price=39.99,
        rating=9.5,
        age_rating=AgeRatingEnum.MATURE,
        developer='CD Projekt Red',
        publisher='CD Projekt',
        image='/uploads/games/witcher.jpg'
    ),
    Game(
        title='Red Dead Redemption 2',
        genres=[GenreEnum.ACTION, GenreEnum.ADVENTURE],
        platforms=[PlatformEnum.PC, PlatformEnum.PLAYSTATION, PlatformEnum.XBOX],
        released_date=datetime(2018, 10, 26),
        price=59.99,
        rating=9.7,
        age_rating=AgeRatingEnum.MATURE,
        developer='Rockstar Games',
        publisher='Rockstar Games',
        image='/uploads/games/rdr.jpg'
    ),
    Game(
        title='Cyberpunk 2077',
        genres=[GenreEnum.RPG, GenreEnum.ACTION],
        platforms=[PlatformEnum.PC, PlatformEnum.PLAYSTATION, PlatformEnum.XBOX],
        released_date=datetime(2020, 12, 10),
        price=59.99,
        rating=7.5,
        age_rating=AgeRatingEnum.MATURE,
        developer='CD Projekt Red',
        publisher='CD Projekt',
        image='/uploads/games/rdr.jpg'
    ),
    Game(
        title='God of War (2018)',
        genres=[GenreEnum.ADVENTURE],
        platforms=[PlatformEnum.PC, PlatformEnum.PLAYSTATION],
        released_date=datetime(2018, 4, 20),
        price=49.99,
        rating=9.8,
        age_rating=AgeRatingEnum.MATURE,
        developer='Santa Monica Studio',
        publisher='Sony Interactive Entertainment',
        image='/uploads/games/gow.jpg'
    ),
    Game(
        title='The Last of Us Part II',
        genres=[GenreEnum.ACTION, GenreEnum.ADVENTURE],
        platforms=[PlatformEnum.PLAYSTATION],
        released_date=datetime(2020, 6, 19),
        price=59.99,
        rating=9.3,
        age_rating=AgeRatingEnum.MATURE,
        developer='Naughty Dog',
        publisher='Sony Interactive Entertainment',
        image='/uploads/games/last.jpg'
    ),
    Game(
        title='Horizon Zero Dawn',
        genres=[GenreEnum.ACTION, GenreEnum.RPG],
        platforms=[PlatformEnum.PC, PlatformEnum.PLAYSTATION],
        released_date=datetime(2017, 2, 28),
        price=49.99,
        rating=9.0,
        age_rating=AgeRatingEnum.TEEN,
        developer='Guerrilla Games',
        publisher='Sony Interactive Entertainment',
        image='/uploads/games/horizon.jpg'
    ),
    Game(
        title='Grand Theft Auto V',
        genres=[GenreEnum.ACTION, GenreEnum.ADVENTURE],
        platforms=[PlatformEnum.PC, PlatformEnum.PLAYSTATION, PlatformEnum.XBOX],
        released_date=datetime(2013, 9, 17),
        price=29.99,
        rating=9.8,
        age_rating=AgeRatingEnum.MATURE,
        developer='Rockstar North',
        publisher='Rockstar Games',
        image='/uploads/games/gta.jpg'
    ),
    Game(
        title='The Legend of Zelda: Breath of the Wild',
        genres=[GenreEnum.ADVENTURE, GenreEnum.ACTION],
        platforms=[PlatformEnum.NINTENDO],
        released_date=datetime(2017, 3, 3),
        price=59.99,
        rating=9.7,
        age_rating=AgeRatingEnum.TEEN,
        developer='Nintendo EPD',
        publisher='Nintendo',
        image='/uploads/games/zelda.jpg'
    ),
    Game(
        title='Dark Souls III',
        genres=[GenreEnum.ACTION, GenreEnum.RPG],
        platforms=[PlatformEnum.PC, PlatformEnum.PLAYSTATION, PlatformEnum.XBOX],
        released_date=datetime(2016, 3, 24),
        price=49.99,
        rating=9.2,
        age_rating=AgeRatingEnum.MATURE,
        developer='FromSoftware',
        publisher='Bandai Namco Entertainment',
        image='/uploads/games/dark-souls.jpg'
    ),
    Game(
        title='DOOM Eternal',
        genres=[GenreEnum.ACTION, GenreEnum.SPORTS],
        platforms=[PlatformEnum.PC, PlatformEnum.PLAYSTATION, PlatformEnum.XBOX, PlatformEnum.NINTENDO],
        released_date=datetime(2020, 3, 20),
        price=59.99,
        rating=8.9,
        age_rating=AgeRatingEnum.MATURE,
        developer='id Software',
        publisher='Bethesda Softworks',
        image='/uploads/games/doom.jpg'
    ),
]
