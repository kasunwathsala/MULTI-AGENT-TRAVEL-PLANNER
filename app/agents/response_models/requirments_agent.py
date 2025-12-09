from pydantic import BaseModel, Field
from typing import List, Optional


class TravelerProfile(BaseModel):
    """Traveler profile information."""

    adults: int = Field(..., description="Number of adult travelers")
    children: int = Field(..., description="Number of child travelers")

class AirportInfo(BaseModel):
    """Airport information with city and IATA code."""

    city: str = Field(..., description="City name")
    airport_iata: str = Field(..., description="IATA airport code")

class TripDetails(BaseModel):
    """Trip basic information."""

    type: str = Field(..., description="Trip type: one_way or round_trip")
    origin: AirportInfo = Field(..., description="Origin airport information")
    destination: AirportInfo = Field(..., description="Destination airport information")
    depart_date: str = Field(..., description="Departure date in YYYY-MM-DD format")
    return_date: Optional[str] = Field(
        None, description="Return date in YYYY-MM-DD format (for round trips)"
    )    

class Preferences(BaseModel):
    """User travel preferences."""

    cabin_class: str = Field(..., description="Cabin class: economy, premium, business")
    non_stop: bool = Field(..., description="Preference for non-stop flights")
    max_layovers: int = Field(..., description="Maximum number of layovers allowed")
    date_flex_days: int = Field(..., description="Date flexibility in days")
    interests: List[str] = Field(..., description="List of travel interests")

class Requirements(BaseModel):
    traveler: TravelerProfile    

class RequirementsAgentResponseModel(BaseModel):
    requirements: Requirements
   