from core.utils.databases.alchemy import (
    Crud,
)
from events.app.models.alchemy.events import Event
from events.app.helpers import (
    alchemy,
)
from events.app.models.pydantic.events import (
    EventSchema,
    EventsOutListSchema,
)

event_crud = Crud(
    model=Event,
    session_maker=alchemy,
    response_schema=EventSchema,
    response_list_schema=EventsOutListSchema,
)



# class EventsCrud(BaseCrud):
#     alchemy_base: AlchemyHelper = alchemy
#
#     async def insert(self, new_item):
#         session_maker = alchemy.session
#         new_event = None
#         async with session_maker() as session:
#             insert_query = insert(Event).returning(*Event.__table__.columns).values(**new_item.dict(exclude_unset=True))
#             res = await session.execute(insert_query)
#             for i_scalar in res.fetchall():
#                 new_event = EventSchema.from_orm(i_scalar)
#             await session.commit()
#         return new_event
#
#     async def select(self, response_model, filters: Optional[List[Filter]] = None):
#         session_maker = alchemy.session
#         async with session_maker() as session:
#             selection = select(Event)
#             if filters:
#                 selection = filter_converter(filters, selection)
#             result = await session.execute(selection)
#             data = []
#             for row in result.scalars():
#                 data.append(self.to_schema(row, EventSchema))
#         if response_model is EventSchema and data:
#             return data[0]
#         if response_model is EventsOutListSchema:
#             return EventsOutListSchema(data=data)
#         raise Exception("Object not found")
#
#     async def update(self, response_model, updating_data: EventPatchSchema, filters: Optional[List[Filter]] = None):
#         session_maker = alchemy.session
#         async with session_maker() as session:
#             query = update(Event)
#             if filters:
#                 query = filter_converter(filters, query)
#             query = query.values(**updating_data.dict(exclude_unset=True))
#             query = query.execution_options(synchronize_session=None)
#             query = query.returning(*Event.__table__.columns)
#             result = await session.execute(query)
#             data = []
#             for i_res in result.fetchall():
#                 print(i_res)
#                 data.append(EventSchema.from_orm(i_res))
#             await session.commit()
#         if response_model is EventSchema and data:
#             return data[0]
#         if response_model is EventsOutListSchema:
#             return EventsOutListSchema(data=data)
#         raise Exception("Object not updated")
#
#     async def delete(self, filters: Optional[List[Filter]] = None):
#         session_maker = alchemy.session
#         async with session_maker() as session:
#             query = delete(Event)
#             if filters:
#                 query = filter_converter(filters, query)
#             query = query.execution_options(synchronize_session=None)
#             await session.execute(query)
#         return True
