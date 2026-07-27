"""
Shopping cart routes for adding and retrieving items
"""


from fastapi import APIRouter
from ..models import CartItem
from ..database import cart_collection

router = APIRouter(prefix="/cart",tags=["Cart"])


@router.post("/add")
def add_to_cart(item: CartItem):
    """
    Add an item to the user's shopping cart."""
    item_data= item.model_dump() if hasattr(item,"model_dump") else item.dict()
    cart_collection.insert_one(item_data)
    return{"message":"Item added to to cart"}


@router.get("/{user_email}")
def get_cart(user_email:str):
    """
    Get all the shopping cart items for a specific user
    """
    items=list(cart_collection.find({"user_email": user_email}, {"_id":0}))
    return items

@router.delete("/{user_email}")
def clear_cart(user_email:str):
    """
    Clear all shopping cart items for a specific user after checkout
    """
    cart_collection.delete_many({"user_email":user_email})
    return{"message": "Cart cleared successfully"}
