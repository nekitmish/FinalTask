from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from states.register import Registered
from utils.db_api import db_commands as commands


@dp.message_handler(Command("ref"), state=Registered.Reg)
async def get_ref_link(message: types.Message):
    await message.answer("Вот твоя реферальная ссылка: "
                         + f"https://t.me/nikitas_pretty_bot?start={message.from_user.id}\n\n"
                           f"От тебя пришло {await commands.count_refs(message.from_user.id)}\n\n"
                           f"Твой баланс: {(await commands.select_user(message.from_user.id)).coins // 100}$")
