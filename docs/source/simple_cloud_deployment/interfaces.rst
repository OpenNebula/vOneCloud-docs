.. _interfaces:

====================
vOneCloud Interfaces
====================

vOneCloud offers a rich set of interfaces to interact with your cloud infrastructure, tailored for specific needs of cloud administrators and cloud users alike.

Web Interface (Sunstone)
------------------------

vOneCloud web interface, called Sunstone, offers three main views:

- `Sunstone vCenter view <http://docs.opennebula.org/4.10/administration/sunstone_gui/suns_views.html#vcenter-view>`__: Aimed at cloud administrators, this view is tailored to present all the available options to manage the physical and virtual aspects of your vCenter infrastructure.

.. image:: /images/vcenter_view.png
    :align: center

- `Sunstone VDC Admin View <http://docs.opennebula.org/4.10/administration/sunstone_gui/vdc_admin_view.html>`__: Aimed at Virtual Datacenter administrators, this interface is designed to manage all the virtual resources of the VDC, including the creation of new users.

.. image:: /images/vdcadmin_dash.png
    :align: center

- `Sunstone Cloud View <http://docs.opennebula.org/4.10/administration/sunstone_gui/cloud_view.html>`__: Aimed at end users, this interface eases virtual resource provisioning and hides all the complexity of the cloud that is going on behind the scenes.


.. todo::

   Document vCenter-Cloud view

.. image:: /images/cloud_dash.png
    :align: center

.. _cli_interface:

Command Line Interface (CLI)
----------------------------

If you are a SysAdmin, you will probably appreciate vOneCloud's `CLI <http://docs.opennebula.org/4.10/user/references/cli.html>`__, which uses the same design philosophy behind \*nix commands (one command for each task).

Moreover, vOneCloud ships with a powerful tool (``onevcenter``) to import vCenter clusters, VM Templates and Networks. The tools is self-explanatory, just set the credentials and IP to access the vCenter host and follow on screen instructions.

To access the vOneCloud command line interface open the vCenter console of the vOneCloud Virtual Machine appliance and change the tty (Ctrl + Alt + F2). Afterwards, log in with the `root` account and the password you used in the :ref:`initial configuration <download_and_deploy_control_console>`, and switch to the `oneadmin` user.


Application Programming Interfaces (API)
----------------------------------------

If you are a DevOp, you are probably used to build scripts to automate tasks for you. vOneCloud offers a rich set of APIs to build scripts to perform these tasks in different programming languages:

- `xmlrpc API <http://docs.opennebula.org/4.10/integration/system_interfaces/api.html>`__ Talk directly to the OpenNebula core
- `Ruby OpenNebula Cloud API (OCA) <http://docs.opennebula.org/4.10/integration/system_interfaces/ruby.html>`__ Build tasks in Ruby
- `Java OpenNebula Cloud API (OCA) <http://docs.opennebula.org/4.10/integration/system_interfaces/java.html>`__ Build tasks in Java
