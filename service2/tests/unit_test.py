from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestService2(TestBase):
    def test_integer(self):
        response = self.client.get('/get_integer')
        integer = response.data.decode('utf-8').isnumeric()
        self.assertFalse(integer)

