from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("ref", "Получить свою реферальную ссылку"),
        types.BotCommand("cancel", "Выти из режима покупки товара, если что-то пошло не так")
    ])
