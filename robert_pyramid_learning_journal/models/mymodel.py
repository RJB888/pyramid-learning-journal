from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


# class MyModel(Base):
#     __tablename__ = 'models'
#     id = Column(Integer, primary_key=True)
#     name = Column(Text)
#     value = Column(Integer)


class JournalEntry(Base):
    __tablename__ = 'journals'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    body = Column(Text)
    author = Column(Text)
    date = Column(Text)

# Index('my_index', JournalEntry.title, unique=True, mysql_length=255)
