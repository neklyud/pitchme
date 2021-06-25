from fastapi import FastAPI
from events.app.api.events import (
    EventsRouter,
    EventRouterList,
)
from events.app.models.pydantic.events import (
    EventsOutListSchema,
    EventSchema,
)
from fastapi import APIRouter


def register_routes(app: FastAPI) -> None:
    router: APIRouter = APIRouter()
    router.get(
        path="/api/event/",
        status_code=200,
        tags=["Event"],
        response_model=EventSchema,
    )(EventsRouter.get)
    router.post(
        path="/api/event/",
        status_code=200,
        tags=["Event"],
        response_model=EventSchema,
    )(EventsRouter.post)
    router.patch(
        path="/api/event/",
        status_code=200,
        tags=["Event"],
        response_model=EventSchema,
    )(EventsRouter.patch)
    router.get(
        path="/api/events/",
        status_code=200,
        tags=["Event"],
        response_model=EventsOutListSchema,
    )(EventRouterList.get)
    app.include_router(router)
