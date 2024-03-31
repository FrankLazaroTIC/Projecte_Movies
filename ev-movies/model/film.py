import datetime
from pydantic import BaseModel

class Films(BaseModel):
	title: str
	director: str
	year: int
	genre: str
	rating: int 
	country: str
  