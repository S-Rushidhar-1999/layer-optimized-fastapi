from pydantic import BaseModel
from datetime import datetime

class BuildMetric(BaseModel):
    commit_id: str
    build_type: str
    build_time_seconds: int
    timestamp: datetime = datetime.utcnow()
