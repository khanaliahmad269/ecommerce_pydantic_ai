"""
order management routes for placing new orders"""

from fastapi import APIRouter
from ..models import Order
from ..database import orders_collection

router = APIRouter(prefix="/orders",tags=["Orders"])


@router.post("/")
def place_order(order: Order):
    """
    Place a new order for a user
    """
    order_data= order.model_dump() if hasattr(order,"model_dump") else order.dict()  
    orders_collection.insert_one(order_data)
    return{"message":"Order Placed Successfully"}