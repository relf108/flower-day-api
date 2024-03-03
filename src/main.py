"""Entrypoint."""

from __future__ import annotations

import uvicorn
from fastapi import FastAPI

from src.auth.router import auth_router
from src.notifications.router import notifications_router

app = FastAPI()
app.include_router(notifications_router)
app.include_router(auth_router)


@app.get("/")
def read_root() -> dict[str, str]:
    """Root endpoint."""
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None) -> dict[str, int | str]:
    """Read item."""
    return {"item_id": item_id, "q": q}


def main() -> None:
    """Run the app."""
    uvicorn.run(app)


if __name__ == "__main__":
    main()
