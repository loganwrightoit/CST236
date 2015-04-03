Source2 Example
===============

Source2 provides functions for describing a rectangle.

Determining Rectangle Type
^^^^^^^^^^^^^^^^^^^^^^^^^^

The function :func:`source.source2.get_rect_type` provides users with a way to provide a set of four sides
of a rectangle and returns the type of rectangle ("square", "rectangle" or "invalid")

Square Example
^^^^^^^^^^^^^^

>>> from source.source2 import get_rect_type
>>> get_rect_type(2, 2, 2, 2)
'square'

Simple DocTest Example
^^^^^^^^^^^^^^^^^^^^^^

This is a simple doctest.

>>> a = 1
>>> b = 1
>>> c = 1
>>> d = 1
>>> str = get_rect_type(a, b, c, d)
>>> print str
square

Complex DocTest Example
^^^^^^^^^^^^^^^^^^^^^^^

This is a complex doctest.

.. testsetup:: *

    from source.source2 import get_rect_type
    a = 1
    b = 2
    c = 2
    d = 1

.. testcode:: get_rect_type

    str = get_rect_type(a, b, c, d)
    print str

.. testoutput:: get_rect_type

    rectangle

Module Reference
^^^^^^^^^^^^^^^^

.. automodule:: source.source2
    :members: