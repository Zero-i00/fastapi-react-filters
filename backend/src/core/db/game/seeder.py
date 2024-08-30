from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.game.dame_data import GAMES
from src.core.models import Game


async def seed_games(session: AsyncSession) -> None:
    # Check if there are any existing games to avoid duplicate seeding
    existing_games = await session.execute(select(Game))
    if existing_games.scalars().first():
        print("Games already seeded.")
        return

    session.add_all(GAMES)
    await session.commit()
    print("Seeded games successfully.")
