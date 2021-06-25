from core.models.pydantic.json_api.filters import Filter
from core.models.enums.filters import JsonAPIFiltersOperators
from typing import List
from sqlalchemy import text


def filter_converter(filters: List[Filter], query):
    for i_filter in filters:
        field_name = i_filter.name
        operation = i_filter.op
        value = i_filter.val
        print(field_name, value)
        if operation is JsonAPIFiltersOperators.eq:
            query = query.where(text("{field_name} = {value}".format(field_name=field_name, value=value)))
    return query
