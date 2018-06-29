from django.test import TestCase

from ..models import ItemsList


class ItemsListModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        ItemsList.objects.create(name='List1')

    def test_name_label(self):
        items_list = ItemsList.objects.get(id=1)
        field_label = items_list._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name(self):
        items_list = ItemsList.objects.get(id=1)
        self.assertEquals(items_list.name, 'List1')

    def test_name_max_length(self):
        items_list = ItemsList.objects.get(id=1)
        max_length = items_list._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_str(self):
        items_list = ItemsList.objects.get(id=1)
        self.assertEquals(items_list.__str__(), 'List1')
