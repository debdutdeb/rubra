import functools

from os import getenv

class Config:
    @functools.cached_property
    def mongo_url(self) -> str:
        url = getenv("MONGO_URL")
        if url:
            return url

        host = getenv("MONGODB_HOST", "localhost")
        user = getenv("MONGODB_USER", getenv("MONGODB_USERNAME", None))
        password = getenv("MONGODB_PASS", getenv("MONGODB_PASSWORD", None))
        port = getenv("MONGODB_PORT", 27017)
        database = getenv("MONGODB_DATABASE", "rubra")

        if user and not password:
            print("MONGODB_USER set but password not found, ignoring user")

        if not user and password:
            print("MONGODB_PASSWORD set but user not found, ignoring password")

        if user and password:
            return f"mongodb://{user}:{password}@{host}:${port}/{database}"

        return f"mongodb://{host}:{port}/{database}"

    @functools.cached_property
    def redis_url(self) -> str:
        url = getenv("REDIS_URL")
        if url:
            return url

        host = getenv("REDIS_HOST", "localhost")
        password = getenv("REDIS_PASS", getenv("REDIS_PASSWORD", None))
        user = getenv("REDIS_USER", getenv("REDIS_USERNAME", None))
        port = getenv("REDIS_PORT", 6379)
        database = getenv("REDIS_DATABASE", "rubra")

        if password:
            return f"redis://{user or ''}:{password}@{host}:{port}/{database}"

        return f"redis://{host}:{port}/{database}" 
