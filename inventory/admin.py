from django.contrib import admin
from .models import Stock, Category
from .forms import StockForm
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.

# class StockAdmin(admin.ModelAdmin):

class StockAdmin(SimpleHistoryAdmin):
   list_display = ['category', 'product_name', 'quantity']
   history_list_display = ["status"]
   form = StockForm
   list_filter = ['category']
   search_fields = ['category', 'item_name']

admin.site.register(Stock, StockAdmin)   
admin.site.register(Category) 
