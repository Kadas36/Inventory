from django.db import models
from simple_history.models import HistoricalRecords
from simple_history import register
from django.contrib.auth.models import User

register(User)

# Create your models here.

category_choice = (
		('Furniture', 'Furniture'),
		('Phone', 'Phone'),
	)

class Category(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	def __str__(self):
		return self.name   	

class Stock(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    received_quantity = models.IntegerField(default=0, blank=True, null=True)
    receipient = models.CharField(max_length=50, blank=True, null=True)
    issued_quantity = models.IntegerField(default=0, blank=True, null=True)
    issue_by = models.CharField(max_length=50, blank=True, null=True)
    issue_to = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    alert_amount = models.IntegerField(default=0,blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    history = HistoricalRecords(excluded_fields=[
                                                'alert_amount',
                                                'date'])

    def __str__(self):
        return self.product_name

      

     
