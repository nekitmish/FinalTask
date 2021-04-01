from aiogram import types

RU_POST_SHIPPING = types.ShippingOption(
    id="post_ru",
    title="Почтой России",
    prices=[
        types.LabeledPrice(
            "Почтой россии с трек-номером", 300
        )
    ]
)

POST_SHIPPING = types.ShippingOption(
    id='post',
    title="Почтой России за границу",
    prices=[
        types.LabeledPrice(
            "Почтой России за пределы страны", 500
        )
    ]
)

EMS_SHIPPING = types.ShippingOption(
    id='EMS',
    title="Курьерской службой Почты России",
    prices=[
        types.LabeledPrice(
            "Курьерской службой от Почты России", 1000
        )
    ]
)

DHL_SHIPPING = types.ShippingOption(
    id='DHL',
    title="DHL",
    prices=[
        types.LabeledPrice(
            'Курьерской службой DHL', 3000
        )
    ]
)