.. _known_issues:

============================
Known Issues and Limitations
============================

Known Issues
================================================================================

These known issues will be addressed in future versions of vOneCloud:

* `Delete operation leaves a poweroff instance registered in vCenter <http://dev.opennebula.org/issues/4648>`__.
* `Wrong import of vCenter VM Templates with NICs in Distributed vSwitches or Distributed Ports <https://dev.opennebula.org/issues/5246>`__
* `Spaces in VMDK names and dirnames not supported <https://dev.opennebula.org/issues/5288>`__
* `Cloud vcenter view does not allow creation of VMs <https://dev.opennebula.org/issues/5313>`__

Fix VM creation problem in 3.0.0
--------------------------------

Release 3.0.0 has a problem in the cloud views that do not let users create new VMs (already fixed in 3.0.1+). Here are the steps to fix this problem in 3.0.0 appliances:

* Enable ssh access to the vOneCloud appliance following :ref:`these instructions <control_panel_system_options_ssh>`

* Connect as root to the frontend using ssh. If you are using windows you can use the software PUTTY, for Linux or Mac OS X you can use the terminal:

.. code::

    ssh root@<your frontend>

* Execute this command, do a copy and paste as any change to the command can make it fail:

.. code::

    sed -i 's/^            templates: false$/            templates: true/' /etc/one/sunstone-views/cloud.yaml

* Close the ssh terminal an return to vOneCloud control panel

* Restart OpenNebula

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
| **VM Unsupported Operations**          | The following operations are only supported from vCenter:                                                                                                                                                                                                                                                                                                                                                                     |
|                                        | - Migrate VM to different ESX clusters                                                                                                                                                                                                                                                                                                                                                                                        |
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
| **VLAN ID not reported**               | vCenter precreated networks are not imported with the VLAN ID information, although they'll work as expected                                                                                                                                                                                                                                                                                                                  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Wrong capcity check at import time** | When a vCenter template or wild VM is imported into OpenNebula, the virtual disks are imported, and vOneCloud tries to fit them in the DS. If not enough space are left, the import may fail.                                                                                                                                                                                                                                 |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **No user feedback on upgrades**       | If you click on **Upgrade** or **Upgrade Now** (to upgrade the vOneCloud version, or the system packages, respectively), you will see that a few jobs appear in `pending` state in the job queue. You will not receive any further user feedback until it finishes executing. This may take a long time: 15 minutes for **Upgrade**, and even more than an hour for **Upgrade Now**, depending on your internet access speed. |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


If you find any new limitation, feel free to add a feature request in `Community - Feature Request section of the vOneCloud Support Portal <https://support.vonecloud.com/hc/communities/public/topics/200215442-Community-Feature-Requests>`__.
