"""Constants used in the project."""

import secrets

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
SECRET_KEY = secrets.token_hex(32)
