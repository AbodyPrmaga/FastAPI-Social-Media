from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os

ROOT = os.path.dirname(os.path.realpath('__file__'))
DB_PATH = os.path.join(ROOT,"database.db")

engine = create_engine(f"sqlite:///{DB_PATH}",echo=True)
with engine.connect() as conn:
    conn.exec_driver_sql("PRAGMA foreign_keys = ON")

Base = declarative_base()