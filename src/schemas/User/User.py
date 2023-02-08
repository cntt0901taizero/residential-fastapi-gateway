from datetime import datetime

from pydantic import Field
from pydantic import BaseModel, BaseSettings


class UserDetailOut(BaseModel):
    id: int = Field(..., ge=1)
    created_at: datetime
    created_by: str = Field(max_length=180)
    name: str = Field(..., max_length=100)
    host_name: str = Field(...)
    is_host: bool = Field(..., description="自組織のイベントか")
    session_count: int = Field(ge=0, description="イベントに紐づくセッション数")
    event_user_count: int = Field(ge=0, description="イベント参加人数")
