from sqlalchemy import create_engine
from sqlalchemy.engine import URL

from plutous.config import config


engine = create_engine(
    URL.create(
        drivername="postgresql+psycopg2",
        **config.db.dict(),
    )
)
