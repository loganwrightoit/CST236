"""
Test for source.source1
"""
from source.source1 import get_triangle_type
from unittest import TestCase

class TestGetTriangleType(TestCase):

    def test_get_triangle_equilateral_all_int(self):
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_isosceles_all_int(self):
        result = get_triangle_type(1, 1, 3)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_scalene_all_int(self):
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')

    """
    Test invalid case where argument is '<= 0'
    """

    def test_get_triangle_invalid_arg1_zero(self):
        result = get_triangle_type(0, 2, 3)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_invalid_arg2_zero(self):
        result = get_triangle_type(1, 0, 3)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_invalid_arg3_zero(self):
        result = get_triangle_type(1, 2, 0)
        self.assertEqual(result, 'invalid')

    """
    Test invalid case where argument is unsupported
    """

    def test_get_triangle_invalid_arg1_char(self):
        result = get_triangle_type('a', 2, 3)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_invalid_arg2_char(self):
        result = get_triangle_type(1, 'a', 3)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_invalid_arg3_char(self):
        result = get_triangle_type(1, 2, 'a')
        self.assertEqual(result, 'invalid')

    """
    Test 'a' as list argument
    """

    def test_get_triangle_arg1_list(self):
        result = get_triangle_type([ 1, 2, 3 ])
        self.assertEqual(result, 'scalene')

    """
    Test 'a' as dict argument
    """

    def test_get_triangle_arg1_dict(self):
        result = get_triangle_type({ 'a': 1, 'b': 2, 'c': 3 })
        self.assertEqual(result, 'scalene')
