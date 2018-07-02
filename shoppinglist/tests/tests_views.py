from django.test import TestCase
from django.urls import reverse

from ..models import ItemsList


class ItemsListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_lists = 5
        for list_num in range(number_of_lists):
            ItemsList.objects.create(name='List %s' % list_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'shoppinglist/index.html')

    def test_lists_returns_all_lists(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        print(resp)
        self.assertTrue( len(resp.context['lists']) == 5)
