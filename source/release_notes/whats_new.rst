.. _whats_new:

========================
What's New vOneCloud 3.4
========================

vOneCloud 3.4 is powered by OpenNebula 5.8 'Edge', and, as such, includes functionality present in :onedoc:`Edge <intro_release_notes/release_notes/index.html>` relevant to vOneCloud:


* **Change boot order** of VM devices updating the VM Template. More info :onedoc:`here <operation/references/template.html#template-os-and-boot-options-section>`.
* **VM migration between clusters and datastores** is now supported, check :ref:`here <migrate_virtual_machines>`.
* **Migrate images from KVM to vCenter**, or vice versa. More info :onedoc:`here <advanced_components/marketplace/migrate_images.html#migrate-images>`.
* **New configuration file**, default behaviour in the process of image importation can be changed. More info :onedoc:`here <deployment/vmware_infrastructure_setup/vcenter_driver.html#vcenterc-image>`.
* **VM actions** can be specified relative to the VM start scheduled :onedoc:`actions <operation/vm_management/vm_instances.html#vm-guide2-scheduling-actions>`, for example: terminate this VM after a month of being created.
* **Automatic selection of Virtual Networks for VM NICs**, balance network usage at deployment time or reduce clutter in your VM Template list. More info :onedoc:`here <operation/network_management/manage_vnets.html#vgg-vm-vnets>`.
* **New self-provisioning model for networks**, :onedoc:`Virtual Network Templates <operation/network_management/vn_templates.html#vn-templates>`. Users can now instantiate their own virtual networks from predefined templates with their own addressing.
* **Support for NIC Alias**, VM’s can have more than one IP associated to the same network interface. More info :onedoc:`here <operation/network_management/manage_vnets.html#vgg-vn-alias>`.

Multiple bugfixes and documentation improvements have been included in this version. The complete list of changes can be checked on the `development portal <https://github.com/OpenNebula/one/milestone/9?closed=1>`__.

vOneCloud 3.4 has been certified with :ref:`support for vSphere 6.0, 6.5 and 6.7 <system_requirements>`.

.. warning:: Upgrade from versions prior to 3.0 cannot be performed automatically. If you hold an active support subscription, please `contact OpenNebula Systems <mailto:support@opennebula.systems&subject="Upgrade to vOneCloud 3.0">`__ to schedule a vOneCloud upgrade.
