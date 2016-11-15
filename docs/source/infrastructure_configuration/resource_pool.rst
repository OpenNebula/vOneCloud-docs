.. _resource_pool:

================================================================================
Resource Pool Confinement
================================================================================

vOneCloud can be configured to place VMs in different Resource Pools. There are two approaches to achieve this, fixed per Cluster basis or flexible per VM Template basis.

Per Cluster Basis
-----------------

In the fixed per Cluster basis approach, the vCenter credentials that vOneCloud use can be confined into a Resource Pool, to allow only a fraction of the vCenter infrastructure to be used by vOneCloud users. The steps to confine vOneCloud users into a Resource Pool are:

- Create a new vCenter user
- Create a Resource Pool in vCenter and assign the subset of Datacenter hardware resources wanted to be exposed through vOneCloud
- Give vCenter user Resource Pool Administration rights over the Resource Pool
- Give vCenter user Resource Pool Administration (or equivalent) over the Datastores where the VMs are going to be running on

Afterwards, these credentials can be used to add to vOneCloud the host representing the vCenter cluster. Add a new attribute called VCENTER_RESOURCE_POOL to the host template representing the vCenter cluster (for instance, in the info tab of the host, or in the CLI), with the name of the Resource Pool.

.. image:: /images/vcenter_rp.png
   :width: 90%
   :align: center

Per VM Template Basis
---------------------

This second approach is more flexible in the sense that all Resource Pools defined in vCenter can be used, and the mechanism to select which one the VM is going to reside into can be defined using the attribute RESOURCE_POOL in the PUBLIC_CLOUD section of vOneCloud VM Template. This mechanism can be used to generate different vOneCloud VM Templates pointing to the same vCenter VM Template, each confined in a different Resource Pool and subject to be assigned to different groups of users.

This attribute can be set in two ways in the vOneCloud VM Template, and can be set/modified at the time of creating/updating the VM Template in vOneCloud:

* **Fixed**: Pick a certain Resource Pool where this VM will be contained
* **Delegated to User**: Provide a comma separated list of the different Resource Pools available for this VM Template, that the end user will be able to chose at VM launch time. A default can be selected.


.. image:: /images/select_rp_vm_template_update.png
   :width: 90%
   :align: center

Nested Resource Pools can be represented using '/'. For instance, a Resource Pool "RPChild" nested under "RPAncestor" can be represented both in VCENTER_RESOURCE_POOL and RESOURCE_POOL attributes as "RPAncestor/RPChild".

.. code::

    RESOURCE_POOL="RPAncestor/RPChild"
    PUBLIC_CLOUD=[
      HOST="Cluster",
      TYPE="vcenter",
      VM_TEMPLATE="4223067b-ed9b-8f73-82ba-b1a98c3ff96e" ]
