import unittest


class TestTest(unittest.TestCase):
    def test_test_case(self) -> None:
        self.maxDiff = None
        assert 1 == 1
