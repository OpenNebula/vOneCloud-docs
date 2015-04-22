.. _whats_new:

========================
What's New vOneCloud 1.4
========================

vOneCloud 1.4 is powered by OpenNebula Cotton Candy, and, as such, includes all the functionality present in :doc:`OpenNebula 4.12 Cotton Candy <release_notes/release_notes/index.html>`. 

The following Cloud Management features have been introduced in vOneCloud 1.4:

- :ref:`Showback functionality <showback>`. New toolset that reports resource usage cost, and allows the integration with chargeback and billing platforms.
- :ref:`Import running VMs with VNC capabilities <import_running_vms>`. vCenter running VMs with VNC ports set to open will be imported with VNC capabilities in vOneCloud
- :ref:`Multi-VM capabilities <multi_vm_applications>`. Management of sets of VMs (services) through the OneFlow component
- :ref:`Improved import and reacquire resources (VM, VM Templates and Networks) <import_running_vms>`. Separated dialogs for each resource instead of performing this actions through the host creation dialog
- :ref:`Improved Group/VDC provisioning model <create_vdc>`. Making VDCs a separate resource has several advantages over the previous Group/VDC concept, since they can have one or more Groups added to them

The Control Panel has also been extended in this release:

- :ref:`Debug capabilities embedded in Control Panel <app_conf_trouble_debug>`. Useful to gather all the details of your infrastructure and get the best support

Multiple bugfixes and documentation improvements have been included in this version. Moreover, vOneCloud 1.4 has been certified with :ref:`support for vSphere 6.0 <system_requirements>`.

The :ref:`Automated Upgrade process <control_panel_automatic_upgrades>` implemented by the :ref:`Control Panel <control_panel>` will only be available to users with an active support subscription. With this functionality users will be notified when a new vOneCloud release is available for download and they will be able to upgrade the vOneCloud platform with a single click. However, this release (1.4) has been marked as public so everyone can upgrade from previous versions using the Control Panel.
