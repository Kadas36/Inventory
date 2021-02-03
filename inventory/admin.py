from django.contrib import admin
from .models import Stock
from .forms import StockForm

# Register your models here.

class StockAdmin(admin.ModelAdmin):
   list_display = ['category', 'product_name', 'quantity']
   form = StockForm
   list_filter = ['category']
   search_fields = ['category', 'item_name']

admin.site.register(Stock, StockAdmin)   
