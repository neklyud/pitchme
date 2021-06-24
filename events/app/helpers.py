from core.utils.databases.alchemy import AlchemyHelper
from events.app.config import config


alchemy = AlchemyHelper(config=config)
