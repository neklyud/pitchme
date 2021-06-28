from core.models.pydantic.json_api.filters import Filter
from core.models.enums.filters import JsonAPIFiltersOperators
from typing import List
from sqlalchemy import text


def filter_converter(filters: List[Filter], query):
    for i_filter in filters:
        field_name = i_filter.name
        operation = i_filter.op
        value = i_filter.val
        if isinstance(value, str):
            value = '\'{value}\''.format(value=value)
        if operation is JsonAPIFiltersOperators.eq:
            query = query.where(text("{field_name} = {value}".format(field_name=field_name, value=value)))
        if operation is JsonAPIFiltersOperators.between and isinstance(value, list):
            for i_num, i_val in enumerate(value):
                if isinstance(i_val, str):
                    value[i_num] = '\'{value}\''.format(value=i_val)
            query = query.where(
                text(
                    "{field_name} BETWEEN {value_1} AND {value_2}".format(
                        field_name=field_name,
                        value_1=value[0],
                        value_2=value[1],
                    )
                )
            )
    return query
