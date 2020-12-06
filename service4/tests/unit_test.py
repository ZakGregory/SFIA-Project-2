from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestService2(TestBase):
    def test_attack(self):
        response = self.client.post(url_for('post_attack'),data="1,1")
        output =  response.data.decode('utf-8')
        self.assertEqual(output, "hit")
