import os

PGUSER = os.environ["POSTGRES_USER"]
PGPASSWORD = os.environ["POSTGRES_PASSWORD"]
PGHOST = os.environ["POSTGRES_HOST"]
PGPORT = os.environ["POSTGRES_PORT"]
PGNAME = os.environ["POSTGRES_NAME"]

DB_URL = f"postgresql://{PGUSER}:{PGPASSWORD}@{PGHOST}:{PGPORT}/{PGNAME}"
