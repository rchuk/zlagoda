import os
from datetime import timedelta

SECRET_KEY = os.environ["SECRET_KEY"]
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_TIME = timedelta(days=1)
