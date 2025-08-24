from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ActivitySchema(BaseModel):
    id: Optional[int]
    name: str
    description: Optional[str]
    timestamp: Optional[datetime]

class GoalSchema(BaseModel):
    id: Optional[int]
    title: str
    target: int
    progress: Optional[int]
    period: str

class ReminderSchema(BaseModel):
    id: Optional[int]
    message: str
    time: datetime

class SessionSchema(BaseModel):
    id: Optional[int]
    activity_id: int
    start_time: Optional[datetime]
    end_time: Optional[datetime]

class ReportSchema(BaseModel):
    id: Optional[int]
    title: str
    content: str
    created_at: Optional[datetime]
