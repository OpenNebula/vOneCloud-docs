.. _known_issues:

============================
Known Issues and Limitations
============================

Known Issues
================================================================================

These known issues will be addressed in future versions of vOneCloud:

* `Delete operation leaves a poweroff instance registered in vCenter <http://dev.opennebula.org/issues/4648>`__.
* `Wrong import of vCenter VM Templates with NICs in Distributed vSwitches or Distributed Ports <https://dev.opennebula.org/issues/5246>`__

Found more?
-----------

If you find any new issue, please let us know in the `Community Questions section of the vOneCloud Support Portal <https://support.vonecloud.com/hc/communities/public/questions>`__.

.. _limitations:

Limitations
================================================================================

These limitations will be addressed in future versions of vOneCloud:

+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          **Limitation**         |                                                                                        **Description**                                                                                        |
+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **VM Unsupported Operations**   | The following operations are only supported from vCenter:                                                                                                                                     |
|                                 | - Migrate VM to different ESX clusters                                                                                                                                                        |
+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **No spaces in VMDKs**          | VMDKs with spaces in their names or paths (ie, folders that contain them) are not supported for importing, attaching or uploading                                                             |
+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **No FILES support in context** | Contextualization in vOneCloud does not support passing files to Virtual Machines                                                                                                             |
+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Cannot import "one-" VMs**    | VMs deployed by another instance of vOneCloud, or machines named with a leading "one-" cannot be imported again                                                                               |
+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **vCenter password length**     | Cannot be more than 22 characters                                                                                                                                                             |
+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Browser Adblock plug ins**    | Features like VNC and VM log viewer may be affected by Adblock plug ins. Please disable these plug ins if you are experiencing issues                                                         |
+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Cloning imported VMs**        | Cloning in vCenter an imported VM will result in a VM that cannot be imported again. Please instantiate from templates and import the resulting VMs, instead of cloning already imported VMs. |
+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **VLAN ID not reported**        | vCenter precreated networks are not imported with the VLAN ID information, although they'll work as expected                                                                                  |
+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

If you find any new limitation, feel free to add a feature request in `Community - Feature Request section of the vOneCloud Support Portal <https://support.vonecloud.com/hc/communities/public/topics/200215442-Community-Feature-Requests>`__.
