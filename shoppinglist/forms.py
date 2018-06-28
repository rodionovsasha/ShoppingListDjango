from django import forms

from .models import ItemsList, Item


class ItemsListForm(forms.ModelForm):
    class Meta:
        model = ItemsList
        fields = ('name',)


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'comment',)
