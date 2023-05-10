import os

import yaml
from pydantic import BaseModel


class BaseConfig(BaseModel):
    __section__ = ""

    @classmethod
    def from_file(
        cls, path: str = os.environ.get("PLUTOUS_CONFIG_PATH", "./plutous.yaml")
    ) -> "BaseConfig":
        with open(path, "r") as f:
            data: dict = yaml.safe_load(f)
            section = cls.__section__.split("/")
            for key in section:
                if not key:
                    continue
                data = data.get(key, {})
        return cls(**data)


class Db(BaseModel):
    host: str
    port: int
    user: str
    password: str
    database: str


class Config(BaseConfig):
    db: Db

config = Config.from_file()