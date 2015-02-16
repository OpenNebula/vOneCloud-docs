.. _whats_new:

========================
What's New vOneCloud 1.2
========================

vOneCloud 1.2 is powered by OpenNebula Fox Fur, and, as such, includes all the functionality present in `OpenNebula 4.10 Fox Fur <http://docs.opennebula.org/4.10/release_notes/release_notes/index.html>`__.

New Features
================================================================================

The following Cloud Management features have been introduced in vOneCloud 1.2:

- :ref:`Import running VMs <import_running_vms>`. vCenter running Virtual Machines can be now be imported seamlessly in vOneCloud without powering them off and hence without any downtime!
- :ref:`Support for vCenter Networks <acquire_resources>`. vCenter Networks and Distributed vSwitches can now be imported into vOneCloud, and then used in VM Templates to define network interfaces in vCenter virtual machines attached to these Networks and Distributed vSwitches
- :ref:`Attach/Detach network interfaces <vmtemplates_and_networks>`. Virtual Machines can now dynamically (ie, while running) have networks interfaces attached or removed.
- :ref:`HTTP proxy support <control_console>`. Corporate HTTP proxies are supported now in vOneCloud.
- :ref:`New Cloud vCenter view <vcenter_cloud_view>`. Designed for provision end users with vCenter resources in a simple way through vOneCloud.

The following :ref:`components <components>` have been introduced in vOneCloud 1.2:

- The new vOneCloud :ref:`Control Console <control_console>` is a text based wizard to aid in the OneCloud bootstrap process.
- The vOneCloud :ref:`Control Panel <control_panel>` is a slick web interface oriented to the configuration of the vOneCloud services as well as used to update to a newer version of vOneCloud.

The :ref:`Automated Upgrade process <control_panel_automatic_upgrades>` implemented by the :ref:`Control Panel <control_panel>` will only be available to users with an active support subscription. With this functionality users will be notified when a new vOneCloud release is available for download and they will be able to upgrade the vOneCloud platform with a single click.

.. _resolved_issues:

Resolved Issues
================================================================================

The following issues present in vOneCloud 1.0 have been solved in 1.2:

+-----------------------------+-----------------------------------------------------------------------------------------------+
|           **Name**          |                                        **Description**                                        |
+-----------------------------+-----------------------------------------------------------------------------------------------+
| Removed unused VM actions   | VM actions which do not apply in vCenter VM like for instance, VM resize and undeploy actions |
+-----------------------------+-----------------------------------------------------------------------------------------------+
| Fixes for hybrid connectors | Various fixes in configuration, information display and usability                             |
+-----------------------------+-----------------------------------------------------------------------------------------------+
| Fix support in HTTP Proxy   | Now available for all vOneCloud services                                                      |
+-----------------------------+-----------------------------------------------------------------------------------------------+
| Removed unused views        | Sunstone views that did not apply were removed to avoid confusion                             |
+-----------------------------+-----------------------------------------------------------------------------------------------+
