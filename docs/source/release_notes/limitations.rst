.. _limitations:

=====================
vOneCloud Limitations
=====================

vOneCloud will use pre defined Templates existing in the vCenter to launch Virtual Machines, as such the following limitations apply:

+-------------------------------+--------------------------------------------------------------------+
|  **No VM Contextualization**  |  Virtual Machines won’t have the ability of being contextualized,  |
|                               |    thus the CONTEXT sections of VM Templates won’t be honored.     |
+-------------------------------+--------------------------------------------------------------------+
| **VM Unsupported Operations** | The following operations are NOT supported on vCenter VMs          |
|                               | managed by OpenNebula, although they can be perfomed               |
|                               | through vCenter                                                    |
|                               | - Attach/detach disk to a running VM                               |
|                               | - Attach/detach network interface to a running VM                  |
|                               | - Migrate VM to different ESX clusters                             |
+-------------------------------+--------------------------------------------------------------------+
| **No Security Groups**        | Firewall rules as defined in Security Groups cannot be enforced in |
|                               | vCenter VMs.                                                       |
+-------------------------------+--------------------------------------------------------------------+
| **No MultivCenter Templates** | vOneCloud Templates representing two or more vCenter VM            |
|                               | Templates cannot currently be defined.                             |
+-------------------------------+--------------------------------------------------------------------+

These limitations will be addressed in future versions of vOneCloud.
