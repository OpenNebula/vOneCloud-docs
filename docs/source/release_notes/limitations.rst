.. _limitations:

=====================
vOneCloud Limitations
=====================

.. todo::

   Re-evaluate limitations

vOneCloud will use pre defined Templates existing in the vCenter to launch Virtual Machines. The following limitations apply:

+--------------------------------------+-------------------------------------------------------------------------------------------+
| **No Automatic Guest Configuration** | :ref:`Contextualization <build_template_context>` mechanism in vOneCloud does not provide |
|                                      |              packages to automatically configure guest OS (Linux or Windows)              |
+--------------------------------------+-------------------------------------------------------------------------------------------+
| **VM Unsupported Operations**        | The following operations are only supported from vCenter:                                 |
|                                      | - Attach/detach disk to a running VM                                                      |
|                                      | - Migrate VM to different ESX clusters                                                    |
+--------------------------------------+-------------------------------------------------------------------------------------------+
| **No MultivCenter Templates**        | vOneCloud Templates representing two or more vCenter VM                                   |
|                                      | Templates cannot currently be defined.                                                    |
+--------------------------------------+-------------------------------------------------------------------------------------------+
| **No spaces in Clusters**            | VMware Clusters with space in their names are not supported                               |
+--------------------------------------+-------------------------------------------------------------------------------------------+

These limitations will be addressed in future versions of vOneCloud. The vOneCloud roadmap can be consulted in the `OpenNebula development portal <http://dev.opennebula.org/projects/opennebula/issues?query_id=61>`__.

If you feel that there is a particular feature interesting for the general public and it is missing from the roadmap, feel free to add a feature request in the development portal (via the New Issue tab).
