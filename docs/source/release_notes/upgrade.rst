.. _upgrade:

=======
Upgrade
=======

.. warning::
    If you make **any** changes to OpenNebula configuration files under ``/etc/one`` please note the they **will** be discarded and overwritten in the next vOneCloud upgrade, except for those listed in this section.

vOneCloud will feature in the next release an automated upgrade procedure. This procedure will allow users to upgrade the version and update the configuration files. However only a specific set of configuration options will be supported during the upgrade:

* :ref:`LDAP authentication <authentication>`
* :ref:`Hybrid cloud configuration <hybrid_cloud>`
