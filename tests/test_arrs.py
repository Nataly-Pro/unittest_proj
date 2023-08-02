import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([1, 2, 3], -2, "test"), "test")

    def test_index_out_of_range(self):
        with self.assertRaises(IndexError):
            arrs.get([], 0, "test")


    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])

    def test_slice_empty_coll(self):
        self.assertEqual(arrs.my_slice([]), [])

    def test_negative_start(self):
        self.assertEqual(arrs.my_slice([1, 2, 3], -10), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], -2), [2, 3])
