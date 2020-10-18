import datetime
import unittest

from tasks.junior.database.connect import config, get_engine


class TestConnectToDatabase(unittest.TestCase):
    def test_check_config(self):

        self.maxDiff = None

        for key, val in config.items():
            self.assertIsNotNone(val)
            self.assertIsNot(val, "")

    def test_check_conn(self):

        self.maxDiff = None
        conn = get_engine()
        res = conn.execute("SELECT CURRENT_TIMESTAMP;").fetchone()
        self.assertIsInstance(res[0], datetime.datetime)
