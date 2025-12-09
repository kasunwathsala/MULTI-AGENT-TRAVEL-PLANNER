from pydantic import BaseModel, Field
from typing import List, Optional


class Traveler(BaseModel):
    adults: int = Field(..., description="Number of adult travelers")
    children: int = Field(..., description="Number of child travelers")

class Requirements(BaseModel):
    traveler: Traveler    

class RequirementsAgentResponseModel(BaseModel):
    requirements: Requirements
   