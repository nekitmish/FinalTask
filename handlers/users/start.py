import re
from re import compile

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from keyboards.inline.buy_button import gen_buy_button
from loader import dp
from states.register import Registered
from utils.db_api import db_commands as commands
from utils.misc.ref_reg import ref_reg


@dp.message_handler(CommandStart(), user_id=ADMINS)
async def admin_start(message: types.Message):
    try:
        await commands.add_user(user_id=message.from_user.id, name=message.from_user.full_name,
                                referral=message.from_user.id)
    except commands.DBUserExistException:
        await message.answer("Вы уже зарегистрированы")
        await Registered.Reg.set()
        return
    await Registered.Reg.set()
    await message.answer(f"Привет, {message.from_user.full_name}! Ты зарегистрирован!")


@dp.message_handler(CommandStart(deep_link=compile(r"i\d+$")), state="*")
async def deep_link_item(message: types.Message):
    item_id = re.search(r'i(\d+)', message.get_args()).group(1)
    try:
        item = await commands.select_item(int(item_id))
    except Exception:
        await message.answer("Некорректный код товара")
        return

    await dp.bot.send_photo(message.from_user.id, photo=item.thumb_url,
                            caption=f"{item.label}\n\n{item.price // 100}$\n\n{item.description}\n\n"
                                    f"В наличии {item.quantity}",
                            reply_markup=gen_buy_button(int(item_id)))


@dp.message_handler(CommandStart(deep_link=compile(r"\d+$")), state=None)
async def deep_link_start(message: types.Message):
    await ref_reg(message, message.get_args())


@dp.message_handler(CommandStart(), state=None)
async def unknown_start(message: types.Message):
    await message.answer("Введи код приглашения или перейди по реферальной ссылке")


@dp.message_handler(state=None)
async def input_ref_key(message: types.Message):
    await ref_reg(message, message.text)


@dp.message_handler(CommandStart(), state=Registered.Reg)
async def unknown_start(message: types.Message):
    await message.answer("Вы уже зарегистрированы")


@dp.message_handler(state='*', content_types=types.ContentType.ANY)
async def unknown_message(message: types.Message):
    await message.answer("Это действие не предусмотрено")
