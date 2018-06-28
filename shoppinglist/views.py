from django.shortcuts import render, get_object_or_404, redirect

from .forms import ItemsListForm
from .models import ItemsList, Item


def index(request):
    lists = ItemsList.objects.all()
    return render(request, 'shoppinglist/index.html', {'lists': lists})


def get_items_list(request, id):
    items_list = get_object_or_404(ItemsList, pk=id)
    items = items_list.item_set.all().order_by('is_bought', 'name')
    return render(request, 'shoppinglist/items_list.html', {'list': items_list, 'items': items})


def get_item(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, 'shoppinglist/item.html', {'item': item})


def add_items_list(request):
    if request.method == "POST":
        form = ItemsListForm(request.POST)
        if form.is_valid():
            items_list = form.save()
            return redirect('items_list', id=items_list.id)
        else:
            return render(request, 'shoppinglist/add_items_list.html',  {'form': form})
    else:
        form = ItemsListForm()
        return render(request, 'shoppinglist/add_items_list.html', {'form': form})


def edit_items_list(request, id):
    items_list = get_object_or_404(ItemsList, pk=id)
    if request.method == "POST":
        form = ItemsListForm(request.POST, instance=items_list)
        if form.is_valid():
            form.save()
            return redirect('items_list', id=id)
        else:
            return render(request, 'shoppinglist/edit_items_list.html',  {'form': form})
    else:
        form = ItemsListForm(instance=items_list)
        return render(request, 'shoppinglist/edit_items_list.html', {'form': form})


def delete_items_list(request, id):
    items_list = get_object_or_404(ItemsList, pk=id)
    items_list.delete()
    return redirect('index')
