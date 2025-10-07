from ..db import Base
from sqlalchemy import Column, String, DateTime, UUID, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
import uuid
from datetime import datetime

# class User(Base):
#     __tablename__ = "users"
#     id = Column(UUID, primary_key=True, index=True, default=uuid.uuid4)
#     email = Column(String, unique=True, index=True)
#     auth0 = Column(String, unique=True, index=True)
#     name = Column(String)
#     created_at = Column(DateTime, default=datetime.now)
#     updated_at = Column(DateTime, default=datetime.now)


class InterviewProblem(Base):
    __tablename__ = "interview_problems"
    id = Column(UUID, primary_key=True, index=True, default=uuid.uuid4)
    problem_number = Column(String, unique=True, index=True)
    name = Column(String)
    category = Column(String)
    difficulty = Column(String)
    tags = Column(String)
    details = Column(JSONB)
    
    #solutions = Column(JSONB)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)



# class InterviewSession(Base):
#     __tablename__ = "interview_sessions"
#     id = Column(UUID, primary_key=True, index=True, default=uuid.uuid4)
#     user_id = Column(UUID, ForeignKey("users.id"))
#     interview_problem = Column(UUID, ForeignKey("interview_problems.id"))
#     resolution = Column(JSONB)
#     notes = Column(JSONB)
#     results = Column(JSONB)
#     status = Column(String)
#     system_design_diagram = Column(JSONB)
#     session_start_time = Column(DateTime)
#     session_end_time = Column(DateTime)
#     created_at = Column(DateTime, default=datetime.now)
#     updated_at = Column(DateTime, default=datetime.now)


