#!/usr/bin/python3

"""It defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """ It represents a review.

    Attributes:
        place_id (str): Place id.
        user_id (str):  User id.
        text (str):     Texts of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
