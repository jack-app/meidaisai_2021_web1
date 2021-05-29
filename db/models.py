from sqlalchemy import Column, Integer, String, Text, DateTime
from db.database import Base
from datetime import datetime


class Tweet(Base):
    __tablename__ = 'tweets' 
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    content = Column(Text)
    position_x = Column(String(128))
    position_y = Column(String(128))
    created_at = Column(DateTime, default=datetime.now())

    def __init__(self, name=None, content=None, position_x = None, position_y = None, created_at=None):
        self.name = name
        self.content = content
        self.created_at = created_at
        self.position_x = position_x
        self.position_y = position_y
    def __repr__(self):
        return '<Tweet { id = %r, name = %r, content = %r, created_at = %r}>' % (self.id, self.name, self.content, self.created_at)