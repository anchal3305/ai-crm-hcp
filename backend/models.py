from sqlalchemy import Column, Integer, String, Text
from db import Base

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    doctor_name = Column(String(100))
    interaction_type = Column(String(50))
    topics = Column(Text)
    sentiment = Column(String(20))
    outcomes = Column(Text)
    follow_up = Column(Text)
