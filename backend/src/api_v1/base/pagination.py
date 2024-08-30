from src.api_v1.base import PaginationScheme
from dataclasses import dataclass


@dataclass
class PaginationType:
    per_page: int
    skip: int


class GetPagination:
    def __call__(self, data: PaginationScheme, default_per_page = 30) -> PaginationType:
        page = data.page or 1
        per_page = data.per_page or default_per_page

        skip = (page - 1) * per_page

        return PaginationType(
            per_page=per_page,
            skip=skip
        )
