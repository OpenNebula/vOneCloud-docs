.. _migrate_virtual_machines:
 
==========================
Migrating Virtual Machines
==========================

vOneCloud allows migration of VMs between different vCenter clusters (ie, vOneCloud hosts) and/or different datastores. Depending on the type of migration (cold, the VM is powered off, or saved; or live, the VM is migrated while running), or the target (cluster and/or datastore), several requirements needs to be met in order to migrate the machine.

Migrating a VM Between vCenter Clusters (vOneCloud Hosts)
---------------------------------------------------------

Requirements (both live and cold migrations)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Every Network attached to the selected VMs need to exists in both vCenter clusters and OpenNebula clusters
* Every Datastore that is used by the VM need to exist in both vCenter clusters and OpenNebula clusters
* Target OpenNebula host can specify a ESX_MIGRATION_LIST attribute:
    - If not specified, target ESX host is not explicitly declared and migration may fail
    - If set to an empty string (""), OpenNebula will randomly chose a target ESX from all the ESXs that belong to the vCenter target cluster
    - If set to a space-separated list of ESX hostnames (that need to beling to the vCenter target cluster), OpenNebula will randomly chose a target ESX from the list

.. Note:: A good place to check if the VM meets the OpenNebula requirements is to peep into the 'AUTOMATIC_REQUIREMENTS' attribute of the Virtual Machine (this can be reviewed in the Template info tab) and check if it includes the target OpenNebula clusters (remember, a cluster in OpenNebula is a collection of hosts, virtual networks and datastores, a cluster in vCenter is represented as a host in OpenNebula).

Requirements (only live migrations)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* vMotion interface enabled in both vCenter clusters (otherwise the driver will warn about compatibility issues)
* OpenNebula live migration only works for running VMs so be sure to check the state before

Migrating a VM Between Datastores
---------------------------------------------------------

On a VM migration, target datastore can be changed. Disks belonging to the VM will be migrated to the target datastore. This is useful for rebalancing resources usage among datastores.

Requirements (both cold and live migrations)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Every Datastore that is used by the VM needs to exist in both vCenter clusters and OpenNebula clusters


Usage
-----

Different migration types are triggered through the migration buttons:

.. image:: /images/migrate_buttons.png
    :align: center

Select a destination host in the emerging dialog. If you need to migrate to a different datastore, simply select the same host and click on "Advanced Options" to select a target datastre:

.. image:: /images/migrate_dialog.png
    :align: center
