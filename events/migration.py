import pathmagic
from events.app.config import config
from core.utils.databases.create_database import DBCreator
from yoyo import read_migrations
from yoyo import get_backend

import asyncio
import argparse

backend = get_backend(config.DATABASE_DSN)
migrations = read_migrations(config.PATH_TO_MIGRATIONS)


def apply_migrations():
    with backend.lock():
        backend.apply_migrations(migrations)


def rollback_migration():
    with backend.lock():
        backend.rollback_migrations(migrations)


async def create_database_and_run_migrations():
    parser = argparse.ArgumentParser(description="Migration arguments")
    parser.add_argument('--apply', action='store_true', help='Apply migrations')
    parser.add_argument('--rollback', action='store_true', help='Rollback migrations')
    args = parser.parse_args()
    await DBCreator.create(config=config)
    if args.apply:
        apply_migrations()
    elif args.rollback:
        rollback_migration()


loop = asyncio.get_event_loop()
loop.run_until_complete(create_database_and_run_migrations())
