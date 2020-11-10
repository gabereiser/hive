from unittest import TestCase


class HiveTest(TestCase):

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

    def test_test_availability(self):
        available = True
        self.assertTrue(available)
