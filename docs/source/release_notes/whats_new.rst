.. _whats_new:

========================
What's New vOneCloud 3.0
========================

vOneCloud 3.0 is powered by OpenNebula 5.4.0 'Medusa', and, as such, includes functionality present in :onedoc:`Medusa <intro_release_notes/release_notes/index.html>` relevant to vOneCloud:

.. _todo: link to documentation of each functionality

* **Enhanced storage management**, vOneCloud is fully aware of all VMs disks. Non-persistent images and volatiles disks are now supported.
* **Storage quotas and datastore capacity check**, never run out of capacity correctly dimensioning the available datastores and the storage quotas given to end users
* **Linked clone support**, add support for linked clones for VMs at the time of importing a VM Template
* **Disk resize capabilities**, resize the capacity of a VM disk at boot time or when the VM is in poweroff
* **Save disk functionality**, register any VM disk as an image for later use in VMs, either directly from a VM Template or through the disk attach operation
* **Disk statistics monitoring**, know the disk I/O of any VM
* **Save as Template functionality**, save any VM as a VM Template at any point during its lifecycle
* **Clearer Clustered datastores**, only imported as system datastores to minimize changes of wrong use
* **Network creation support**, a new vCenter network mode is available in virtual network definition, standard and different port groups and vSwitches can be created from within OpenNebula. VLAN IDs, MTUs and number of ports can be specified when a port group is created.
* **Full storage and networking support in imported VM Templates**, images and networks representing disks and network interfaces are created for VM templates and folder placement features.
* **Improved CDROM management**, now a new CDROM drive is added to the VM if not present when an ISO image is attached
* **Imported VMs improvements**, with the possibility of adding VNC to any imported VM
* **Removed naming limitations**, vCenter cluster and datastore names with spaces are now supported
* **Improved monitoring**, up to two orders of magnitude of speedup
* **Faster VM deployment**, with up to 10 VM spinning up simultaneously per cluster
* **User input sorting**, to ask the information in the correct order to end users (for instance, username before password)
* **Improved naming conventions**, to allow importing resources with the same name in different vCenter locations

Additionally, vOneCloud 3.0 add new features related with the vCenter driver not yet present in any OpenNebula release:

Multiple bugfixes and documentation improvements have been included in this version. For instance, deleting SSH keys from cloud view, importing images with correct size, VM contextualization persistance across reboots, disk not removed if detached in poweroff state, context disk not displayed in Sunstone, skip import of resources if no permissions available, and a long list of other bugfixes and enhancements that can be consulted in the `development portal <https://dev.opennebula.org/projects/opennebula/issues?utf8=%E2%9C%93&set_filter=1&f%5B%5D=fixed_version_id&op%5Bfixed_version_id%5D=%3D&v%5Bfixed_version_id%5D%5B%5D=86&f%5B%5D=&c%5B%5D=tracker&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=subject&c%5B%5D=assigned_to&c%5B%5D=updated_on&group_by=>`__.

vOneCloud 3.0.0 has been certified with :ref:`support for vSphere 5.5, 6.0 and 6.5 <system_requirements>`.

Upgrade to 3.0.0 from previous versions cannot be performed automatically. If you hold an active support subscription, please `contact OpenNebula Systems <mailto:support@opennebula.systems&subject="Upgrade to vOneCloud 3.0.0">`__ to schedule a vOneCloud upgrade.
