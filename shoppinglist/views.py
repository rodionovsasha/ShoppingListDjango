from django.shortcuts import render, get_object_or_404, redirect

from .forms import ItemsListForm
from .models import ItemsList, Item


def index(request):
    lists = ItemsList.objects.all()
    return render(request, 'shoppinglist/index.html', {'lists': lists})


def get_items_list(request, id):
    list_of_items = get_object_or_404(ItemsList, pk=id)
    items = list_of_items.item_set.all().order_by('is_bought', 'name')
    return render(request, 'shoppinglist/items_list.html', {'list': list_of_items, 'items': items})


def get_item(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, 'shoppinglist/item.html', {'item': item})


def add_items_list(request):
    if request.method == "POST":
        form = ItemsListForm(request.POST)
        if form.is_valid():
            list_of_items = form.save()
            return redirect('items_list', id=list_of_items.id)
        else:
            return render(request, 'shoppinglist/add_items_list.html',  {'form': form})
    else:
        form = ItemsListForm()
        return render(request, 'shoppinglist/add_items_list.html', {'form': form})
