Threat Example
==============

Threat holds properties for describing a threat that is most commonly used by a Kingdom object (:func:`source.kingdom.Kingdom`).

.. note::
    Properties include distance, velocity, and priority.

Determining Distance
^^^^^^^^^^^^^^^^^^^^

The property :py:attr:`source.threat.distance` indicates the distance of the threat.

Distance Example
^^^^^^^^^^^^^^^

>>> import source.threat
>>> import source.orc
>>> orc = source.orc.OrcWhite()
>>> orc.distance = 5
>>> print orc.distance
5


Determining Velocity
^^^^^^^^^^^^^^^^^^^^

The property :py:attr:`source.threat.velocity` indicates the movement velocity of the threat.

Velocity Example
^^^^^^^^^^^^^^^^

>>> import source.threat
>>> import source.orc
>>> orc = source.orc.OrcWhite()
>>> orc.velocity = 3
>>> print orc.velocity
3


Determining Priority
^^^^^^^^^^^^^^^^^^^^

The property :py:attr:`source.threat.priority` can be used to prioritize the threat.

Priority Example
^^^^^^^^^^^^^^^^

>>> import source.threat
>>> import source.orc
>>> orc = source.orc.OrcWhite()
>>> orc.priority = 7
>>> print orc.priority
7


Module Reference
^^^^^^^^^^^^^^^^

.. automodule:: source.threat
    :members:

.. automodule:: source.orc
    :members: