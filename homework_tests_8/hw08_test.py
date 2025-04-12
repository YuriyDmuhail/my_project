import unittest
from hw07.homework_07 import  make_summ, average_num, list_with_str, counting_unique


class MakerSumTest(unittest.TestCase):
    """
    Тестуємо функцію make_summ
    """
    def test_if_equal(self):
        self.assertEqual(make_summ(2,3), 5)
    def test_if_not_equal(self):
        self.assertNotEqual(make_summ(2,3), 6)
    def test_if_type_error(self):
        self.assertRaises(TypeError, make_summ, "2", 3)
    def test_with_float_only(self):
        self.assertEqual(make_summ(2.5, 3.5), 6)
    def test_with_float_second(self):
        self.assertEqual(make_summ(2.05, 3.04), 5.09)

class AverageNumTest(unittest.TestCase):
    """
    Тестуємо функцію average_num - середнє значення
    """
    def test_if_equal(self):
        self.assertEqual(average_num(2,3), 2.5)
    def test_with_float(self):
        self.assertEqual(average_num(2.5, 3.5, 4, 4.05), 3.5125)
    def test_if_type_error(self):
        self.assertRaises(TypeError, average_num, "2", 3)
class ListWithStrTest(unittest.TestCase):
    """
    Тестуємо функцію яка фільтрує список і повертає значення з типом str
    """
    def test_if_equal(self):
        self.assertEqual(list_with_str([1, "2", "3"]), ["2", "3"])
        self.assertEqual(list_with_str([True, "2", "3"]), ["2", "3"])
        self.assertEqual(list_with_str([None, "2", "3"]), ["2", "3"])
        self.assertEqual(list_with_str(["", "2", "3"]), ["", "2", "3"])

class CountingUniqueTest(unittest.TestCase):
    def test_if_equal(self):
        self.assertEqual(counting_unique([1, 2, 3, 4, 5, 6 , 7, 8, 9, 10, 11]), True)
        self.assertEqual(counting_unique(["h", "h", "h", "h", "h", "h", "h"]), False)
