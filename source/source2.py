"""
:mod:`source.source2` -- Example source code
============================================

The following example code determines if a set of 4 sides is square or rectangular
"""

def get_rect_type(a=0, b=0, c=0, d=0):
    """
    Determine if the given object is a square or rectange

    :param a: line a
    :type a: float or int or tuple or list or dict

    :param b: line b
    :type b: float

    :param c: line c
    :type c: float

    :param d: line d
    :type d: float

    :return: "square", "rectangle", "invalid"
    :rtype: str
    """
    if isinstance(a, (tuple, list)) and len(a) == 4:
        d = a[3]
        c = a[2]
        b = a[1]
        a = a[0]

    if isinstance(a, dict) and len(a.keys()) == 4:
        values = []
        for value in a.values():
            values.append(value)
        a = values[0]
        b = values[1]
        c = values[2]
        d = values[3]

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)) and isinstance(d, (int, float))):
        return "invalid"

    if a <= 0 or b <= 0 or c <= 0 or d <= 0:
        return "invalid"

    if a == b and b == c and c == d:
        return "square"
    elif a == b and c == d or a == c and b == d or a == d and b == c:
        return "rectangle"
    else:
        return "invalid"
