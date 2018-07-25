.. _resolved_issues_in_3.0.2:

========================
Resolved Issues in 3.0.2
========================

vOneCloud 3.0.2 is a maintenance release with the following added functionlity:

* Scroll Bar in Sunstone VM Log.
* Add boolean to option list for User Inputs in VM template.
* Additional confirmation level for critical actions and VMs.
* Add volatile disk should allow user to specify size in MB as well as GB.
* Wild VMs should import NICs and Disks.
* Ease DS selection on VM Template update and instantiation.
* Add SCHEDULED ACTIONS to VM Templates.

Also, this version comes with numerous bugfixes:

* Improve consistency of networks created when importing templates and wilds.
* OpenNebula flow should only work on leader.
* VM with ipv6 Error in ip6tables chain.
* detach disks are not being delete if vm is running.
* detach disk is not being properly applied.
* After a successful datastore monitoring UNKNOWN VMs change to RUNNING.
* Wrong message when doing a disk save as.
* Wrong error msg when disk saveas without name.
* Support spaces in VMDK names and dirnames.
* vCenter VM NICs pointing to the same network are not correctly identified.
* Skip vCenter VApps when importing templates as they are not supported.
* GPRAPHICS PORT is not cleared after freeing it in the cluster vnc port pool.
* Wrong import of vCenter VM Templates with NICs in Distributed vSwitches or Distributed Ports.
* Registering image with complex URL in PATH fails.
* Empty list of Zombie VMs.
* VMs wrongly reported as ZOMBIES.
* OpenNebula does not take into account VM NIC MAC value
* A myiriad of Sunstone bugfixes and small revamps.

