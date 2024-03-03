"""Models for the application."""

from __future__ import annotations

from datetime import datetime, timedelta

import pytz as tz
from jose import jwt
from pydantic import BaseModel

from src.auth.constants import ALGORITHM, SECRET_KEY


class Token(BaseModel):
    """Model for an auth token."""

    access_token: str
    token_type: str


class TokenData(BaseModel):
    """Model for auth token data."""

    email: str | None = None


class Auth:
    """Authentication class."""

    def get_access_token(
        self: Auth,
        data: dict,
        expires_delta: timedelta | None = None,
    ) -> str:
        """Get an access token."""
        to_encode = data.copy()
        expire = (
            datetime.now(tz=tz.utc) + expires_delta
            if expires_delta
            else datetime.now(tz=tz.utc) + timedelta(minutes=15)
        )
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    async def authenticate_user(self: Auth, email: str, password: str) -> dict:
        """Authenticate a user."""
        # user = UserObject().get(UserModel(email=email))
        # if not user:
        #     return False
        # if not verify_password(password, user.hashed_password):
        #     return False
        # return user
        return {"email": email, "password": password}
