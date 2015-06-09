.. _resource_pool:

========================
Resource Pool Confinment
========================

vCenter credentials of the user that vOneCloud is configured with to access the vCenter clusters can be confined into a Resource Pool, to allow only a fraction of the vCenter infrastructure to be used by vOneCloud users. The steps to confine vOneCloud users into a Resource Pool are:

 - Create a new vCenter user
 - Create a Resource Pool in vCenter and assign the subset of Datacenter hardware resources wanted to be exposed through vOneCloud
 - Give vCenter user Resource Pool Administration rights over the Resource Pool
 - Give vCenter user Resource Pool Administration (or equivalent) over the Datastores the VMs are going to be running on

 Afterwards, these credentials can be used to add to vOneCloud the host representing the vCenter cluster. Add a new tag called VCENTER_RESOURCE_POOL to the host template representing the vCenter cluster (for instance, in the info tab of the host, or in the CLI), with the name of the Resource Pool. All the VMs created through vOneCloud would be confined to this Resource Pool.

 .. note:: Remember to modify the VCENTER_PASSWORD tag as well, since after the VCENTER_RESOURCE_POOL update it will get double encrypted. This :ref:`limitation <limitations>` will be addressed in future releases of vOneCloud.

 .. image:: /images/vcenter_rp.png
    :width: 90%
    :align: center


