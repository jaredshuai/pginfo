from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from ..database import get_session
from ..models import Project, Device
from ..response import custom_response

router = APIRouter(prefix="/api/projects", tags=["projects"])

@router.post("/")
def create_project(project: Project, session: Session = Depends(get_session)):
    session.add(project)
    session.commit()
    session.refresh(project)
    return custom_response(project.dict(), msg="创建成功")

@router.get("/", response_model=List[Project])
def read_projects(name: str = None, session: Session = Depends(get_session)):
    if name:
        projects = session.exec(select(Project).where(Project.name.contains(name))).all()
    else:
        projects = session.exec(select(Project)).all()
    return projects

@router.get("/{project_id}", response_model=Project)
def read_project(project_id: int, session: Session = Depends(get_session)):
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.put("/{project_id}", response_model=Project)
def update_project(project_id: int, project: Project, session: Session = Depends(get_session)):
    db_project = session.get(Project, project_id)
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")
    project_data = project.dict(exclude_unset=True)
    for key, value in project_data.items():
        setattr(db_project, key, value)
    session.add(db_project)
    session.commit()
    session.refresh(db_project)
    return db_project

@router.delete("/{project_id}")
def delete_project(project_id: int, session: Session = Depends(get_session)):
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    session.delete(project)
    session.commit()
    return custom_response(None, msg="删除成功")

@router.get("/{project_id}/devices", response_model=List[Device])
