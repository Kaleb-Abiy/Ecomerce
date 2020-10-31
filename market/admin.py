from django.contrib import admin
from .models import *

class ShipingList(admin.ModelAdmin):
    list_display=('order', 'city', 'customer')
    search_fields = ('city', 'order__transaction_id')

class ItemList(admin.ModelAdmin):
    list_display=('product', 'order') 
    search_fields=('order',)   

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Item, ItemList)
admin.site.register(ShipingAdress, ShipingList)
