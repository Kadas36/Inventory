from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm, StockSearchForm, StockUpdateForm

# Create your views here.

def store_home(request):
    return render(request, 'store/home.html')

def add_items(request):
    form = StockForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/list_item/')

    context = {
        "form":form,
        "title":"Add Item"
    }    
    return render(request, 'store/add_item.html', context)

def list_item(request):
    title = 'List of Items'
    form = StockSearchForm(request.POST or None)

    queryset = Stock.objects.all()

    if request.method == 'POST':
        queryset = Stock.objects.filter(category__icontains=form['category'].value(),
                                    product_name__icontains=form['product_name'].value()
                                    )
    context = {
        "form": form,
        "header": title,
        "queryset": queryset,
    }
    return render(request, "store/list_item.html", context)  

def update_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = StockUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = StockUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('/list_item/')

	context = {
		'form':form
	}
	return render(request, 'store/add_item.html', context) 

def delete_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('/list_item/')
	return render(request, 'store/delete_items.html')       


