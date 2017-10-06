from unittest import TestCase
from app import app
import json


class ApiTests(TestCase):
    def setUp(self):
        self.test_app = app.test_client()

    def tearDown(self):
        pass

    def test_api_responds_json(self):
        """Test that query to /someapi returns some json"""
        res = self.test_app.get('/someapi')
        self.assertEqual(res.status_code, 200)
        try:
            json.loads(res.data)
        except Exception as e:
            self.fail("Failed parsing the retured json: "+str(e))
