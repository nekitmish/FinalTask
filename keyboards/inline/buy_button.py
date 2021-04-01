from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.callback_datas import buy_callback


def gen_buy_button(item_id: int):
    buy_kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton("Купить", callback_data=buy_callback.new(item_id=item_id))
        ]
    ])
    return buy_kb
