from typing import Optional

from pydantic import BaseModel


class RAGRequest(BaseModel):
    query: str


class RAGUsedContext(BaseModel):
    image_url: str
    price: Optional[float] = None
    description: str


class RAGResponse(BaseModel):
    answer: str
    used_context: list[RAGUsedContext]
