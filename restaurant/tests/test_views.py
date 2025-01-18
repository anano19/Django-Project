from rest_framework.test import APITestCase
from django.urls import reverse
from ..models import MenuItem
from rest_framework.test import APIClient

class MenuViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_item1 = MenuItem.objects.create(name="Ice Cream", description="Delicious vanilla ice cream", price=2.50, available=True)
        self.menu_item2 = MenuItem.objects.create(name="Pasta", description="Creamy Alfredo pasta", price=12.99, available=True)

    def test_get_all_menu_items(self):
        response = self.client.get(reverse('menu-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], self.menu_item1.name)
        self.assertEqual(response.data[1]['name'], self.menu_item2.name)