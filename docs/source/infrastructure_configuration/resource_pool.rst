.. _resource_pool:

========================
Resource Pool Confinment
========================

vOneCloud can be configured to place VMs in different Resource Pools. There are two approachs to achieve this, fixed per Cluster basis or flexible per VM Template basis.

In the fixed per Cluster basis approach, the vCenter credentials that vOneCloud use can be confined into a Resource Pool, to allow only a fraction of the vCenter infrastructure to be used by vOneCloud users. The steps to confine vOneCloud users into a Resource Pool are:

- Create a new vCenter user
- Create a Resource Pool in vCenter and assign the subset of Datacenter hardware resources wanted to be exposed through vOneCloud
- Give vCenter user Resource Pool Administration rights over the Resource Pool
- Give vCenter user Resource Pool Administration (or equivalent) over the Datastores the VMs are going to be running on

Afterwards, these credentials can be used to add to vOneCloud the host representing the vCenter cluster. Add a new tag called VCENTER_RESOURCE_POOL to the host template representing the vCenter cluster (for instance, in the info tab of the host, or in the CLI), with the name of the Resource Pool.

.. image:: /images/vcenter_rp.png
   :width: 90%
   :align: center

The second approach is more flexible in the sense that all Resource Pools defined in vCenter can be used, and the mechanism to select which one the VM is going to reside into can be defined using the attribute RESOURCE_POOL in the PUBLIC_CLOUD section of vOneCloud VM Template.


TODO     - Add picture of RESOURCE_POOL selection in Sunstone


