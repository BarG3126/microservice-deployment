"""Schema for Apartment."""

from pydantic import BaseModel


class Apartment(BaseModel):
    """
    Apartment Schema.

    area (float): Area of apartment on square meters.
    constraction_year (int): Year apartment was constructed.
    bedrooms (int): Number of bedrooms in the apartment.
    garden_area (str): Apartment garden area
    balcony_present (str): Apartment balcony precence
    parking_present (str): Apartment parking precence
    furnished (str): Indicated if the apartment in furnished.
    garage_present(str): Apartment garage precence
    storage_present (str): Apartment storage precence
    """

    area: int
    construction_year: int
    bedrooms: int
    garden_area: int
    balcony_present: int
    parking_present: int
    furnished: int
    garage_present: int
    storage_present: int
