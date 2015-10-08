.. _whats_new:

========================
What's New vOneCloud 1.8
========================

vOneCloud 1.8 is powered by OpenNebula Great A'Tuin, and, as such, includes functionality present in :doc:`OpenNebula 4.14 Great A'Tuin <release_notes/release_notes/index.html>` relevant to vOneCloud:

- :ref:`Import VMs from public clouds <operations_on_running_vms>`. vOneCloud 1.8 introduces the management of VMs not launched by vOneCloud in either Amazon EC2, Microsoft Azure and IBM SoftLayer.
- :ref:`Keep the VM disks after deletion <add_multi_cluster_vm_template>`. A new attribute, KEEP_DISKS_ON_DONE will instruct vOneCloud on leaving or deleting the VM disks when they finish their lifecycle.

Additionally, vOneCloud 1.8 adds new features related with the vCenter driver not yet present in any OpenNebula release:

- :ref:`Pagination added to vCenter import dialog <acquire_resources>`. In large scale deployments, this will aid in the importation of large numbers of VM Templates and Networks.
- :ref:`Support for Guest Customization <vcenter_customization>`. At the time of creating or modifying an imported VM Template, it is now possible to associate a Guest Customization profile to configure guest OS parameters such as the computer name, network settings, setting and expiring the administrator/root password, SID change for Windows Operating systems, and so on.
- :ref:`Show all the IPs from a VM in Sunstone <operations_on_templates>`. Both for imported and newly created VMs, all the IP addresses reported by the guest OS via the VMware tools are retrieved by vOneCloud and presented in Sunstone.
- :ref:`Append name to "one-*" name in vCenter display name <name_suffix_note>`. VM Name as shown in vOneCloud is appended in vCenter VM name for easier VM tracking.
- :ref:`Imported resources suffixed with their source cluster name <cluster_prefix>`. This feature aids in the resource identification in the vCenter portal by mapping it to the vOneCloud representation name.
- :ref:`Multi cluster VM Template definition <add_multi_cluster_vm_template>`. Create vOneCloud VM Templates that reference more than one vCenter VM Template in different vCenter clusters.

The Control Panel has also been extended in this release:

- :ref:`Enable SSH <control_panel_system_options_ssh>`. To easily allow console access to the vOneCloud appliance.
- :ref:`Enable SSL <control_panel_system_options_ssl>`. To enable the secure access to the vOneCloud appliance web interface (Sunstone) using the SSL protocol.

Additionally, a new documentation category starts with vOneCloud 1.8 to explain advanced customizations to the appliance that are not performed through the Control Panel:

- :ref:`vOneCloud rebranding <advanced_customizations_rebranding>`. hange the logos of the Sunstone interface.

Multiple bugfixes and documentation improvements have been included in this version. vOneCloud 1.8 has been certified with :ref:`support for vSphere 5.5 and 6.0 <system_requirements>`.

The :ref:`Automated Upgrade process <control_panel_automatic_upgrades>` implemented by the :ref:`Control Panel <control_panel>` will only be available to users with an active support subscription. With this functionality users will be notified when a new vOneCloud release is available for download and they will be able to upgrade the vOneCloud platform with a single click. However, this release (1.8) has been marked as public so everyone can upgrade from previous versions using the Control Panel.
