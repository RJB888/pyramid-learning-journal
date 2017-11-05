from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)


class JournalEntry(Base):
    __tablename__ = 'JournalEntries'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    body = Column(Text)
    date = Column()

Index('my_index', MyModel.name, unique=True, mysql_length=255)
