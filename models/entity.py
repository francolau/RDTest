from sqlalchemy import Column, Integer, String, Table, MetaData
from pydantic import BaseModel

metadata = MetaData()

entity = Table(
    'entity',
    metadata,
    Column("ID", Integer, primary_key=True, autoincrement=True),
    Column("field_1", String),
    Column("author", String),
    Column("description", String),
   Column("my_numeric_field",Integer),
   )

class EntityIn(BaseModel):
    field_1: str
    author: str
    description: str
    my_numeric_field: int

