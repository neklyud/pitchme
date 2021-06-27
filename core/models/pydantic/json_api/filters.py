from pydantic import BaseModel, validator
from core.models.enums.filters import JsonAPIFiltersOperators
from typing import List, Optional, Union


class Filter(BaseModel):
    name: str
    op: JsonAPIFiltersOperators
    val: Optional[Union[str, List[Union[int, str]]]]


class FilterList(BaseModel):
    filters: List[Filter]
