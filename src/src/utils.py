import random
import string
from decimal import Decimal


async def like_format(query: str | None):
    if query is None:
        return "%"
    else:
        return f"%{query}%"


def float_to_decimal(value: float, precision: int = 4) -> Decimal:
    return Decimal(value).quantize(Decimal(10)**-precision)


def generate_random_str_id(length: int) -> str:
    characters = string.ascii_letters + string.digits

    return "".join(random.choices(characters, k=length))
