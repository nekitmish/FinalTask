from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from loader import dp
from states.register import Registered


@dp.message_handler(Command("cancel"), state=['purchase', 'enter_quantity'])
async def command_cancel(message: types.Message, state: FSMContext):
    await state.reset_state(with_data=True)
    await Registered.Reg.set()
