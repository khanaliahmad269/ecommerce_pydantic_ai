""""
pydantic models for data validation and serialization
"""

from pydantic import BaseModel
from typing import List,Optional

## type hinting

class Product(BaseModel):
    """Product Model for store inventory"""
    name:str
    description: str
    price: int
    category: str
    size: list[str]  #s #m #l #xl 
    color: list[str] #red,blue,green,yellow
    image: str  #url of picsum photos


class Order(BaseModel):
    """Order placement model"""
    user_email:str
    product_name:str
    quantity: int



class CartItem(BaseModel):
    """Shopping cart item model"""

    user_email:str
    product_name:str
    quantity:int
