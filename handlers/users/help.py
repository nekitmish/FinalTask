from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку",
            "/ref - Получить информацию о реферальной программе",
            "/cancel - Выйти из режима покупки товара, если что-то пошло не так",
            "\nДля выборов товаров вы можете использовать инлайн-режим.\n",
            "Для этого введите в любом диалоге: @имя_бота")
    
    await message.answer("\n".join(text))
