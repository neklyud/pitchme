from pydantic import BaseModel, root_validator
from core.models.enums.filters import JsonAPIFiltersOperators
from typing import List


class Filter(BaseModel):
    name: str
    op: JsonAPIFiltersOperators
    val: str


class FilterList(BaseModel):
    filters: List[Filter]
