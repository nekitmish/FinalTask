from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def gen_show_kb(item_id):
    show_item_kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Показать товар", url=f"https://t.me/nikitas_pretty_bot?start=i{item_id}")
        ]
    ])
    return show_item_kb
