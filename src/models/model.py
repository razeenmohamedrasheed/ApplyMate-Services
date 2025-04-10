from sqlalchemy import Column, Boolean, Integer, String, DateTime, func, ForeignKey, Enum, Date
from sqlalchemy.orm import relationship, declarative_base
from db import Base
import enum

Base = declarative_base()

# ------------------- Roles Table -------------------
class Roles(Base):
    __tablename__ = "user_roles"

    role_id = Column(Integer, primary_key=True, index=True)
    user_role = Column(String(50), unique=True, nullable=False)

    candidates = relationship("Candidates", back_populates="role")
    recruiters = relationship("Recruiters", back_populates="role")

# ------------------- Gender Enum -------------------
class GenderEnum(enum.Enum):
    male = "male"
    female = "female"
    other = "other"

# ------------------- Candidates Table -------------------
class Candidates(Base):
    __tablename__ = "candidates"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    dob = Column(Date, nullable=True)
    contact = Column(String,unique=True, nullable=False)
    gender = Column(Enum(GenderEnum), nullable=True)
    resume = Column(String(255), nullable=True)  
    github_url = Column(String(255), nullable=True)
    linkedin_url = Column(String(255), nullable=True)
    password = Column(String(255), nullable=False)
    has_experience = Column(Boolean, default=False)
    role_id = Column(Integer, ForeignKey("user_roles.role_id"), nullable=False)

    role = relationship("Roles", back_populates="candidates")


# ------------------- Recruiters Table -------------------
class Recruiters(Base):
    __tablename__ = "recruiters"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    dob = Column(Date, nullable=True)
    contact = Column(Integer,unique=True, nullable=False)
    gender = Column(Enum(GenderEnum), nullable=True)
    resume = Column(String(255), nullable=True)  
    linkedin_url = Column(String(255), nullable=True)
    password = Column(String(255), nullable=False)
    company_name = Column(String(255), nullable=False)
    role_id = Column(Integer, ForeignKey("user_roles.role_id"), nullable=False)

    role = relationship("Roles", back_populates="recruiters")