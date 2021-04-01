from asgiref.sync import sync_to_async

from django_project.finalbot.usersmanage.models import Item, User, Referral, Purchase


class DBUserExistException(BaseException):
    pass


@sync_to_async
def add_user(user_id: int, name: str, referral: int):
    try:
        return User(user_id=int(user_id), name=name, referral_id=referral).save()
    except Exception:
        raise DBUserExistException


@sync_to_async
def select_user(user_id: int) -> User:
    return User.objects.get(user_id=user_id)


@sync_to_async
def add_coins(user_id: int):
    user = User.objects.get(user_id=user_id)
    if user is not None:
        user.coins = user.coins + 1000
        user.save()
    else:
        pass


@sync_to_async()
def edit_coins(user_id: int, value: int):
    user = User.objects.get(user_id=user_id)
    user.coins = user.coins - value
    user.save()


@sync_to_async
def get_items():
    return Item.objects.order_by('label').exclude(quantity=0)


@sync_to_async()
def find_items(text: str):
    return Item.objects.filter(label__contains=text).exclude(quantity=0)


@sync_to_async()
def select_item(item_id: int) -> Item:
    return Item.objects.get(id=item_id)


@sync_to_async()
def count_refs(referrer_id: int):
    return Referral.objects.filter(referrer_id=referrer_id).count()


@sync_to_async()
def add_ref(referrer_id: int, referral_id: User):
    print("Запись в таблице рефералов создана")
    return Referral(id=referral_id, referrer_id=referrer_id).save()


@sync_to_async()
def add_purchase(user_id: int, item_id: int, quantity: int, amount: int, buyer_name: str,
                 buyer_phone: str, address: str):
    print("Запись в таблице покупок создана")
    return Purchase(user_id=user_id, item_id=item_id, quantity=quantity, amount=amount, buyer_name=buyer_name,
                    buyer_phone=buyer_phone, address=address).save()


@sync_to_async()
def edit_quantity(item_id: int, quantity: int):
    db_item = Item.objects.get(id=item_id)
    db_item.quantity = db_item.quantity - quantity
    db_item.save()
