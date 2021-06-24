from enum import Enum


class JsonAPIFiltersOperators(str, Enum):
    eq: str = "eq"
    in_: str = "between"
    ne: str = "ne"
