
.. _requirements:

============
Requirements
============

.. warning:: It is advised to manage one vCenter by only one OpenNebula (ie, do not manage the same vCenter from two different OpenNebulas). Otherwise VMs from both server will clash and produce errors.

The following components are needed to be present in the infrastructure to implement a cloud infrastructure run by OpenNebula:

+---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Component** |                                                                                                                                                             **Observations**                                                                                                                                                             |
+---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vCenter       | - ESX hosts, VM Templates and Running VMs expected to be managed by OpenNebula needs to be grouped into clusters                                                                                                                                                                                                                         |
|               | - The IP or DNS needs to be known, as well as the credentials (username and password) of an :onedoc:`admin user <deployment/node_installation/vcenter_node_installation.html>`.                                                                                                                                                          |
+---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ESX           | - At least 1 with 2 GB of free RAM and 1 free CPU                                                                                                                                                                                                                                                                                        |
+---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Guest OS      | - VMware tools are needed in the guestOS to enable several features (contextualization and networking feedback). Please install `VMware Tools (for Windows) <https://www.vmware.com/support/ws55/doc/new_guest_tools_ws.html>`__ or `Open Virtual Machine Tools <https://github.com/vmware/open-vm-tools>`__ (for \*nix) in the guestOS. |
+---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Browser       | - IE, Chrome and Firefox                                                                                                                                                                                                                                                                                                                 |
+---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Check specific versions in the :onedoc:`OpenNebula documentation </intro_release_notes/release_notes/platform_notes.html>`.

.. note:: To enable VNC functionality, please follow the :onedoc:`instructions in the main OpenNebula documentation <deployment/node_installation/vcenter_node_installation.html#vnc-on-esx-hosts>`.