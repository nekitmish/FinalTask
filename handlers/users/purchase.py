import re

from aiogram import types
from aiogram.dispatcher import FSMContext

from data.shipping import RU_POST_SHIPPING, POST_SHIPPING, EMS_SHIPPING, DHL_SHIPPING
from keyboards.inline.callback_datas import buy_callback
from loader import dp
from loader import storage
from states.register import Registered
from utils.db_api.db_commands import select_item, add_purchase, edit_quantity, edit_coins
from utils.misc.item import generate_item


@dp.callback_query_handler(buy_callback.filter(), state=Registered.Reg)
async def ask_quantity(callback: types.CallbackQuery, callback_data: dict):
    await callback.answer(cache_time=60)
    item_id = int(callback_data.get("item_id"))
    await callback.message.edit_reply_markup(reply_markup=None)

    item = await select_item(item_id)
    if item.quantity < 0:
        await dp.bot.send_message(callback.from_user.id, "Сожалеем, этого товара не осталось в наличии :(")
        return

    await dp.bot.send_message(callback.from_user.id, "Введите количество товара")

    state = FSMContext(storage, callback.message.chat.id, callback.from_user.id)
    await state.set_state("enter_quantity")
    await state.set_data({'item_id': item_id})


@dp.message_handler(state="enter_quantity")
async def send_invoice(message: types.Message, state: FSMContext):
    if re.match(r"\d+$", message.text):
        quantity = int(message.text)
        item_id = (await state.get_data()).get('item_id')
        in_stock = (await select_item(item_id)).quantity
        if in_stock >= quantity > 0:
            await dp.bot.send_invoice(message.from_user.id,
                                      **(await generate_item(item_id, message.from_user.id,
                                                             quantity, state)).generate_invoice(),
                                      payload=message.from_user.id)
            await state.set_state("purchase")
            await state.update_data({'quantity': quantity})
            return
    await message.answer("Введите корректное количество")


@dp.shipping_query_handler(state='purchase')
async def choose_shipping(query: types.ShippingQuery):
    if query.shipping_address.country_code == "RU":
        await dp.bot.answer_shipping_query(query.id, ok=True,
                                           shipping_options=[RU_POST_SHIPPING, EMS_SHIPPING])
    else:
        await dp.bot.answer_shipping_query(query.id, ok=True,
                                           shipping_options=[POST_SHIPPING, EMS_SHIPPING, DHL_SHIPPING])


@dp.pre_checkout_query_handler(state='purchase')
async def pre_checkout(query: types.PreCheckoutQuery, state: FSMContext):
    await dp.bot.answer_pre_checkout_query(query.id, ok=True)
    await add_purchase(user_id=query.from_user.id, item_id=(await state.get_data()).get('item_id'),
                       quantity=(await state.get_data()).get('quantity'), amount=query.total_amount,
                       buyer_name=query.order_info.name, buyer_phone=query.order_info.phone_number,
                       address=f"{query.order_info.shipping_address.country_code},"
                               f" {query.order_info.shipping_address.city},"
                               f"{query.order_info.shipping_address.street_line1},"
                               f"{query.order_info.shipping_address.street_line2},"
                               f"POSTAL: {query.order_info.shipping_address.post_code}")
    await edit_quantity((await state.get_data()).get('item_id'), (await state.get_data()).get('quantity'))
    await edit_coins(query.from_user.id, (await state.get_data()).get('discount'))
    await state.reset_state(with_data=True)
    await Registered.Reg.set()
    await dp.bot.send_message(query.from_user.id, "Спасибо за покупку, ожидайте информации об отправке!")
