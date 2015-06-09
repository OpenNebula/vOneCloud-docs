.. _whats_new:

========================
What's New vOneCloud 1.6
========================

vOneCloud 1.6 is powered by OpenNebula Cotton Candy, and, as such, includes all the functionality present in :doc:`OpenNebula 4.12 Cotton Candy <release_notes/release_notes/index.html>`. 

The following Cloud Management features have been introduced in vOneCloud 1.6:

- :ref:`Capacity honoring in VM Templates <operations_on_templates>`. VM Templates can be adjusted in terms of CPU and Memory. vOneCloud will modify these parameters at the time of cloning a Template into a Virtual Machine
- :ref:`Capacity resizing <operations_on_running_vms>`. Running VMs can be poweroff and having their capacity (CPU and/or Memory) changed.
- :ref:`Resource Pool <resource_pool>`. vOneCloud can be confined into a Resource Pool, to allow only a fraction of the vCenter infrastructure to be used by vOneCloud users
- :ref:`Provisioning scripts <customer_vars>`. vOneCloud can instruct VMs to run generic scripts at boot time to further configure the guest OS or any software package
- :ref:`Keymap support for VNC connections <operations_on_templates>`. Now the keyboard layout can be defined to improve the VNC connection experience

Multiple bugfixes and documentation improvements have been included in this version. vOneCloud 1.6 has been certified with :ref:`support for vSphere 5.5 and 6.0 <system_requirements>`.

The :ref:`Automated Upgrade process <control_panel_automatic_upgrades>` implemented by the :ref:`Control Panel <control_panel>` will only be available to users with an active support subscription. With this functionality users will be notified when a new vOneCloud release is available for download and they will be able to upgrade the vOneCloud platform with a single click. However, this release (1.6) has been marked as public so everyone can upgrade from previous versions using the Control Panel.
