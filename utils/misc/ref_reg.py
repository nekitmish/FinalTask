from aiogram import types

from states.register import Registered
from utils.db_api import db_commands as commands
from utils.misc.check_ref import check_valid_ref


async def ref_reg(message: types.Message, referrer_id: str):
    if await check_valid_ref(referrer_id):
        try:
            user = await commands.select_user(message.from_user.id)
        except Exception:
            await commands.add_coins(int(referrer_id))
            await commands.add_user(user_id=message.from_user.id,
                                    name=message.from_user.full_name,
                                    referral=int(referrer_id))
            await commands.add_ref(referral_id=await commands.select_user(int(message.from_user.id)),
                                   referrer_id=int(referrer_id))
            await Registered.Reg.set()
            await message.answer("Ты зарегистрирован по реферальной ссылке!")
            return

        await message.answer("Вы уже зарегистрированы")
        await Registered.Reg.set()

    else:
        await message.answer("Некорректный код")
