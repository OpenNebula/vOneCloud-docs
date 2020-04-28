

vOneCloud implements a powerful permissions, quotas and ACLs mechanisms to control which users and groups are allowed to use which physical and virtual resources, keeping a record of the comsumption of these resources as well as monitoring their state periodically.

.. _multitenancy:

=============
Multi Tenancy
=============

OpenNebula offers a powerful mechanism for managing, grouping and assigning roles to groups of users, ensuring they use of a slice of the cloud in a fully automated manner. Permissions and Access Control List mechanisms ensures the ability to allow or forbid access to any resource controlled by OpenNebula, being physical or virtual.

OpenNebula keeps also a record of the consumption of these resources as well as monitoring their state periodically.

User & Roles
------------

OpenNebula can manage different types of users, attending to the permissions they have over infrastructure and logical resources.

+----------------------+-----------------------------------------------------------------+------------+
|    **User Type**     |                         **Permissions**                         |  **View**  |
+----------------------+-----------------------------------------------------------------+------------+
| Cloud Administrators | enough privileges to perform any operation on any object        | vcenter    |
+----------------------+-----------------------------------------------------------------+------------+
| Group Administrators | manage a limited set and users within VDCs                      | groupadmin |
+----------------------+-----------------------------------------------------------------+------------+
| End Users            | access a simplified view with limited actions to create new VMs | cloud      |
+----------------------+-----------------------------------------------------------------+------------+

.. note:: VDC is the acronym for Virtual Datacenter

.. image:: /images/sunstone_user_list.png
    :align: center

Learn more about user management :onedoc:`here <operation/users_groups_management/manage_users.html>`.

.. _vdc_management:

Group & VDC Management
----------------------

A **group** of users makes it possible to isolate users and resources. A user can see and use the shared resources from other users. The **group** is an authorization boundary for the users, but you can also partition your cloud infrastructure and define what resources are available to each group using Virtual Data Centers (VDC).

A VDC defines an assignment of one or several groups to a pool of physical resources. This pool of physical resources consists of resources from one or several clusters, which are logical groups of hosts and virtual networks. VDCs are a great way to partition your cloud into smaller clouds, and assign them to groups with their administrators and users, completely isolated from other groups.

.. image:: /images/sunstone_group_list.png
    :align: center

Read more about :onedoc:`groups <operation/users_groups_management/manage_groups.html>` and :onedoc:`VDCs <operation/users_groups_management/manage_vdcs.html>`.

Access Control Lists
--------------------

vOneCloud implements a very useful ACL mechanism that enables fine-tuning of allowed operations for any user, or group of users. Each operation generates an authorization request that is checked against the registered set of ACL rules. There are predefined ACLs that implements default behaviors (like VDC isolation), but they can be altered by the cloud administrator.

.. image:: /images/sunstone_acl_list.png
    :align: center

Writing (or even reading) ACL rules is not trivial, more information about :onedoc:`ACLs here <operation/users_groups_management/chmod.html#managing-acl-rules>`.

Accounting & Monitoring
-----------------------

OpenNebula is constantly monitoring the infrastructure resources to keep track of resource consumption. The objective is twofold: being able to have a clear picture of the infrastructure to aid in the resource scheduling, as well as being able to enforce :ref:resource quotas and give accounting information.

The monitoring subsystem gathers information relative to hosts and virtual machines, such as host and VM status, basic performance indicators and capacity consumption. OpenNebula comes preconfigured to retrieve such information directly from vCenter.

Using the information form the monitoring subsystem, OpenNebula is able to provide accounting information, both in text and graphically. An administrator can see the consumption of a particular user or group in terms of hours of CPU consumed, or total memory used in a given time window. This information is useful to feed a chargeback or billing platform.

.. image:: /images/accounting_vcenter_view.png
    :align: center

Learn more on the :onedoc:`monitoring <deployment/open_cloud_host_setup/monitoring.html>` and :onedoc:`accounting <operation/users_groups_management/accounting.html>` subsystems.

Resource Quotas
---------------

OpenNebula quota system tracks user and group usage of system resources, allowing the cloud administrator to set limits on the usage of these resources.

Quota limits can be set for:

- **users**, to individually limit the usage made by a given user.
- **groups**, to limit the overall usage made by all the users in a given group.

Tracking the usage on:

- **Compute**: Limit the overall memory, CPU or VM instances

Quotas can be updated either from the vCenter View or from the Group Admin View.

.. image:: /images/sunstone_update_quota.png
    :align: center

Refer to :onedoc:`this guide <operation/users_groups_management/quota_auth.html>` to find out more.

Showback
--------

OpenNebula ships with functionality to report resource usage cost. Showback reports are generated daily (at midnight)using the information retrieved from OpenNebula.

**Set the VM Cost**

Each VM Template can optionally define a cost. The cost is defined as cost per CPU per hour, and cost per memory MB per hour. The cost units are abstract and their equivalent to monetary or other cost metrics have to be defined in each deployment.

This cost is defined per VM Template by the Cloud Administrator at the time of creating or updating a VM Template, applying a cost to the total Memory and CPU of the VMs that will be spawn from this VM Template.

.. image:: /images/set_template_cost.png
    :align: center


**Retrieve Monthly Reports**

Any user or administrator can see their monthly showback reports clicking on their user icon to access Settings.


.. image:: /images/get_to_settings.png
    :align: center

And clicking on the Showback tab, obtain the cost consumed by clicking on the "Get Showback"


.. image:: /images/show_showback.png
    :align: center

Learn more on the :onedoc:`Showback functionality <operation/users_groups_management/showback.html>`.
