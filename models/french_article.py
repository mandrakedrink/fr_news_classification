from pydantic import BaseModel, conlist
from typing import List

class FrenchArticle(BaseModel):
    data: List[str]
    title: List[str]