from django.shortcuts import render, get_object_or_404

from .models import ItemsList


def index(request):
    lists = ItemsList.objects.all()
    return render(request, 'shoppinglist/index.html', {'lists': lists})


def items_list(request, id):
    list_of_items = get_object_or_404(ItemsList, pk=id)
    items = list_of_items.item_set.all().order_by('is_bought', 'name')
    return render(request, 'shoppinglist/items_list.html', {'list': list_of_items, 'items': items})
