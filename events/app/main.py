from events.app.config import config
from fastapi import (
    FastAPI,
)
from core.utils.databases.postgres_helper import PostgresFacade
from events.app.routes import register_routes


def create_app() -> FastAPI:
    app = FastAPI(
        debug=config.DEBUG,
        title=config.APP_TITTLE,
    )
    register_routes(app)
    return app


app = create_app()
db = PostgresFacade(config)


@app.on_event("startup")
async def on_startup():
    await db.connect()


@app.on_event("shutdown")
async def on_shutdown():
    await db.disconnect()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, port=8001)
