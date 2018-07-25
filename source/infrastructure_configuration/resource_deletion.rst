.. _resource_deletion:

================================================================================
Resource Deletion
================================================================================

There are different behavior of the vCenter resources when deleted in vOneCloud.

The following resources are NOT deleted in vCenter when deleted in vOneCloud:

- VM Templates.
- Networks. Unless OpenNebula has created the port groups and/or switches instead of just consume them.
- Datastores.

The following resource are deleted in vCenter when deleted in vOneCloud:

- Virtual Machines.
- Images. A VMDK or ISO file will be deleted in vCenter unless the VCENTER_IMPORTED attribute is set to YES.