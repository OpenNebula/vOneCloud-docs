.. _whats_new:

========================
What's New vOneCloud 3.0
========================

vOneCloud 3.0 is powered by OpenNebula 5.4.0 'Medusa', and, as such, includes functionality present in :onedoc:`Medusa <intro_release_notes/release_notes/index.html>` relevant to vOneCloud:

.. _todo: link to documentation of each functionality

* **Enhanced storage management**, vOneCloud is fully aware of all :ref:`VMs disks <import_vm_templates>`. Non-persistent images and volatiles disks are now supported.
* **Storage quotas and datastore capacity check**, never run out of capacity correctly dimensioning the available datastores and the storage :ref:`quotas <resource_quotas>` given to end users
* **Balance storage load** of :ref:`VMs across datastores <select_datastore>` automatically without the need of Storage DRS
* **Linked clone support**, add support for :ref:`linked clones<linked_clones>` for VMs at the time of importing a VM Template
* **Disk resize capabilities**, :ref:`resize <disk_resize>` the capacity of a VM disk at boot time or when the VM is in poweroff
* **Save disk functionality**, :ref:`register any VM disk as an image <disk_save>` for later use in VMs, either directly from a VM Template or through the disk attach operation
* **Save as Template functionality**, :ref:`save any VM as a VM Template<save_as_template>` at any point during its lifecycle
* **Folder management**, define in which :ref:`vCenter folder <vm_placement>` you want your VMs into, on a VM to VM basis.
* **Network creation support**, a new vCenter network model is available in virtual network definition, :ref:`standard and different port groups and vSwitches can be created <vcenter_enhanced_networking>` from within OpenNebula. VLAN IDs, MTUs and number of ports can be specified when a port group is created.
* **Full storage and networking support** in :ref:`imported VM Templates <import_vm_templates>`, images and networks representing disks and network interfaces are created for VM templates and folder placement features.
* **Improved CDROM management**, now a new :ref:`CDROM drive <add_new_images>` is added to the VM if not present when an ISO image is attached
* **Imported VMs improvements**, with the possibility of :ref:`adding VNC to any imported VM <import_vms>`.
* **Removed naming limitations**, vCenter cluster and :ref:`datastore <add_new_datastore>` names with spaces are now supported
* **Improved performance**, up to two orders of magnitude of speedup in monitoring and import times, as well as less error prone synchronous calls to vCenter
* **Faster VM deployment**, with up to 10 VM spinning up simultaneously per cluster
* **User input sorting**, to :ref:`ask information <user_inputs>` in the correct order to end users (for instance, username before password), and also new types (lists, booleans, etc)
* **Improved naming conventions**, to allow importing resources with the same name in different vCenter locations
* **Numerous web interface enchancements**, like automatic estimation of VM cost through the Showback mechanism, better VM information display in :ref:`Cloud View <cloud_view>`, image upload resume option, improved user and group management dialogs and many more.
* **Better audit trail**, now the history records of VMs includes the UID of the user that perfomed the action

Additionally, vOneCloud 3.0 add new features related with the vCenter driver not yet present in any OpenNebula release:

Multiple bugfixes and documentation improvements have been included in this version. For instance, deleting SSH keys from cloud view, importing images with correct size, VM contextualization persistance across reboots, disk not removed if detached in poweroff state, context disk not displayed in Sunstone, skip import of resources if no permissions available, and a long list of other bugfixes and enhancements that can be consulted in the `development portal <https://dev.opennebula.org/projects/opennebula/issues?utf8=%E2%9C%93&set_filter=1&f%5B%5D=fixed_version_id&op%5Bfixed_version_id%5D=%3D&v%5Bfixed_version_id%5D%5B%5D=86&f%5B%5D=&c%5B%5D=tracker&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=subject&c%5B%5D=assigned_to&c%5B%5D=updated_on&group_by=>`__.

vOneCloud 3.0.0 has been certified with :ref:`support for vSphere 5.5, 6.0 and 6.5 <system_requirements>`.

Upgrade to 3.0.0 from previous versions cannot be performed automatically. If you hold an active support subscription, please `contact OpenNebula Systems <mailto:support@opennebula.systems&subject="Upgrade to vOneCloud 3.0.0">`__ to schedule a vOneCloud upgrade.
