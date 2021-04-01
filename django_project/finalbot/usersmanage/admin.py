from django.contrib import admin

from .models import Item, Purchase, User, Referral


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'coins', 'created_at')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'label', 'price', 'quantity', 'description')


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'item_id', 'quantity', 'amount', 'purchase_time', 'buyer_name', 'buyer_phone')


@admin.register(Referral)
class RefAdmin(admin.ModelAdmin):
    list_display = ('id', 'referrer_id')
