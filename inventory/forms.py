from django import forms
from .models import Stock

class StockForm(forms.ModelForm):
  class Meta:
    model = Stock
    fields = ['category', 'product_name', 'quantity']

  def clean_category(self):
    category = self.cleaned_data.get('category')
    if not category:
      raise forms.ValidationError('This field is required')
    for instance in Stock.objects.all():
      if instance.category == category:
        raise forms.ValidationError(str(category) + ' is already created')
    return category

  def clean_item_name(self):
    product_name = self.cleaned_data.get('product_name')
    if not product_name:
      raise forms.ValidationError('This field is required')
    return product_name


class StockSearchForm(forms.ModelForm):
   class Meta:
     model = Stock
     fields = ['category', 'product_name'] 

class StockUpdateForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['category', 'product_name', 'quantity']         