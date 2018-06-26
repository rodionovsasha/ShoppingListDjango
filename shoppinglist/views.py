from django.shortcuts import render

from .models import ItemsList


def index(request):
    lists = ItemsList.objects.all()
    return render(request, 'shoppinglist/index.html', {'lists': lists})
