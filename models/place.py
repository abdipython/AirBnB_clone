#!/usr/bin/python3

"""It defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """ It represents the place.

    Attributes:
        city_id (str): City id.
        user_id (str): User id.
        name (str): Name of place.
        description (str): Description of the place.
        number_rooms (int): No of rooms at the place.
        number_bathrooms (int): NO of bathrooms at the place.
        max_guest (int): Maximum no of guests allowed in the place.
        price_by_night (int): Price by night of the place.
        latitude (float): Latitude of place.
        longitude (float): Longitude of  place.
        amenity_ids (list): List of amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
