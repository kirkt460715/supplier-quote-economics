"""核对交接文件中的来源依据。"""
import unittest
from inspect_delivery import read_table


class DeliveryTest(unittest.TestCase):
    def test_linked_records(self):
        data = {r["quote"]: r for r in read_table("quotes.json")}
        self.assertTrue(all(r["quote"] in data for r in read_table("committed.json")))
        self.assertEqual(data["QA"]["window"], data["QB"]["window"])
        self.assertNotEqual(data["QA"]["process"], data["QB"]["process"])
        self.assertTrue(any(r["accepted"] is None for r in read_table("samples.json")))
