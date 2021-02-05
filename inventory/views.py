 
from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm, StockSearchForm, StockUpdateForm, IssueForm, ReceiveForm, ReorderLevelForm,CategoryCreateForm
from django.contrib import messages
from simple_history.utils import update_change_reason
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login/')
def add_items(request):
	form = StockForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Successfully Saved')
		return redirect('/')

	context = {
		"form":form,
		"title":"Add Item"
	}    
	return render(request, 'store/add_item.html', context)

@login_required(login_url='/accounts/login/')
def add_category(request):
	form = CategoryCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Successfully Created')
		return redirect('/')
	context = {
		"form": form,
		"title":"Add Category"
	}
	return render(request, "store/add_item.html", context)

@login_required(login_url='/accounts/login/')
def list_item(request):
    title = 'List of Items'
    form = StockSearchForm(request.POST or None)

    queryset = Stock.objects.all()

    if request.method == 'POST':
        queryset = Stock.objects.filter(
                                    product_name__icontains=form['product_name'].value()
                                    )
    context = {
        "form": form,
        "header": title,
        "queryset": queryset,
    }
    return render(request, "store/list_item.html", context)  

@login_required(login_url='/accounts/login/')
def update_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = StockUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = StockUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Saved')
            return redirect('/')

    context = {
        'form':form,
		"title":"Update Item"
    }
    return render(request, 'store/add_item.html', context) 

@login_required(login_url='/accounts/login/')
def delete_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Item deleted')
        return redirect('/')
    return render(request, 'store/delete_items.html')    

def stock_detail(request, pk):
	queryset = Stock.objects.get(id=pk)
	context = {
		"queryset": queryset,
		"title":"Delete Item"
	}
	return render(request, "store/stock_detail.html", context)  

@login_required(login_url='/accounts/login/')
def issue_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = IssueForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.quantity -= instance.issued_quantity
		instance.issue_by = str(request.user)
		messages.success(request, "Issued SUCCESSFULLY. " + str(instance.quantity) + " " + str(instance.product_name) + "s now left in Store")
		instance.save()

		return redirect('/stock_detail/'+str(instance.id))
		
	context = {
		"title": 'Issue ' + str(queryset.product_name),
		"queryset": queryset,
		"form": form,
		"username": 'Issue By: ' + str(request.user),
	}
	return render(request, "store/add_item.html", context)


@login_required(login_url='/accounts/login/')
def receive_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = ReceiveForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.quantity += instance.received_quantity
		instance.save()
		messages.success(request, "Received SUCCESSFULLY. " + str(instance.quantity) + " " + str(instance.product_name)+"s now in Store")

		return redirect('/stock_detail/'+str(instance.id))
		
	context = {
			"title": 'Receive ' + str(queryset.product_name),
			"instance": queryset,
			"form": form,
			"username": 'Receive By: ' + str(request.user),
		}
	return render(request, "store/add_item.html", context)

@login_required(login_url='/accounts/login/')
def reorder_level(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = ReorderLevelForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Reorder level for " + str(instance.product_name) + " is updated to " + str(instance.alert_amount))

		return redirect("/")
	context = {
			"instance": queryset,
			"form": form,
		}
	return render(request, "store/add_item.html", context)    

@login_required(login_url='/accounts/login/')
def list_history(request):
	queryset = Stock.history.all()

	form = StockSearchForm(request.POST or None)
	if request.method == 'POST':
		queryset = Stock.history.filter(
								product_name__icontains=form['product_name'].value()
								)
		
	context = {
		'historyset': queryset,
		'form': form
	}
	return render(request, 'store/history.html', context)