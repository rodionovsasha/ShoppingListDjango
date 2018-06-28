from django import forms

from .models import ItemsList


class ItemsListForm(forms.ModelForm):
    class Meta:
        model = ItemsList
        fields = ('name',)
