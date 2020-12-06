from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_home(self):
        with patch("requests.get") as g:
            with patch("requests.post") as p:
                g.return_value.text = "1"
                p.return_value.text = "hit"

                response = self.client.get(url_for("home"))
                self.assertIn(b'1', response.data)
                self.assertIn(b'hit', response.data)
