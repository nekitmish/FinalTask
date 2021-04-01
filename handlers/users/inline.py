from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp
from utils.db_api.db_commands import get_items, find_items
from utils.misc.query_answer import generate_answer


@dp.inline_handler(Text(equals=""), state='*')
async def empty_query(query: types.InlineQuery):
    await query.answer(results=await generate_answer(get_items), cache_time=5)


@dp.inline_handler(state='*')
async def process_query(query: types.InlineQuery):
    await query.answer(results=await generate_answer(find_items, query.query), cache_time=5)
