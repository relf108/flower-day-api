from fastapi import APIRouter

notifications_router = APIRouter(prefix="/notifications", tags=["notifications"])

@notifications_router.get("/")
async def read_notifications():
    return [{"message": "This is a notification"}]

@notifications_router.post("/")
async def create_notifications():
    return [{"message": "Notification has been created"}]

@notifications_router.put("/")
async def update_notifications():
    return [{"message": "Notification has been updated"}]

@notifications_router.delete("/")
async def delete_notifications():
    return [{"message": "Notification has been deleted"}]
