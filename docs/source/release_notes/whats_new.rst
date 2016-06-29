.. _whats_new:

========================
What's New vOneCloud 2.0
========================

vOneCloud 2.0 is powered by OpenNebula Wizard, and, as such, includes functionality present in :onedoc:`OpenNebula 5.0 Wizard <intro_release_notes/release_notes/index.html>` relevant to vOneCloud:

- :ref:`Datastore <add_new_datastore>` and :ref:`VMDK image <add_new_images>` management, as well as :ref:`import <import_images_and_ds>`.
- :ref:`New Virtual Router Resource <virtual_routers>`, to allow routing between isolated virtual networks.
- :ref:`More flexible vCenter VM naming <name_prefix_note>`, with a configurable prefix.
- :ref:`New resource pool mode <resource_pool>`, with the ability to select in which resource pool a particular VM is confined.
- :ref:`OneFlow new templates operations <multi_vm_applications>`, like the ability to clone existing service templates.
- :ref:`Keep disks on done <keep_disks_one_done>`, to avoid deleting disks when the VM is terminated.
- :ref:`Instantiate to persistent <instantiate_to_persistent>`, to easily create a rich VM Template catalog.
- :ref:`Dynamic VM reconfiguration <vm_dynamic_reconfiguration>`, that can be performed while the VM is running or powered off.
- :ref:`Share resources between logical clusters <create_vdc>`, like Virtual Networks and Datastores.

An important effort has been carried out focusing on optimizations, allowing vOneCloud to manage vCenter instances with large number of VM Templates, VMs and Networks. Also, multiple bugfixes and documentation improvements have been included in this version. vOneCloud 2.0 has been certified with :ref:`support for vSphere 5.5 and 6.0 <system_requirements>`.

Hybrid cloud functionality has been removed to simplify maintenance and upgrades.

The :ref:`Automated Upgrade process <control_panel_automatic_upgrades>` implemented by the :ref:`Control Panel <control_panel>` will only be available to users with an active support subscription. With this functionality users will be notified when a new vOneCloud release is available for download and they will be able to upgrade the vOneCloud platform with a single click.
