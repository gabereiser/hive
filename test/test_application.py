from unittest import TestCase
from flask import Response
from .mixins.test_case import TestCaseMixin


class HiveApplicationTest(TestCaseMixin, TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_application_index(self):
        client = self.create_app().test_client()
        response: Response = client.get('/')
        self.assertFalse(response.is_json)
        self.assertEqual(response.status_code, 302)
        self.assertIsNotNone(response.response)

        data = {'username': 'admin', 'password': 'admin'}
        response = client.post('/login', data=data, follow_redirects=True)
        self.assertFalse(response.is_json)
        self.assertEqual(response.status_code, 200)
        body = ascii(str(response.data))
        self.assertNotIn('Invalid username', body)

        response = client.get('/', follow_redirects=True)
        self.assertFalse(response.is_json)
        self.assertEqual(response.status_code, 200)

    def test_application_status(self):
        app = self.create_app()
        client = self.create_app().test_client()
        status: Response = client.get('/api/status')
        self.assertTrue(status.is_json)
        self.assertEqual(status.json.get('status'), 'ok')
        self.assertEqual(status.status_code, 200)
