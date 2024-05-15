from functools import cached_property
from motor.motor_asyncio import AsyncIOMotorClient

from config import Config

class Connections:
    def __init__(self):
        self._config = Config()

    async def mongo_client(self):
        client = AsyncIOMotorClient(self._config.mongo_url)
        info = await client.server_info()
        print("[MongoDB] server info: ", info)

        return client
