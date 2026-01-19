from fastapi import APIRouter
from .models import Item
from .db import collection

router = APIRouter()

@router.post("/items")
def create_item(item: Item):
    collection.insert_one(item.dict())
    return {"message": "Item created"}

@router.get("/items")
def get_items():
    return list(collection.find({}, {"_id": 0}))
