Input Example
==============

Input provides functions designed to process user input in the absense of an input mechanism, such as during automated testing.

Process Input
^^^^^^^^^^^^^^^^

The function :func:`source.input.process` provides testers with a way to provide user commands to control the program.

Process Example
^^^^^^^^^^^^^^^^^^

>>> import source.input
>>> source.input.Input().process("?")
'Some options'



Module Reference
^^^^^^^^^^^^^^^^

.. automodule:: source.input
    :members: