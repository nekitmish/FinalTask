from django.db import models


class TimedBaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(TimedBaseModel):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(unique=True, verbose_name='ID пользователя Телеграм')

    name = models.CharField(max_length=50)
    referral_id = models.BigIntegerField(verbose_name='ID пригласившего пользователя')
    coins = models.IntegerField(verbose_name='Реферальные отчисления', default=0)

    def __str__(self):
        return f"№{self.id} ({self.user_id}) - {self.name}"


class Item(TimedBaseModel):
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=20, verbose_name='Название товара')
    thumb_url = models.CharField(verbose_name='Фото товара', max_length=200)
    description = models.CharField(max_length=2000, verbose_name='Описание товара')
    price = models.IntegerField(verbose_name='Цена товара')
    quantity = models.IntegerField(verbose_name='Количество в наличии')

    def __str__(self):
        return f"№{self.id} - {self.label}"


class Purchase(TimedBaseModel):
    class Meta:
        verbose_name = "Покупка"
        verbose_name_plural = "Покупки"

    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(verbose_name='ID покупателя')
    item_id = models.IntegerField(verbose_name='ID товара')
    quantity = models.IntegerField(verbose_name='Количество')
    amount = models.IntegerField(verbose_name='Сумма покупки')
    purchase_time = models.DateTimeField(verbose_name='Время покупки', auto_now_add=True)
    buyer_name = models.CharField(max_length=50, verbose_name='Имя покупателя')
    buyer_phone = models.CharField(max_length=50, verbose_name='Номер телефона')
    address = models.CharField(max_length=200, verbose_name="Адрес доставки")

    def __str__(self):
        return f"№{self.id} - {self.item_id} ({self.quantity})"


class Referral(TimedBaseModel):
    class Meta:
        verbose_name = "Реферал"
        verbose_name_plural = "Рефералы"

    id = models.ForeignKey(User, unique=True, primary_key=True, on_delete=models.CASCADE)
    referrer_id = models.BigIntegerField()

    def __str__(self):
        return f"№{self.id} - от {self.referrer_id}"
