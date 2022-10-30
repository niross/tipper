from typing import Union

from pydantic import BaseModel


class TipReport(BaseModel):
    id: Union[int, None] = None
    latitude: float
    longitude: float
    number_of_items: Union[int, None] = None
    description: Union[str, None] = None
    is_hazardous: Union[bool, None] = None
    image: Union[str, None] = None
    reporter_title: Union[str, None] = None
    reporter_first_name: Union[str, None] = None
    reporter_last_name: Union[str, None] = None
    reporter_email: Union[str, None] = None
    reporter_phone: Union[str, None] = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "latitude": 51.4620742,
                "longitude": -0.1905076,
                "number_of_items": 1,
                "description": "A lot of rubbish",
                "is_hazardous": True,
            }
        }
