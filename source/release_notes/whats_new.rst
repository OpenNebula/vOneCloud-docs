.. _whats_new:

========================
What's New vOneCloud 3.2
========================

vOneCloud 3.2 is powered by OpenNebula 5.6 'Blue Flash', and, as such, includes functionality present in :onedoc:`Blue Flash <intro_release_notes/release_notes/index.html>` relevant to vOneCloud:

* **Revamped import mechanism**, vOneCloud Sunstone :ref:`import <import_vcenter>` of vCenter resources has been greatly streamlined.
* **Overall driver performance**, all operations, specially monitoring, run quicker and consuming less resources.
* **VNC options for Wild VMs**, now they can be defined at :ref:`import <import_vcenter>` time to avoid collisions.
* **Network creation reworked**, with more admin feedback in the :ref:`network representation <vcenter_enhanced_networking>`.
* **Migrate VMs between clusters**, now is possible to migrate VMs between different vCenter clusters from voneCloud.
* **Marketplace**, vOneCloud users and admins can now enjoy the OpenNebula Systems public and private :ref:`marketplaces <marketplace>` to easily download new appliances.
* **Docker integration**, :onedoc:`easily build a Docker fabric <advanced_components/applications_containerization/index.html>` using vOneCloud.
* **Schedule periodic actions**, now with time relative to VM creation. Check the VM Template creation dialog for options.

Multiple bugfixes and documentation improvements have been included in this version. The complete list of changes can be checked on the `development portal <https://github.com/OpenNebula/one/milestone/4?closed=1>`__.

vOneCloud 3.2 has been certified with :ref:`support for vSphere 5.5, 6.0 and 6.5 <system_requirements>`.

.. warning:: Upgrade from versions prior to 3.0 cannot be performed automatically. If you hold an active support subscription, please `contact OpenNebula Systems <mailto:support@opennebula.systems&subject="Upgrade to vOneCloud 3.0">`__ to schedule a vOneCloud upgrade.
