.. _interfaces:

====================
vOneCloud Interfaces
====================

vOneCloud offers a rich set of interfaces to interact with your cloud infrastructure, tailored for specific needs of cloud administrators and cloud users alike.

Web Interface (Sunstone)
------------------------

vOneCloud web interface, called Sunstone, offers three main views:

- :doc:`Sunstone vCenter view <administration/sunstone_gui/suns_views.html#vcenter-view>`: Aimed at cloud administrators, this view is tailored to present all the available options to manage the physical and virtual aspects of your vCenter infrastructure.

.. image:: /images/vcenter_view.png
    :align: center

- :doc:`Sunstone Group Admin View <administration/sunstone_gui/vdc_admin_view.html>`: Aimed at Group administrators, this interface is designed to manage all the virtual resources accesible by a group of users, including the creation of new users.

.. image:: /images/vdcadmin_dash.png
    :align: center

.. _vcenter_cloud_view:

- **Sunstone vCenter Cloud View**: Aimed at end users, this interface eases virtual resource provisioning and hides all the complexity of the cloud that is going on behind the scenes. It is a tailored version of the Sunstone :doc:`Cloud View <administration/sunstone_gui/cloud_view.html>`, with adjusted functionality relevant to vOneCloud and vCenter.

.. image:: /images/cloud_dash.png
    :align: center

.. _cli_interface:

Command Line Interface (CLI)
----------------------------

If you are a SysAdmin, you will probably appreciate vOneCloud's :ref:`CLI <user/references/cli.html>`, which uses the same design philosophy behind \*nix commands (one command for each task).

Moreover, vOneCloud ships with a powerful tool (``onevcenter``) to import vCenter clusters, VM Templates and Networks. The tools is self-explanatory, just set the credentials and IP to access the vCenter host and follow on screen instructions.

To access the vOneCloud command line interface you need to :ref:`login into the vOneCloud appliance <advanced_login>`, and switch to the `oneadmin` user.


Application Programming Interfaces (API)
----------------------------------------

If you are a DevOp, you are probably used to build scripts to automate tasks for you. vOneCloud offers a rich set of APIs to build scripts to perform these tasks in different programming languages:

- :doc:`xmlrpc API <integration/system_interfaces/api.html>` Talk directly to the OpenNebula core
- :doc:`Ruby OpenNebula Cloud API (OCA) <integration/system_interfaces/ruby.html>` Build tasks in Ruby
- :doc:`Java OpenNebula Cloud API (OCA) <integration/system_interfaces/java.html>` Build tasks in Java
