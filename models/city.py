#!/usr/bin/python3

"""This defines a City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """ it represents a city.

    Attributes:
        state_id (str): State id.
        name (str):  Name of the city.
    """

    state_id = ""
    name = ""
