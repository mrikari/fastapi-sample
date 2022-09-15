from databases import Database
from dependencies import get_settings
from sqlalchemy import MetaData, create_engine

SQLALCHEMY_DATABASE_URL = get_settings().database_url

database = Database(SQLALCHEMY_DATABASE_URL)
metadata = MetaData()


def create_all():
    import schemas  # noqa #F401

    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
    metadata.create_all(engine)
