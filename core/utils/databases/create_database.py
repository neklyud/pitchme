import asyncpg


class DBCreator(object):
    @classmethod
    async def create(cls, config) -> None:
        connection = await asyncpg.connect(user=config.DB_USER, password=config.DB_PASSWORD)
        database_name = await connection.fetch(
            "SELECT FROM pg_database WHERE datname='{db_name}'".format(
                db_name=config.DB_NAME
            )
        )
        if not database_name:
            await connection.execute("CREATE DATABASE {db_name}".format(db_name=config.DB_NAME))