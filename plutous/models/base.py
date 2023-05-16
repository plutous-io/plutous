import re
from datetime import datetime as dt

from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import Mapped, declared_attr, mapped_column


class BaseMixin:
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[dt] = mapped_column(TIMESTAMP, nullable=False)
    updated_at: Mapped[dt] = mapped_column(
        TIMESTAMP,
        nullable=False,
        default=dt.utcnow,
        onupdate=dt.utcnow,
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return re.sub("(?<!^)(?=[A-Z])", "_", cls.__name__).lower()
