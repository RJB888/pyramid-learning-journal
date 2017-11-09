"""Establish data model for database."""

from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime
)

from .meta import Base
from datetime import datetime

FMT = "%m/%d/%Y"


class JournalEntry(Base):
    """Create the model for the Journal Entry."""

    __tablename__ = 'journals'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    body = Column(Text)
    author = Column(Text, default="Robert Bronson")
    date = Column(DateTime, default=datetime.today())
