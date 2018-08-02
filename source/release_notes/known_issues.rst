.. _known_issues:

============================
Known Issues and Limitations
============================

Known Issues
================================================================================

These known issues will be addressed in future versions of vOneCloud:

* `vCenter cant import templates with ISOS <https://github.com/OpenNebula/one/issues/2329>`__.
* `NIC Model is ignored on VM vCenter Template <https://github.com/OpenNebula/one/issues/2293>`__
* `VNC on ESXi Can Break Firewall <https://github.com/OpenNebula/one/issues/1728>`__
* `Wild VM monitoring should not return datastores that contain only swap files <https://github.com/OpenNebula/one/issues/1699>`__
* `Template delete recursive operation of templates instantiated as persistent does not remove images from the vcenter datastores <https://github.com/OpenNebula/one/issues/1350>`__
* `Saving a template from a VM that has been instatiated to persistent does not work <https://github.com/OpenNebula/one/issues/1299>`__

Found more?
-----------

If you find any new issue, please let us know in the `Community Questions section of the vOneCloud Support Portal <https://support.vonecloud.com/hc/communities/public/questions>`__.

.. _limitations:

Limitations
================================================================================

These limitations will be addressed in future versions of vOneCloud:

+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|             **Limitation**             |                                                                                                                                                                                                        **Description**                                                                                                                                                                                                        |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **No FILES support in context**        | Contextualization in vOneCloud does not support passing files to Virtual Machines                                                                                                                                                                                                                                                                                                                                             |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Cannot import "one-<id>" VMs**       | VMs deployed by another instance of vOneCloud, or machines named with a leading "one-" cannot be imported again                                                                                                                                                                                                                                                                                                               |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **vCenter password length**            | Cannot be more than 22 characters                                                                                                                                                                                                                                                                                                                                                                                             |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Browser Adblock plug ins**           | Features like VNC and VM log viewer may be affected by Adblock plug ins. Please disable these plug ins if you are experiencing issues                                                                                                                                                                                                                                                                                         |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Cloning imported VMs**               | Cloning in vCenter an imported VM will result in a VM that cannot be imported again. Please instantiate from templates and import the resulting VMs, instead of cloning already imported VMs.                                                                                                                                                                                                                                 |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **No user feedback on upgrades**       | If you click on **Upgrade** or **Upgrade Now** (to upgrade the vOneCloud version, or the system packages, respectively), you will see that a few jobs appear in `pending` state in the job queue. You will not receive any further user feedback until it finishes executing. This may take a long time: 15 minutes for **Upgrade**, and even more than an hour for **Upgrade Now**, depending on your internet access speed. |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


If you find any new limitation, feel free to add a feature request in `Community - Feature Request section of the vOneCloud Support Portal <https://support.vonecloud.com/hc/communities/public/topics/200215442-Community-Feature-Requests>`__.
