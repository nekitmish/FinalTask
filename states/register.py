from aiogram.dispatcher.filters.state import StatesGroup, State


class Registered(StatesGroup):
    Unreg = State()
    Reg = State()
