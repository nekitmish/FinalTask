from dataclasses import dataclass
from typing import List

from aiogram.dispatcher import FSMContext
from aiogram.types import LabeledPrice

import utils.db_api.db_commands as commands
from data import config


@dataclass
class Item:
    title: str
    description: str
    start_parameter: str
    currency: str
    prices: List[LabeledPrice]
    provider_data: dict = None
    photo_url: str = None
    photo_size: int = None
    photo_width: int = None
    photo_height: int = None
    need_name: bool = False
    need_phone_number: bool = False
    need_email: bool = False
    need_shipping_address: bool = False
    send_phone_number_to_provider: bool = False
    send_email_to_provider: bool = False
    is_flexible: bool = False

    provider_token: str = config.PROVIDER_TOKEN

    def generate_invoice(self):
        return self.__dict__


async def generate_item(item_id: int, user_id: int, quantity: int, state: FSMContext):
    db_item = await commands.select_item(item_id)
    user = await commands.select_user(user_id)
    discount = user.coins
    price = db_item.price
    if price * quantity - discount < 100:
        discount = price * quantity - 100
    await state.update_data({'discount': discount})
    item = Item(
        title=db_item.label,
        description=db_item.description,
        start_parameter=f"create_invoice_{item_id}",
        currency="USD",
        prices=[
            LabeledPrice(
                label=f"{db_item.label}\nКоличество: {quantity}",
                amount=price * quantity,
            ),
            LabeledPrice(
                label="Скидка с учетом реферального баланса",
                amount=-discount,
            ),
        ],
        need_shipping_address=True,
        photo_url=db_item.thumb_url,
        is_flexible=True,
        photo_size=600,
        need_name=True,
        need_email=True,
        need_phone_number=True
    )
    return item
