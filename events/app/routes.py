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
from events.app.api.users import UsersRouter, UsersRouterList
from events.app.models.pydantic.users import (
    UsersSchema,
    UsersOutListSchema,
)
from events.app.api.filters import FiltersRouter, FiltersRouterList
from events.app.models.pydantic.filters import FiltersSchema, FiltersOutListSchema


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

    users_router: APIRouter = APIRouter()
    users_router.get(
        path="/api/user/",
        status_code=200,
        tags=["Users"],
        response_model=UsersSchema,
    )(UsersRouter.get)

    users_router.patch(
        path="/api/user/",
        status_code=200,
        tags=["Users"],
        response_model=UsersSchema,
    )(UsersRouter.patch)

    users_router.post(
        path="/api/user/",
        status_code=200,
        tags=["Users"],
        response_model=UsersSchema,
    )(UsersRouter.post)
    users_router.get(
        path="/api/users/",
        status_code=200,
        tags=["Users"],
        response_model=UsersOutListSchema,
    )(UsersRouterList.get)
    app.include_router(users_router)

    filter_router: APIRouter = APIRouter()
    filter_router.get(
        path="/api/filter",
        status_code=200,
        tags=["Filters"],
        response_model=FiltersSchema,
    )(FiltersRouter.get)
    filter_router.get(
        path="/api/filters",
        status_code=200,
        tags=["Filters"],
        response_model=FiltersOutListSchema,
    )(FiltersRouterList.get)
    filter_router.post(
        path="/api/filter",
        status_code=200,
        tags=["Filters"],
        response_model=FiltersSchema,
    )(FiltersRouter.post)
    app.include_router(filter_router)
