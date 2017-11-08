from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base
from datetime import datetime

FMT = "%m/%d/%Y"

class JournalEntry(Base):
    __tablename__ = 'journals'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    body = Column(Text)
    author = Column(Text, default="Robert Bronson")
    date = Column(DateTime, default=datetime.today.strftime(FMT))

# Index('my_index', JournalEntry.title, unique=True, mysql_length=255)
