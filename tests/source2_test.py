"""
Test for source.source2
"""
from source.source2 import get_rect_type
from unittest import TestCase

class TestGetRectType(TestCase):

    def test_get_rect_square_all_int(self):
        result = get_rect_type(1, 1, 1, 1)
        self.assertEqual(result, 'square')

    def test_get_rect_rectangle_order1_int(self):
        result = get_rect_type(1, 1, 2, 2)
        self.assertEqual(result, 'rectangle')

    def test_get_rect_rectangle_order2_int(self):
        result = get_rect_type(1, 2, 1, 2)
        self.assertEqual(result, 'rectangle')

    def test_get_rect_rectangle_order3_int(self):
        result = get_rect_type(1, 2, 2, 1)
        self.assertEqual(result, 'rectangle')

    """
    Test invalid case where argument is '<= 0'
    """

    def test_get_rect_invalid_arg1_zero(self):
        result = get_rect_type(0, 2, 3)
        self.assertEqual(result, 'invalid')

    def test_get_rect_invalid_arg2_zero(self):
        result = get_rect_type(1, 0, 3)
        self.assertEqual(result, 'invalid')

    def test_get_rect_invalid_arg3_zero(self):
        result = get_rect_type(1, 2, 0)
        self.assertEqual(result, 'invalid')

    def test_get_rect_invalid_arg4_zero(self):
        result = get_rect_type(1, 2, 0)
        self.assertEqual(result, 'invalid')

    """
    Test invalid case where argument is unsupported
    """

    def test_get_rect_invalid_arg1_char(self):
        result = get_rect_type('a', 1, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_rect_invalid_arg2_char(self):
        result = get_rect_type(1, 'a', 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_rect_invalid_arg3_char(self):
        result = get_rect_type(1, 1, 'a', 1)
        self.assertEqual(result, 'invalid')

    def test_get_rect_invalid_arg3_char(self):
        result = get_rect_type(1, 1, 1, 'a')
        self.assertEqual(result, 'invalid')

    """
    Test invalid case where arguments aren't valid pairs
    """

    def test_get_rect_invalid_pair1_char(self):
        result = get_rect_type(2, 1, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_rect_invalid_pair2_char(self):
        result = get_rect_type(1, 2, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_rect_invalid_pair3_char(self):
        result = get_rect_type(1, 1, 2, 1)
        self.assertEqual(result, 'invalid')
        
    def test_get_rect_invalid_pair4_char(self):
        result = get_rect_type(1, 1, 1, 2)
        self.assertEqual(result, 'invalid')

    """
    Test 'a' as list argument
    """

    def test_get_rect_arg1_list(self):
        result = get_rect_type([ 1, 1, 1, 1 ])
        self.assertEqual(result, 'square')

    """
    Test 'a' as dict argument
    """

    def test_get_rect_arg1_dict(self):
        result = get_rect_type({ 'a': 1, 'b': 1, 'c': 1, 'd': 1 })
        self.assertEqual(result, 'square')
