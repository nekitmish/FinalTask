from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from utils.db_api import quick_commands as commands


class SuccessfulPayment(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        payment = message.successful_payment
        if payment is None:
            return False
        return True


