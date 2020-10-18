import logging
import os
from typing import Dict

import sqlalchemy  # type: ignore  #pylint: disable=E0401

logging.basicConfig(level="INFO", format="%(asctime)s %(message)s")


config: Dict[str, str] = {
    "username": os.environ.get("PG_REMOTE_USERNAME", ""),
    "password": os.environ.get("PG_REMOTE_PASSWORD", ""),
    "host": os.environ.get("PG_REMOTE_HOST", ""),
    "port": os.environ.get("PG_REMOTE_PORT", ""),
    "database": os.environ.get("PG_REMOTE_DATABASE", ""),
    "sslmode": os.environ.get("PG_REMOTE_SSLMODE", ""),
}


def get_engine(creds: Dict[str, str] = config) -> sqlalchemy.engine:

    url: str = "postgresql+psycopg2://{}:{}@{}:{}/{}?sslmode={}".format(*[creds[key] for key in creds.keys()])

    if url == "postgresql+psycopg2://{}:{}@{}:{}/{}?sslmode={}":
        raise Exception("Missing details in config")

    engine: sqlalchemy.engine = sqlalchemy.create_engine(url)
    logging.info(engine)
    engine.connect()

    return engine
