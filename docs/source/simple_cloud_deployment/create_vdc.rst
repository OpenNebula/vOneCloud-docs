.. _create_vdc:

===========================
Create a Virtual Datacenter
===========================

The provisioning model by default in vOneCloud is based on three different :ref:`roles <user_groups>` using three different web :ref:`interfaces <interfaces>`.

*vOneCloud* user comes pre configured and is the **Cloud Administrator**, in full control of all the physical and virtual resources and using the vCenter view.

A Virtual Datacenter (VDC) defines an assignment of one or several groups to a pool of physical resources. This pool of physical resources consists of resources from one or several clusters, which are logical groups of hosts, virtual networks and datastores, which can be shared between VDCs. VDCs are a great way to partition your cloud into smaller clouds, and assign them to groups with their administrators and users, completely isolated from other groups.

A **Group Admin** manages her partition of the cloud, including user management, but only within the VDCs assigned to the Group, not for the whole cloud like the **Cloud Administrator**.

Let's create a Group (under System) named *Production* with an administrator called **prodadmin**:

.. image:: /images/create_vdc_adminview.png
    :align: center

Let's create a VDCs (under System) named *ProductionVDC*, and assign the *Production* group to use it:

.. image:: /images/create_prod_vdc.png
    :align: center

Let's add resources to the VDC under the "Resources" tab, for instance a vCenter instance and a Virtual Network:

.. image:: /images/assign_resources_to_vdc.png
    :align: center

Now login again using the newly created **prodadmin**. The Group Admin view will kick in. Try it out creating the first *produser* and assign them quotas on resource usage:

.. image:: /images/create_vdc_vdcview.png
    :align: center

As *vOneCloud* user, in the vCenter View, you will be able to see all the VM Templates that have been automatically created when importing the vCenter infrastructure. You can assign any of these VM Templates to the VDC by assigned them to the Group associated to the VDC:

.. image:: /images/create_vdc_change_template.png
    :align: center

The same applies for Virtual Networks these VM Templates may use.

If you log with *produser*, the view will change to the vCenter Cloud View, where **vdcuser** can start consuming VMs based on the VM Template shared by the **Cloud Administrator** and allowed by the **vdcadmin**:

.. image:: /images/create_vdc_cloudview.png
    :align: center

Read more about :doc:`Group <operation/users_groups_management/manage_groups.html>` and :doc:`VDC <operation/users_groups_management/manage_vdcs.html>` managing.
