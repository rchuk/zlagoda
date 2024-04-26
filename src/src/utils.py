import random
import string


async def like_format(query: str | None):
    if query is None:
        return "%"
    else:
        return f"%{query}%"


def generate_random_str_id(length: int) -> str:
    characters = string.ascii_letters + string.digits

    return "".join(random.choices(characters, k=length))
