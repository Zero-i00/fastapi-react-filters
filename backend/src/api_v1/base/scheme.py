from typing import Optional

from pydantic import BaseModel

class PaginationScheme(BaseModel):
    page: Optional[int] = None
    per_page: Optional[int] = None
