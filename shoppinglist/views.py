from django.shortcuts import render, get_object_or_404

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
