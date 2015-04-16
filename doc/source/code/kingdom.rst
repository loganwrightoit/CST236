Kingdom Example
===============

Kingdom provides functions related to threats, including orcs.

Adding a Threat
^^^^^^^^^^^^^^^

The function :func:`source.kingdom.addThreat` provides users with a way to add new threats to the kingdom.  Allowable classes are those extending the :func:`source.threat.Threat` abstract class, such as :func:`source.orc.OrcWhite`.

Add Threat Example
^^^^^^^^^^^^^^^^^^

.. testsetup:: threatex

    import source.kingdom
    from source.orc import OrcWhite
    kingdom = source.kingdom.Kingdom()

.. testcode:: threatex

    kingdom.addThreat(OrcWhite())
    threats = kingdom.getThreats()
    print threats[0].threatType

.. testoutput:: threatex

    WhiteOrc


Removing a Threat by UUID
^^^^^^^^^^^^^^^^^^^^^^^^^

The function :func:`source.kingdom.removeThreat` provides users with a way to remove existing threats from a kingdom by specifying a unique threat id.

Remove Threat Example
^^^^^^^^^^^^^^^^^^^^^

.. testsetup:: rthreatex

    import source.kingdom
    from source.orc import OrcWhite
    kingdom = source.kingdom.Kingdom()

.. testcode:: rthreatex

    threat = OrcWhite()
    kingdom.addThreat(threat)
    kingdom.removeThreat(threat.uuid)
    threats = kingdom.getThreats()
    print threats

.. testoutput:: rthreatex

    []


Module Reference
^^^^^^^^^^^^^^^^

.. automodule:: source.kingdom
    :members:

.. automodule:: source.orc
    :members:

.. automodule:: source.threat
    :members: