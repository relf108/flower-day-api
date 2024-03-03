"""Notifications router."""

from fastapi import APIRouter

notifications_router = APIRouter(prefix="/notifications", tags=["notifications"])

# TODO(Tristan Sutton): Make these endpoints user specific using OAuth Sessions


@notifications_router.get("")
async def read_notifications() -> list[dict[str, str]]:
    """Read notifications."""
    return [
        {
            "notificationTitle": "Notification Title",
            "notificationBody": "Notification Body",
        },
        {
            "notificationTitle": "Notification Title 2",
            "notificationBody": "Notification Body 2",
        },
        {
            "notificationTitle": "Notification Title 3",
            "notificationBody": "Notification Body 3",
        },
    ]


@notifications_router.post("/")
async def create_notifications() -> dict[str, str]:
    """Create notifications."""
    return [{"message": "Notification has been created"}]


@notifications_router.put("/")
async def update_notifications() -> dict[str, str]:
    """Update notifications."""
    return [{"message": "Notification has been updated"}]


@notifications_router.delete("/")
async def delete_notifications() -> dict[str, str]:
    """Delete notifications."""
    return [{"message": "Notification has been deleted"}]
