from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, date
from enum import Enum
import json
from typing import List, Optional, Dict, Any
import uuid

class Status(Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"

def now_iso() -> str:
    return datetime.now().isoformat()

def parse_iso(iso_str: str) -> datetime:
    return datetime.fromisoformat(iso_str)

@dataclass
class User:
    id: str
    name: str
    email: str

    @staticmethod
    def create(name: str, email: str) -> "User":
        return User(id=str(uuid.uuid4()), name=name, email=email)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }
    
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "User":
        return User(id=data["id"], name=data["name"], email=data["email"])

@dataclass
class Task:
    id: str 
    title: str 
    description: str = ""
    assignee: Optional[User] = None
    status: Status = Status.TODO
    priority: int = 3
    created_at: str = field(default_factory=now_iso)
    due_date: Optional[str] = None
    tags: List[str] = field(default_factory=list)

    @staticmethod
    def create(title: str, description: str = "", priority: int = 3, due_date: Optional[date] = None) -> "Task":
        due_iso = due_date.isoformat() if due_date else None
        return Task(id=str(uuid.uuid4()), title=title, description=description, priority=priority, due_date=due_iso)
    
    def assign(self, user: User) -> None:
        self.assignee = user
        self.status = Status.IN_PROGRESS
    
    def complete(self) -> None:
        self.status = Status.DONE
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "assignee": self.assignee.to_dict() if self.assignee else None,
            "status": self.status.value,
            "priority": self.priority,
            "created_at": self.created_at,
            "due_date": self.due_date,
            "tags": self.tags
        }