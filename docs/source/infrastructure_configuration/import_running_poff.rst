.. _import_running_poffvms:
.. _import_vms:

==================================
Import Running and Powered Off VMs
==================================

**Running** and **Powered Off VMs** can be imported through the WILDS tab in the Host info tab representing the vCenter cluster where the VMs are running in.

.. image:: /images/import_wild_vms.png
    :width: 90%
    :align: center

VNC caoacibilities will be automatically add to imoported VMs.

In the ZOMBIES tab you'll find VMs that were launched from OpenNebula but, for whatever reason, OpenNebula is not aware of this, e.g coming from a different OpenNebula installation, or being managed from a different vOneCloud. Zombie VMs are meant to be a warning of a VM that need manual clean-up.

Read more about the :onedoc:`vCenter drivers <deployment/vmware_infrastructure_setup/vcenter_driver.html>`. Regarding the vCenter datastores in vOneCloud, refer to the :onedoc:`vCenter datastore guide <deployment/vmware_infrastructure_setup/datastore_setup.html>`
