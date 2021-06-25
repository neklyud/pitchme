from fastapi import FastAPI
from events.app.api.events import (
    EventsRouter,
    EventRouterList,
)
from events.app.models.pydantic.events import (
    EventsOutListSchema,
    EventSchema,
)
from events.app.models.pydantic.theme import (
    ThemeOutListSchema,
    ThemeSchema,
)
from events.app.models.pydantic.events_schema import (
    EventsThemesSchema,
    EventsThemesOutListSchema,
)
from events.app.api.events_themes import EventsThemesRouter, EventThemesRouterList
from events.app.api.theme import ThemeRouter, ThemeRouterList
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

    theme_router: APIRouter = APIRouter()
    theme_router.get(
        path="/api/theme/",
        status_code=200,
        tags=["Theme"],
        response_model=ThemeSchema,
    )(ThemeRouter.get)
    theme_router.post(
        path="/api/theme/",
        status_code=200,
        tags=["Theme"],
        response_model=ThemeSchema,
    )(ThemeRouter.post)
    theme_router.patch(
        path="/api/theme/",
        status_code=200,
        tags=["Theme"],
        response_model=ThemeSchema,
    )(ThemeRouter.patch)
    theme_router.get(
        path="/api/themes/",
        status_code=200,
        tags=["Theme"],
        response_model=ThemeOutListSchema,
    )(ThemeRouterList.get)
    app.include_router(theme_router)

    events_theme_router: APIRouter = APIRouter()
    events_theme_router.get(
        path="/api/event-theme/",
        status_code=200,
        tags=["EventsThemes"],
        response_model=EventsThemesSchema,
    )(EventsThemesRouter.get)
    events_theme_router.post(
        path="/api/event-theme/",
        status_code=200,
        tags=["EventsThemes"],
        response_model=EventsThemesSchema,
    )(EventsThemesRouter.post)
    events_theme_router.get(
        path="/api/events-themes/",
        status_code=200,
        tags=["EventsThemes"],
        response_model=EventsThemesOutListSchema,
    )(EventThemesRouterList.get)
    app.include_router(events_theme_router)
