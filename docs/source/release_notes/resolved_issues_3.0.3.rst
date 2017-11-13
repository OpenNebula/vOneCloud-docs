.. _resolved_issues_in_3.0.3:

========================
Resolved Issues in 3.0.3
========================

vOneCloud 3.0.3 is a maintenance release with the following added functionlity:

* Enable template save as for vCenter.
* More comprehensive error messages.
* Force even memory values for MEM attribute.


Also, this version comes with numerous bugfixes:

* ldap driver with rfc2307bis does not use correct user field.
* Protected info all method does respond_to in Ruby 1_9.
* Dashboard accounting too slow.
* Total cost does not take into account the cost disks.
* vCenter drivers cosume too much time searching for objects.
* Sunstone cannot disable VM Groups shown in VM creating dialog.
* Erase vnc port and wild mapping entry when you delete a vm.
* Check user permission for disk_snapshot_create.
* Sorting in VM Start Time is done alphabetically.
* OneFlow shutdown command is not available in sunstone.
* VM snapshot revert_delete works with wrong snapshots.
* Dashboard statistics do not show actual VM name.
* Overcommitment update boken in Sunstone.
* No unit selector in disk cloud view.
* VM Instantiate tab cant see memory size.
* vCenter customizations doesnt work.
* VM force shutdown output of shutdown command is executed.
* Unable to start VMs created by deleted users.
* Quota error when exceeding virtual network reservations.
* importing network on vcenter with vlan doesnt report the vlan id.
* onedb change body should not include volatile AR parameters.
* onedb purge history only works with VMs with multiple history records in the body.
* Not release VNC port when stop the virtual machine.
* sql opennebula logdb table grows indefinitely in solo mode.
* Fix user oned session cache for users.
* After importing wild VM with an unavailable VNC por it throws an error but the VM is stuck in HOLD.
* Warn user or throw error when VNET does not exist when instantiating.
* Snapshots of non persistent images are not deleted on VM termination.
* OneFlow sends a delete to VMs if terminate fails.
* Scheduler cannot handle hosts with more than 2TB memory.
* Script injection in SPICE viewer only Firefox.
* IMAGE_UNAME field must be quoted when adding files in the context section.
* Cant change vcenter credentials.
* Can not select English language if default language is set to another one.
* Importing vcenter resources without any Host.
* VDC resources are not being retrieved properly in Sunstone.
* Linked clones are always created when importing templates.
* Import templates discards linked clones value.
* Problem with IE11.
* Import datastores without any vcenter cluster.
* vCenter automatic_vlan_id does not work.
* vCenter VM can have different NIC MAC than requested.
* vCenter VM NICs pointing to the same network are not correctly identified.

