from os import getenv

def get_mongo_database_name():
    return getenv("MONGO_DATABASE", "rubra_db")

def get_mongo_url() -> str:
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

def get_redis_url() -> str:
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

def get_litellm_url() -> str:
    url = getenv("LITELLM_URL")
    if url:
        return url

    host = getenv("LITELLM_HOST")
    port = getenv("LITELLM_PORT")

    return f"http://{host}:{port}"

def get_vector_db_url() -> str:
    url = getenv("VECTOR_DB_URL")
    if url:
        return url

    host = getenv("VECTOR_DB_HOST", "localhost")
    port = getenv("VECTOR_DB_PORT", 8010)
    name = getenv("VECTOR_DB_NAME", "similarity_search")

    return f"http://{host}:{port}/{name}"

mongo_database = get_mongo_database_name()

mongo_url = get_mongo_url()

litellm_url = get_litellm_url()

vector_db_url = get_vector_db_url()

redis_url = get_redis_url()
