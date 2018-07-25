.. _interfaces:

====================
vOneCloud Interfaces
====================

vOneCloud offers a rich set of interfaces to interact with your cloud infrastructure, tailored for specific needs of cloud administrators and cloud users alike.

You can select one of the available views clicking in the username at the top right of the screen and selecting the Views entry.

.. image:: /images/select_view.png
    :align: center


Web Interface (Sunstone)
------------------------

vOneCloud web interface, called Sunstone, offers three main views:

- :onedoc:`Sunstone Admin view <deployment/sunstone_setup/suns_views.html#admin-view>`: Aimed at cloud administrators, this view is tailored to present all the available options to manage the physical and virtual aspects of your vCenter infrastructure.

.. image:: /images/vcenter_view.png
    :align: center

- :onedoc:`Sunstone Group Admin View <deployment/sunstone_setup/suns_views.html#group-admin-view>`: Aimed at Group administrators, this interface is designed to manage all the virtual resources accessible by a group of users, including the creation of new users.

.. image:: /images/vdcadmin_dash.png
    :align: center

.. _vcenter_cloud_view:

- **Sunstone Cloud View**: Aimed at end users, this interface eases virtual resource provisioning and hides all the complexity of the cloud that is going on behind the scenes. It is a tailored version of the Sunstone :onedoc:`Cloud View <deployment/sunstone_setup/suns_views.html#cloud-view>`, with adjusted functionality relevant to vOneCloud and vCenter.

.. image:: /images/cloud_dash.png
    :align: center

.. _cli_interface:

Command Line Interface (CLI)
----------------------------

If you are a SysAdmin, you will probably appreciate vOneCloud's :onedoc:`CLI <operation/references/cli.html>`, which uses the same design philosophy behind \*nix commands (one command for each task).

Moreover, vOneCloud ships with a powerful tool (``onevcenter``) to import vCenter clusters, VM Templates and Networks. The tools is self-explanatory, just set the credentials and IP to access the vCenter host and follow on screen instructions.

To access the vOneCloud command line interface you need to :ref:`login into the vOneCloud appliance <advanced_login>`, and switch to the `oneadmin` user.


Application Programming Interfaces (API)
----------------------------------------

If you are a DevOp, you are probably used to build scripts to automate tasks for you. vOneCloud offers a rich set of APIs to build scripts to perform these tasks in different programming languages:

- :onedoc:`xmlrpc API <integration/system_interfaces/api.html>` Talk directly to the OpenNebula core
- :onedoc:`Ruby OpenNebula Cloud API (OCA) <integration/system_interfaces/ruby.html>` Build tasks in Ruby
- :onedoc:`Java OpenNebula Cloud API (OCA) <integration/system_interfaces/java.html>` Build tasks in Java
