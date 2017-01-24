.. _whats_new:

========================
What's New vOneCloud 2.2
========================

vOneCloud 2.2 is powered by OpenNebula 5.2.1 'Excession', and, as such, includes functionality present in :onedoc:`OpenNebula 5.2 'Excession' <intro_release_notes/release_notes/index.html>` relevant to vOneCloud:

* **Support for clustered Datastores**, SDRS clustered :ref:`datastores <vcenter_ds>` are now visible in vCenter.
* **Better Sunstone support**, with host dropdown option in DS creation and image import.
* **Network monitoring**, now vCenter VMs network traffic is accounted for in OpenNebula.
* **Limit VM Network consumption**, with :ref:`specific values <import_networks>` available in each of the NICs of a Virtual Machine.
* **More useful vCenter networks import**, :ref:`importing networks <import_networks>` with the same name in different clusters is now possible.
* **More useful vCenter datracenter import**, :ref:`importing datastores <import_images_and_ds>` skips those not associated with any cluster.

Multiple bugfixes and documentation improvements have been included in this version. For instance, attaching and detaching network cards properly rollback if an error is found, uploading VMDKs is less error prone, fixed errors in CDROM attach/detach, better support for CDROMs, and a long list of other bugfixes and enhancements that can be consulted in the `development portal <https://dev.opennebula.org/projects/opennebula/issues?utf8=%E2%9C%93&set_filter=1&f%5B%5D=fixed_version_id&op%5Bfixed_version_id%5D=%3D&v%5Bfixed_version_id%5D%5B%5D=83&v%5Bfixed_version_id%5D%5B%5D=87&f%5B%5D=&c%5B%5D=tracker&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=subject&c%5B%5D=assigned_to&c%5B%5D=updated_on&group_by=category>`__.

vOneCloud 2.2 has been certified with :ref:`support for vSphere 5.5 and 6.0 <system_requirements>`.

The :ref:`Automated Upgrade process <control_panel_automatic_upgrades>` implemented by the :ref:`Control Panel <control_panel>` will only be available to users with an active support subscription. With this functionality users will be notified when a new vOneCloud release is available for download and they will be able to upgrade the vOneCloud platform with a single click.
