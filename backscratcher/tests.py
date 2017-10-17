import json
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from .models import Backscratcher
from .serializers import BackscratcherSerializer


class GetAllBackscratchersTest(TestCase):
    """ Test module for GET all puppies API """

    def setUp(self):
        self.user = User.objects.create_user('foo', 'foo@bar.de', 'bar')
        Token.objects.create(user=self.user)
        self.token = Token.objects.get(user=self.user).key
        self.c = Client()
        self.test1 = Backscratcher.objects.create(
            item_name='Test1',
            item_description='TestDes1',
            item_size=['M'],
            item_price=100.00
        )
        self.test2 = Backscratcher.objects.create(
            item_name='Test2',
            item_description='TestDes2',
            item_size=['M', 'L'],
            item_price=100.00
        )
        self.valid_payload = {
            'item_name': 'Test3',
            'item_description': 'TestDesc3',
            'item_size': ['M', 'L'],
            'item_price': 100
        }

    def test_get_all_backscratchers(self):
        header = {'HTTP_AUTHORIZATION': 'Token {}'.format(self.token)}
        response = self.c.get(
            reverse(
                'get_post_backscratchers'),
                {},
                **header
            )
        backscratchers = Backscratcher.objects.all()
        serializer = BackscratcherSerializer(backscratchers, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_backscratcher(self):
        header = {'HTTP_AUTHORIZATION': 'Token {}'.format(self.token)}
        response = self.c.get(
            reverse(
                'get_delete_update_backscratchers',
                kwargs={'pk': self.test1.pk}
            ), {}, **header)
        backscratcher = Backscratcher.objects.get(pk=self.test1.pk)
        serializer = BackscratcherSerializer(backscratcher)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_backscratcher(self):
        header = {'HTTP_AUTHORIZATION': 'Token {}'.format(self.token)}
        response = self.c.get(
            reverse(
                'get_delete_update_backscratchers',
                kwargs={'pk': 100}
            ), {}, **header)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
