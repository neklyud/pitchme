from enum import Enum


class JsonAPIFiltersOperators(str, Enum):
    eq: str = "eq"
    in_: str = "in"
    ne: str = "ne"
    between: str = "between"
