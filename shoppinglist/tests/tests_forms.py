from django.test import TestCase

from ..forms import ItemsListForm
from ..models import ItemsList


class ItemsListFormTest(TestCase):

    def test_valid_form(self):
        items_list = ItemsList.objects.create(name='List1')
        data = {'name': items_list.name, }
        form = ItemsListForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        items_list = ItemsList.objects.create(name='')
        data = {'name': items_list.name, }
        form = ItemsListForm(data=data)
        self.assertFalse(form.is_valid())
