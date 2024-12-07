from django.contrib import admin

from capital.models import Purchase, Stock

# Register your models here.
admin.site.site_header = 'CELESTIAL ADMINISTRATION'
admin.site.site_title = 'Celestial Admin'


class StockAdmin(admin.ModelAdmin):
    list_display = ['product', 'product_id', 'price']
    search_fields = ['product', 'product_id', 'price']
    list_filter = ['price']
    list_per_page = 10


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['sold_by', 'created_at', 'bought_by', 'amount']
    search_fields = ['sold_by', 'created_at', 'bought_by', 'amount']
    list_per_page = 10
    list_filter = ['created_at']


admin.site.register(Stock, StockAdmin)
admin.site.register(Purchase,PurchaseAdmin)

# python manage.py --help

# python manage.py createsuperuser
# admin@gmail.com
# 123456

# localhost:8000/admin
from django.contrib import admin

# Register your models here.
