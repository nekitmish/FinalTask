from aiogram import types

from keyboards.inline.show_button import gen_show_kb


async def generate_answer(func, *args):
    results = []
    items = await func(*args)
    for item in items:
        article = types.InlineQueryResultArticle(
            id=item.id,
            title=item.label,
            thumb_url=item.thumb_url,
            description=item.price,
            input_message_content=types.InputMessageContent(message_text=item.label + '\n' + item.description),
            reply_markup=gen_show_kb(item.id)
        )
        results.append(article)
    return results
