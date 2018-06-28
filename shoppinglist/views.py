from django.shortcuts import render, get_object_or_404, redirect

from .forms import ItemsListForm, ItemForm
from .models import ItemsList, Item


def index(request):
    lists = ItemsList.objects.all()
    return render(request, 'shoppinglist/index.html', {'lists': lists})


def get_items_list(request, id):
    items_list = get_object_or_404(ItemsList, pk=id)
    items = items_list.item_set.all().order_by('is_bought', 'name')
    return render(request, 'shoppinglist/items_list.html', {'list': items_list, 'items': items})


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


def get_item(request, list_id, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, 'shoppinglist/item.html', {'item': item})


def add_item(request, list_id):
    print(request)
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.items_list = get_object_or_404(ItemsList, pk=list_id)
            item.save()
            return redirect('item', list_id=list_id, id=item.id)
        else:
            return render(request, 'shoppinglist/add_item.html',  {'form': form})
    else:
        form = ItemForm()
        return render(request, 'shoppinglist/add_item.html', {'form': form})


def edit_item(request, list_id, id):
    item = get_object_or_404(Item, pk=id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item', id=id)
        else:
            return render(request, 'shoppinglist/edit_item.html',  {'form': form})
    else:
        form = ItemForm(instance=item)
        return render(request, 'shoppinglist/edit_item.html', {'form': form})


def delete_item(request, list_id, id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    return redirect('items_list', id=list_id)


def buy_item(request, list_id, id):
    item = get_object_or_404(Item, pk=id)
    item.is_bought = not item.is_bought
    item.save()
    return redirect('items_list', id=list_id)
