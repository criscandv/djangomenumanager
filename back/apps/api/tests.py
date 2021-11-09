from djongo import models

from django.test import TransactionTestCase, Client, TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import QueryDict

from rest_framework import status
from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient

from apps.api.models import Menu
from apps.api.viewsets import MenuViewSet


MENU_TEST_DATA = {
    "name": "Menu test data",
    "price": 15
}

class MenuTestCase(TransactionTestCase):
    data_user = {
        "username": "usertest",
        "email": "user@tests.com",
        "password": "thepassis1"
    }

    def setUp(self):
        self.factory = APIRequestFactory()
        self.test_client = Client()

        try:
            self.user = User.objects.get(username=self.data_user["username"])
        except ObjectDoesNotExist:
            self.user = User.objects.create_user(
                username=self.data_user["username"], email=self.data_user["email"], password=self.data_user["password"]
            )

    def tearDown(self):
        pass

    def create_request(self, data={}, **kwargs ):
        auth = False if '__auth' in kwargs and kwargs['__auth'] == False else True
        formatt = 'json' if not '__format' in kwargs else kwargs['__format']
        user = self.user if not '__user' in kwargs else kwargs['__user']
        method_test = kwargs['_method_test_'] if '_method_test_' in kwargs else self.method_test if hasattr(self, 'method_test') else None

        if not method_test:
            self.assertEqual(True, False, 'Method test is not assigned')

        if not hasattr(self, 'url_test_request'):
            self.assertEqual(True, False, 'Url is not assigned')

        request = self.method_test(self.url_test_request, data=data, format=formatt)
        if auth:
            force_authenticate(request, user=user)
            setattr(request, 'user', user)

        return request

    def complete_response_request(self, data={}, pk=None, **kwargs):
        view = kwargs['_view_'] if '_view_' in kwargs else self.view if hasattr(self, 'view') else None
        if not view:
            self.assertEqual(True, False, 'View is not assigned')

        request = self.create_request(data, **kwargs)

        if pk:
            return view(request, pk=pk)

        return view(request)

    def create_menu(self):
        try:
            menu = Menu.objects.get(name=MENU_TEST_DATA['name'])
        except ObjectDoesNotExist:
            menu = Menu()
            menu.name = MENU_TEST_DATA['name']
            menu.price = MENU_TEST_DATA['price']
            menu.save()

        self.menu = menu

    def validate_authentication(self):
        request = self.create_request(data={}, __auth=False)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, response.data)

    def test_list(self):
        self.create_menu()

        self.method_test = self.factory.get
        self.url_test_request = '/api/menus/'
        self.view = MenuViewSet.as_view({'get': 'list'})
        data = {}

        # Validate authentication
        self.validate_authentication()

        # Validate Gett all data
        response = self.complete_response_request(data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(len(response.data), 1)

    def test_retrieve(self):
        self.create_menu()

        self.method_test = self.factory.get
        self.url_test_request = '/api/menus/'
        self.view = MenuViewSet.as_view({'get': 'retrieve'})
        data = {}

        # Validate authentication
        self.validate_authentication()

        # Pk is not present
        response = self.complete_response_request(data=data, pk=None)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.data)

        # Validate item not found
        response = self.complete_response_request(data=data, pk=123456)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND, response.data)

        # Validate retrieve item data
        response = self.complete_response_request(data=data, pk=self.menu.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(response.data['data']['name'], self.menu.name, response.data)

    def test_create(self):
        self.method_test = self.factory.post
        self.url_test_request = '/api/menus/'
        self.view = MenuViewSet.as_view({'post': 'create'})
        data = {
            "name": "Menu test data 2",
            "price": 15
        }

        response = self.complete_response_request(data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)

    def test_update(self):
        self.create_menu()

        self.method_test = self.factory.put
        self.url_test_request = '/api/menus/'
        self.view = MenuViewSet.as_view({'put': 'update'})
        data = {
            "name": "Menu test data Actualizado",
            "price": 30
        }

        # Validate authentication
        self.validate_authentication()

        # Pk is not present
        response = self.complete_response_request(data=data, pk=None)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.data)

        # Validate item not found
        response = self.complete_response_request(data=data, pk=123456)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND, response.data)

        # Validate update data
        response = self.complete_response_request(data=data, pk=self.menu.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_destroy(self):
        self.create_menu()

        self.method_test = self.factory.delete
        self.url_test_request = '/api/menus/'
        self.view = MenuViewSet.as_view({'delete': 'destroy'})
        data = {}

        # Validate authentication
        self.validate_authentication()

        # Pk is not present
        response = self.complete_response_request(data=data, pk=None)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.data)

        # Validate item not found
        response = self.complete_response_request(data=data, pk=123456)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND, response.data)

        # Validate delete data
        response = self.complete_response_request(data=data, pk=self.menu.id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, response.data)