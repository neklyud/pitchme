from fastapi import FastAPI
from events.app.api.events import EventsRouter
from events.app.models.pydantic.events import (
    EventsOutListSchema,
)


def register_routes(app: FastAPI) -> None:
    app.add_api_route(
        path="/api/event/",
        tags=["Event"],
        endpoint=EventsRouter.get,
        response_model=EventsOutListSchema,
    )
