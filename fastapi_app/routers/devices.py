from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from ..database import get_session
from ..models import Device
from ..response import custom_response

router = APIRouter(prefix="/api/devices", tags=["devices"])

@router.post("/")
def create_device(device: Device, session: Session = Depends(get_session)):
    session.add(device)
    session.commit()
    session.refresh(device)
    return custom_response(device.dict(), msg="创建成功")

@router.get("/", response_model=List[Device])
def read_devices(
    project_id: Optional[int] = None,
    name: Optional[str] = None,
    ip_address: Optional[str] = None,
    session: Session = Depends(get_session)
):
    query = select(Device)
    if project_id:
        query = query.where(Device.project_id == project_id)
    if name:
        query = query.where(Device.name.contains(name))
    if ip_address:
        query = query.where(Device.ip_address.contains(ip_address))
    devices = session.exec(query).all()
    return devices

@router.get("/{device_id}", response_model=Device)
def read_device(device_id: int, session: Session = Depends(get_session)):
    device = session.get(Device, device_id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    return device

@router.put("/{device_id}", response_model=Device)
def update_device(device_id: int, device: Device, session: Session = Depends(get_session)):
    db_device = session.get(Device, device_id)
    if not db_device:
        raise HTTPException(status_code=404, detail="Device not found")
    device_data = device.dict(exclude_unset=True)
    for key, value in device_data.items():
        setattr(db_device, key, value)
    session.add(db_device)
    session.commit()
    session.refresh(db_device)
    return db_device

