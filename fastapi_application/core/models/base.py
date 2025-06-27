from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import declared_attr

from fastapi_application.core.config import settings
from utils import camel_case_to_snake_case


class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(
        naming_convention=settings.db.naming_convention,
    )

    @declared_attr
    def __tablename__(cls) -> str: # pylint: disable=no-self-argument
        return f"{camel_case_to_snake_case(cls.__name__)}s"
    