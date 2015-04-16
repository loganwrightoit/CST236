Kingdom Example
==============

Kingdom provides functions related to threats, including orcs.

Adding a Threat
^^^^^^^^^^^^^^^

The function :func:`source.kingdom.addThreat` provides users with a way to add new threats to the kingdom.  Allowable classes are those extending the :func:`source.threat.Threat` abstract class, such as :func:`source.orc.OrcWhite`.

Add Threat Example
^^^^^^^^^^^^^^^^^^^^^^^^

.. testsetup:: *

    from source.kingdom import addThreat
    from source.orc import OrcWhite
    kingdom = Kingdom()

.. testcode:: add

    kingdom.addThreat(OrcWhite())
    threats = kingdom.getThreats()
    print threats[0].threatType

.. testoutput:: add

    "OrcWhite"


Module Reference
^^^^^^^^^^^^^^^^

.. automodule:: source.kingdom
    :members:

.. automodule:: source.orc
    :members:

.. automodule:: source.threat
    :members: