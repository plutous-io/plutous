import re
from datetime import datetime as dt

from sqlalchemy import TIMESTAMP
from sqlalchemy import Enum as _Enum
from sqlalchemy import Index
from sqlalchemy.orm import Mapped, declared_attr, mapped_column


class BaseMixin:
    __name__: str

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[dt] = mapped_column(
        TIMESTAMP,
        default=dt.utcnow,
        nullable=False,
    )
    updated_at: Mapped[dt] = mapped_column(
        TIMESTAMP,
        nullable=False,
        default=dt.utcnow,
        onupdate=dt.utcnow,
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return re.sub("(?<!^)(?=[A-Z])", "_", cls.__name__).lower()

    @declared_attr.directive
    def __table_args__(cls) -> tuple:
        return (
            Index(
                f"ix_{cls.__tablename__}_created_at",
                "created_at",
            ),
            Index(
                f"ix_{cls.__tablename__}_updated_at",
                "updated_at",
            ),
        )


class Enum(_Enum):
    schema = None

    def __init__(self, *args, **kwargs):
        kwargs.pop("schema", None)
        super().__init__(schema=self.schema, *args, **kwargs)
