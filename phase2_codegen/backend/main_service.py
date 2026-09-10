# main.py
import os
import uuid
from datetime import datetime, timedelta, date
from enum import Enum

import bcrypt
from fastapi import FastAPI, Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import (
    Column,
    String,
    DateTime,
    Date,
    DECIMAL,
    Enum as SQLEnum,
    ForeignKey,
    create_engine,
    Boolean,
)
from sqlalchemy.orm import relationship, sessionmaker, declarative_base, Session

# --------------------
# Configuration
# --------------------
SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# --------------------
# Enums
# --------------------
class UserRole(str, Enum):
    admin = "admin"
    accountant = "accountant"
    viewer = "viewer"


class BillingCycle(str, Enum):
    monthly = "monthly"
    quarterly = "quarterly"
    annual = "annual"


class InvoiceStatus(str, Enum):
    draft = "draft"
    pending = "pending"
    paid = "paid"
    overdue = "overdue"
    voided = "voided"


# --------------------
# ORM Models
# --------------------
class Organization(Base):
    __tablename__ = "organizations"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    tax_id = Column(String, nullable=True)
    currency = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    users = relationship("User", back_populates="organization")
    clients = relationship("Client", back_populates="organization")
    invoices = relationship("Invoice", back_populates="organization")
    payments = relationship("Payment", back_populates="organization")  # placeholder


class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    organization_id = Column(String, ForeignKey("organizations.id"), nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(SQLEnum(UserRole), nullable=False)

    organization = relationship("Organization", back_populates="users")


class Client(Base):