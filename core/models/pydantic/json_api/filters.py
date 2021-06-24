from pydantic import BaseModel
from core.models.enums.filters import JsonAPIFiltersOperators


class Filter(BaseModel):
    name: str
    op: JsonAPIFiltersOperators
    val: str
