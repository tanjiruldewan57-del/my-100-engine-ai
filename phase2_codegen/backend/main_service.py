from datetime import datetime, timezone, timedelta
from enum import Enum
from typing import Optional, List
from uuid import UUID, uuid4

import jwt
from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, Field, ConfigDict
from sqlalchemy import (
    create_engine, Column, Integer, String, Float, Boolean, DateTime, Enum as SQLEnum, ForeignKey, Text, JSON
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, Session
from threading import Lock

# --- Configuration ---
BASE_URL = "http://localhost:8000"
DATABASE_URL = "sqlite:///./marketplace.db"
JWT_SECRET_KEY = "super-secret-key-for-production"
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
STRIPE_WEBHOOK_SECRET = "whsec_test_secret"

# --- Database Setup ---
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Thread lock for SQLite safety in this simplified backend
_db_lock = Lock()

def get_db():
    with _db_lock:
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

# --- Enums ---
class VendorStatus(str, Enum):
    PENDING = "pending"
    ACTIVE = "active"
    SUSPENDED = "suspended"
    CLOSED = "closed"

class InventoryReservationStatus(str, Enum):
    RESERVED = "reserved"
    CONSUMED = "consumed"
    EXPIRED = "expired"
    CANCELLED = "cancelled"

class OrderStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class PaymentStatus(str, Enum):
    UNPAID = "unpaid"
    PAID = "paid"
    REFUNDED = "refunded"
    FAILED = "failed"

class WebhookEventStatus(str, Enum):
    RECEIVED = "received"
    PROCESSING = "processing"
    PROCESSED = "processed"
    FAILED = "failed"

# --- Models (SQLAlchemy) ---

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

class VendorModel(Base):
    __tablename__ = "vendors"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    store_name = Column(String(255), nullable=False)
    status = Column(SQLEnum(VendorStatus), default=VendorStatus.PENDING, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    products = relationship("ProductModel", back_populates="vendor")

class ProductModel(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    vendor_id = Column(Integer, ForeignKey("vendors.id"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, default="")
    price = Column(Float, nullable=False)
    currency = Column(String(3), default="USD", nullable=False)
    sku = Column(String(100), unique=True, index=True, nullable=False)
    is