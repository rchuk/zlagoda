import random
import string


def generate_random_str_id(length: int) -> str:
    characters = string.ascii_letters + string.digits

    return "".join(random.choices(characters, k=length))
