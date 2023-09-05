import os

import databases
from sqlalchemy import create_engine

sqlite_file_name = "../test.db"
base_dir = os.path.dirname(os.path.realpath(__file__)) # Actual carpeta

database_url = f"sqlite:///{os.path.join(base_dir,sqlite_file_name)}"

Engine = create_engine(database_url, connect_args={"check_same_thread": False}) # Motor

database = databases.Database(database_url)

