from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.item import Item
from utils.db_api.schemas.user import User


async def add_user(id: int, name: str, referral: int):
    try:
        user = User(id=id, name=name, referral=referral, coins=0)
        await user.create()
    except UniqueViolationError:
        pass


async def select_user(id: int):
    user = await User.query.where(User.id == id).gino.first()
    return user


async def select_user_by_ref(ref: str):
    user = await User.query.where(User.ref_link == ref).gino.first()
    return user


async def get_user_ref(id: int):
    return (await select_user(id)).id


async def add_coins(id: int):
    user = await select_user(id)
    if user is not None:
        coins = user.coins + 10
        await user.update(coins=coins).apply()
    else:
        print("User not found")


async def count_users():
    total = await db.func.count(User.id).gino.scalar()
    return total


async def add_item(label: str, thumb_url: str, description: str, price: int):
    try:
        item = Item(label=label, thumb_url=thumb_url, description=description, price=price)
        await item.create()
    except UniqueViolationError:
        pass


async def get_items():
    items = await Item.query.order_by(Item.label).gino.all()
    return items


async def find_items(text: str):
    items = await Item.query.where(Item.label.like(f'%{text}%')).gino.all()
    return items


async def select_item(item_id: int):
    item = await Item.query.where(Item.id == item_id).gino.first()
    return item
