from pydantic import BaseModel
from typing import Optional, Dict, Any, List

class ChatRequest(BaseModel):
    user_id: str
    message: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    session_id: Optional[str] = None

class ChatResponse(BaseModel):
    reply: str
    sources: Optional[List[Dict[str, Any]]] = []
    meta: Optional[Dict[str, Any]] = {}
