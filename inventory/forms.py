from django import forms
from .models import Stock,Category

class StockForm(forms.ModelForm):
  class Meta:
    model = Stock
    fields = ['category', 'product_name', 'quantity']

  # def clean_category(self):
  #   category = self.cleaned_data.get('category')
  #   if not category:
  #     raise forms.ValidationError('This field is required')
  #   for instance in Stock.objects.all():
  #     if instance.category == category:
  #       raise forms.ValidationError(str(category) + ' is already created')
  #   return category

  # def clean_item_name(self):
  #   product_name = self.cleaned_data.get('product_name')
  #   if not product_name:
  #     raise forms.ValidationError('This field is required')
  #   return product_name

  def clean_item_name(self):
    product_name = self.cleaned_data.get('product_name')
    if not product_name:
      raise forms.ValidationError('This field is required')
    for instance in Stock.objects.all():
      if instance.product_name == product_name:
        raise forms.ValidationError(str(product_name) + ' is already created')
    return product_name

class CategoryCreateForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['name']

class StockSearchForm(forms.ModelForm):
   class Meta:
     model = Stock
     fields = ['product_name'] 

class StockUpdateForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['category', 'product_name', 'quantity']  

class IssueForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['issued_quantity', 'issue_to']


class ReceiveForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['received_quantity', 'receipient']     

class ReorderLevelForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['alert_amount']          