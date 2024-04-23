from typing import Optional

from pydantic import BaseModel, StrictStr, StrictInt


class CustomerCardEntity(BaseModel):
    id: StrictInt
    first_name: StrictStr
    last_name: StrictStr
    patronymic: Optional[StrictStr]
    phone_number: StrictStr
    discount_percent: StrictInt
    city: Optional[StrictStr]
    street: Optional[StrictStr]
    zip_code: Optional[StrictStr]
