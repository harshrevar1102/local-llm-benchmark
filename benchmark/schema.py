from pydantic import BaseModel


class Explanation(BaseModel):
    title: str
    summary: str
    example: str