from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from .views import ProductViewSet
from django.contrib.auth.models import User
from .models import Product

class ProductTests(APITestCase):
    def setUp(self):
        super().setUp()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.product = Product.objects.create(name="Test Product", description="Test Description", price=10.00, stock=100)

    def test_list_products(self):
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_product_authenticated(self):
        url = reverse('product-list')
        data = {'name': 'New Product', 'description': 'New Description', 'price': 20.00, 'stock': 50}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_product_unauthenticated(self):
        self.client.credentials()
        url = reverse('product-list')
        data = {'name': 'New Product', 'description': 'New Description', 'price': 20.00, 'stock': 50}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class OrderTests(APITestCase):
    def setUp(self):
        super().setUp()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.product = Product.objects.create(name="Test Product", description="Test Description", price=10.00, stock=100)

    def test_create_order_authenticated(self):
        url = reverse('order-list')
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_orders_unauthenticated(self):
        self.client.credentials() 
        url = reverse('order-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class AuthenticationTests(APITestCase):
    def setUp(self):
        super().setUp()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

    def test_access_protected_endpoint_with_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_access_protected_endpoint_without_authentication(self):
        self.client.credentials()
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)