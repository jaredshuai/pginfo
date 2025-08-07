
from datetime import datetime
from enum import Enum
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class Status(str, Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    ERROR = "error"


class Project(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    devices: List["Device"] = Relationship(back_populates="project")


class Device(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    brand: Optional[str] = None
    model: Optional[str] = None

    ip_address: Optional[str] = None
    subnet_mask: Optional[str] = None
    gateway: Optional[str] = None

    photo: Optional[str] = None

    longitude: Optional[float] = None
    latitude: Optional[float] = None

    remote_code: Optional[str] = None
    remote_password: Optional[str] = None

    location: Optional[str] = None
    status: Optional[Status] = None

    product_manual: Optional[str] = None

    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    project_id: Optional[int] = Field(default=None, foreign_key="project.id")
    project: Optional[Project] = Relationship(back_populates="devices")

