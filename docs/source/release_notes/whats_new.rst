.. _whats_new:

========================
What's New vOneCloud 1.2
========================

vOneCloud 1.2 is powered by OpenNebula Fox Fur, and, as such, includes all the functionality present in `OpenNebula Fox Fur 4.10.2 <http://docs.opennebula.org/4.10/release_notes/release_notes/index.html>`__.

.. todo:: OpenNebula 4.10.3

Compared to the 1.0 version of vOneCloud, this stable release comes with a number of bug fixes that can be consulted in the `OpenNebula development portal <http://dev.opennebula.org/projects/opennebula/issues?query_id=62>`__.

The following features and components are being introduced in vOneCloud 1.2 and are worth to be highlighted for their relevance:

- :ref:`New vOneCloud Control Console and Control Panel <components>`. The new vOneCloud :ref:`Control Console <control_console>` is a text based wizard to aid in the OneCloud bootstrap process, and the new vOneCloud :ref:`Control Panel <control_panel>` is a slick web interface oriented to the configuration of the vOneCloud services as well as used to update to a newer version of vOneCloud.
- :ref:`Automated upgrade process <control_panel_automatic_upgrades>`. Users will be notified when a new vOneCloud release is available for download. Paying customers will be able to upgrade with a single click.
- :ref:`Import running VMs <import_running_vms>`. vCenter running Virtual Machines can be now be imported seamlessly in vOneCloud without powering them off and hence without any downtime!
- :ref:`Support for vCenter Networks <acquire_resources>`. vCenter Networks and Distributed vSwitches can now be imported into vOneCloud, and then used in VM Templates to define network interfaces in vCenter virtual machines attached to these Networks and Distributed vSwitches
- :ref:`Attach/Detach network interfaces <vmtemplates_and_networks>`. Virtual Machines can now dynamically (ie, while running) have networks interfaces attached or removed.
- :ref:`HTTP proxy support <control_console>`. Corporate HTTP proxies are supported now in vOneCloud.
- :ref:`New Cloud vCenter view <vcenter_cloud_view>`. Designed for provision end users with vCenter resources in a simple way through vOneCloud.


