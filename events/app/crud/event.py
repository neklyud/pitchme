from core.utils.databases.alchemy import (
    Crud,
)
from events.app.models.alchemy.events import Event
from events.app.models.alchemy.theme import Theme
from events.app.helpers import (
    alchemy,
)
from events.app.models.pydantic.events import (
    EventSchema,
    EventsOutListSchema,
)
from events.app.models.pydantic.theme import (
    ThemeSchema,
    ThemeOutListSchema,
)
from typing import (
    Optional,
    List,
)
from core.models.pydantic.json_api.filters import Filter
from events.app.models.alchemy.event_theme import EventsThemes
from events.app.models.pydantic.events_schema import (
    EventsThemesOutListSchema,
    EventsThemesSchema,
)

event_crud = Crud(
    model=Event,
    session_maker=alchemy,
    response_schema=EventSchema,
    response_list_schema=EventsOutListSchema,
)

theme_crud = Crud(
    model=Theme,
    session_maker=alchemy,
    response_schema=ThemeSchema,
    response_list_schema=ThemeOutListSchema,
)


class EventsThemesCrud(Crud):
    async def update(self, response_model, updating_data, filters: Optional[List[Filter]] = None):
        raise Exception("Cannot update events themes")

    async def delete(self, filters: Optional[List[Filter]] = None):
        raise Exception("Cannot delete events themes")


events_themes_crud = EventsThemesCrud(
    model=EventsThemes,
    session_maker=alchemy,
    response_schema=EventsThemesSchema,
    response_list_schema=EventsThemesOutListSchema,
)
