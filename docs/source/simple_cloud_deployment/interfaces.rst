.. _interfaces:

====================
vOneCloud Interfaces
====================

vOneCloud offers a rich set of interfaces to interact with your cloud infrastructure, tailored for specific needs of cloud administrators and cloud users alike.

Web Interface (Sunstone)
------------------------

vOneCloud web interface, called Sunstone, offers two main views:

- `Sunstone vCenter view <http://docs.opennebula.org/4.10/administration/sunstone_gui/suns_views.html#vcenter-view>`__: Aimed at cloud administrators, this view is tailored to present all the available options to manage the physical and virtual aspects of your vCenter infrastructure. 

- `Sunstone Cloud View <http://docs.opennebula.org/4.10/administration/sunstone_gui/cloud_view.html>`__: Aimed at cloud end users, this interface eases virtual resource provisioning and hides all the complexity of the cloud that is going on behind the scenes.


Command Line Interface (CLI)
----------------------------

If you are a SysAdmin, you will probably appreciate vOneCloud's `CLI <http://docs.opennebula.org/4.10/user/references/cli.html>`__, which uses the same design philosophy behind *nix commands (one command for each task).

Moreover, vOneCloud ships with a powerful tool (``onevcenter``) to import vCenter clusters and VM Templates. The tools is self-explanatory, just set the credentials and IP to access the vCenter host and follow on screen instructions.

Cloud Interfaces
----------------

Your EC2 ready applications can run on top of vOneCloud, since it implements the `EC2 Query API <http://docs.opennebula.org/4.10/advanced_administration/public_cloud/introc.html>`__.

Application Programming Interfaces (API)
----------------------------------------

If you are a DevOp, you are probably use to build scripts to automate tasks for you. OpenNebula offers a rich set of APIs to build scripts to perform these tasks in different programming languages:

- `xmlrpc API <http://docs.opennebula.org/4.10/integration/system_interfaces/api.html>`__ Talk directly to the OpenNebula core
- `Ruby OpenNebula Cloud API (OCA) <http://docs.opennebula.org/4.10/integration/system_interfaces/ruby.html>`__ Build tasks in Ruby
- `Java OpenNebula Cloud API (OCA) <http://docs.opennebula.org/4.10/integration/system_interfaces/java.html>`__ Build tasks in Java
- `OneFlow API <http://docs.opennebula.org/4.10/integration/system_interfaces/appflow_api.html>`__ Build tasks to manage Multi-VM services
