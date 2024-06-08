from typing import Optional
from pydantic import BaseModel,Field

class Movie(BaseModel):
    id: Optional [int] =None
    title: str = Field(min_length=5, max_length=15)
    overview:str = Field(min_length=10, max_length=50)
    year: int = Field(default= 2020 , le=2022)
    rating: float= Field(ge=1, le=10)
    category:str= Field(min_length=5, max_length=15)
