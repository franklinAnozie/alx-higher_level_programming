#!/usr/bin/python3
from unittest import TestCase
max_integer = __import__('6-max_integer').max_integer

class max_integer_test(TestCase):
    def test_max(self):
        self.assertEqual(max_integer([2, 8, 3, 6]), 8)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([24]), 24)
        self.assertEqual(max_integer(["a", "b", "c", "k"]), "k")
        self.assertEqual(max_integer([[], [[]], [[[]]]]), [[[]]])
        self.assertEqual(max_integer([(), (()), ((()))]), ((())))
    
    def test_values(self):
        self.assertRaises(TypeError, max_integer, [7, "a", 0])
        self.assertRaises(TypeError, max_integer, [7, [], "r"])
        self.assertRaises(TypeError, max_integer, [[], {}, ()])
