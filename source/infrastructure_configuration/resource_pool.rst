.. _resource_pool:

================================================================================
Resource Pool Confinement
================================================================================

vOneCloud can place VMs in different Resource Pools. There are two approaches to achieve this:

* fixed per Cluster basis
* flexible per VM Template basis.

Fixed per Cluster basis
================================================================================

In the fixed per Cluster basis approach, the vCenter connection that vOneCloud use can be confined into a Resource Pool, to allow only a fraction of the vCenter infrastructure to be used by vOneCloud users. The steps to confine vOneCloud users into a Resource Pool are:

* Create a new vCenter user.
* Create a Resource Pool in vCenter and assign the subset of Datacenter hardware resources wanted to be exposed through vOneCloud.
* Give vCenter user Resource Pool Administration rights over the Resource Pool.
* Give vCenter user Resource Pool Administration (or equivalent) over the Datastores the VMs are going to be running on.
* Import the vCenter cluster into vOneCloud as explained later. The import action will create an vOneCloud host.
* Add a new attribute called VCENTER_RESOURCE_POOL to vOneCloud's host template representing the vCenter cluster (for instance, in the info tab of the host, or in the CLI), with the reference to a Resource Pool.

.. image:: /images/vcenter_resource_pool_cluster.png
    :width: 50%
    :align: center


Flexible per VM Template
================================================================================

The second approach is more flexible in the sense that all Resource Pools defined in vCenter can be used, and the mechanism to select which one the VM is going to reside into can be defined using the attribute VCENTER_RESOURCE_POOL in the vOneCloud VM Template.

Once we have in vOneCloud an imported template, we can **update it** from the CLI or the Sunstone interface and we will have two choices:

* Specify a fixed Resource Pool that will be used by any VM based on the template.
* Offer a list of Resource Pools so the user can select one of them when a VM is instantiated.

Using the CLI we would use the **onetemplate update** command and we would add or edit the VCENTER_RESOURCE_POOL attribute.

If we want to specify a Resource Pool, that attribute would be placed inside the template and would contain a reference to the resource pool.

.. code::

    VCENTER_RESOURCE_POOL="TestResourcePool/NestedResourcePool"

If we wanted to offer a list to the user, we would place the VCENTER_RESOURCE_POOL attribute inside a USER_INPUT element, an it would contain a string that represents a list. Let's see an example:

.. code::

    USER_INPUTS=[
        VCENTER_RESOURCE_POOL="O|list|Which resource pool you want this VM to run in? |TestResourcePool/NestedResourcePool,TestResourcePool|TestResourcePool/NestedResourcePool" ]

The VCENTER_RESOURCE_POOL has the following elements:

* O: it means that it is optional to select a Resource Pool.
* list: this will be a list shown to users.
* Which resource pool you want this VM to run in?: that's the question that will be shown to users.
* TestResourcePool/NestedResourcePool,TestResourcePool: that's the list of Resource Pool references separeted with commas that are available to the user.
* TestResourcePool/NestedResourcePool: is the default Resource Pool that will be selected on the list.

.. note:: As we'll see later, the import tools provided by OpenNebula will create the VCENTER_RESOURCE_POOL attribute easily.

Using Sunstone we have the same actions described for the onevcenter tool.

If we want to specify a Resource Pool we should select Fixed from the Type drop-down menu and introduce the reference under Default Resource Pool:

.. image:: /images/vcenter_resource_pool_fixed_sunstone.png
    :width: 50%
    :align: center

If we wanted to offer a list to the user:

* We would select Provide on Instantiation from the Type drop-down menu.
* We would specify the default value that we want to be selected in the list.
* We would introduce the references of the Resource Pools that we want to include in the list, using a comma to separate values.

.. image:: /images/vcenter_resource_pool_list_sunstone.png
    :width: 50%
    :align: center


Referencing a Resource Pool
================================================================================

The VCENTER_RESOURCE_POOL attribute expects a string containing the name of the Resource Pool. If the Resource Pool is nested, the name of the Resource Pool should be preceeded by slashes and the names of the parent Resource Pools.

For instance, a Resource Pool "NestedResourcePool" nested under "TestResourcePool"

.. image:: /images/vcenter_resource_pool_nested.png
    :width: 35%
    :align: center

would be represented as "TestResourcePool/NestedResourcePool":

.. code::

    VCENTER_RESOURCE_POOL="TestResourcePool/NestedResourcePool"