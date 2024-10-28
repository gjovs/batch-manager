from typing import TypedDict
from dotenv import load_dotenv
import os

load_dotenv()

class DatabaseConfigTypedDict(TypedDict):
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

class Config:
    DATABASE: DatabaseConfigTypedDict = {
      "DB_HOST": os.getenv("DB_HOST"),
      "DB_PORT": os.getenv("DB_PORT"),
      "DB_NAME": os.getenv("DB_NAME"),
      "DB_USER": os.getenv("DB_USER"),
      "DB_PASSWORD": os.getenv("DB_PASSWORD")
    }
