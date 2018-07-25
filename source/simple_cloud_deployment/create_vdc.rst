.. _create_vdc:

===========================
Create a Virtual Datacenter
===========================

A Virtual Datacenter (VDC) defines an assignment of a pool of physical resources to one or several groups of users. This pool consists of logical groups of hosts, virtual networks and datastores from one or several clusters, which can be shared between VDCs. VDCs are a great way to partition your cloud into smaller clouds, and assign them to groups with their administrators and users, completely isolated from other groups.

A **Group Admin** manages her partition of the cloud, including user management, but only within the VDCs assigned to the Group.

Let's create a Group (under System) named *Production* with an administrator called **prodadmin**:

.. image:: /images/create_vdc_adminview.png
    :align: center

Let's create a VDCs (under System) named *ProductionVDC*, and assign the *Production* group to use it:

.. image:: /images/create_prod_vdc.png
    :align: center

Let's add resources to the VDC under the "Resources" tab, for instance a vCenter instance and a Virtual Network:

.. image:: /images/assign_resources_to_vdc.png
    :align: center

Now login again using the newly created **prodadmin**. The Group Admin view will kick in (views will be explained later in its own section.). Try it out creating the first *produser* and assign them quotas on resource usage:

.. image:: /images/create_vdc_vdcview.png
    :align: center

As the *CloudAdmin* user, in the vCenter View, you will be able to see all the VM Templates that have been automatically created when importing the vCenter infrastructure. You can assign any of these VM Templates to the VDC by assigned them to the Group associated to the VDC:

.. image:: /images/create_vdc_change_template.png
    :align: center

The same applies for Virtual Networks these VM Templates may use.

If you log with *produser*, the view will change to the vCenter Cloud View, where you can start consuming VMs based on the VM Template shared by the **Cloud Administrator** and allowed by the **prodadmin**:

.. image:: /images/create_vdc_cloudview.png
    :align: center

Read more about :onedoc:`Group <operation/users_groups_management/manage_groups.html>` and :onedoc:`VDC <operation/users_groups_management/manage_vdcs.html>` managing.
