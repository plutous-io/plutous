import os

import yaml
from pydantic import BaseModel


class Db(BaseModel):
    host: str
    port: int
    user: str
    password: str
    database: str


class Config(BaseModel):
    db: Db

    @classmethod
    def from_file(
        cls, path: str = os.environ.get("PLUTOUS_CONFIG_PATH", "./plutous.yaml")
    ) -> "Config":
        with open(path, "r") as f:
            data: dict = yaml.safe_load(f)
        return cls(**data)

config = Config.from_file()