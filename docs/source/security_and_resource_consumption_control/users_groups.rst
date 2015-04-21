.. _user_groups:

======================
Users, Groups and ACLs
======================

vOneCloud offers a powerful mechanism for managing, grouping and assigning roles to users. Permissions and Access Control List mechanisms ensures the ability to allow or forbid access to any resource controlled by vOneCloud, being physical or virtual.

.. _users_and_roles:

User & Roles
------------

vOneCloud can manage different types of users, attending to the permissions they have over infrastructure and logical resources.

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

Learn more about user management :doc:`here <administration/users_and_groups/manage_users.html>`.

.. _vdc_management:

Group & VDC Management
----------------------

A **group** of users makes it possible to isolate users and resources. A user can see and use the shared resources from other users. The **group** is an authorization boundary for the users, but you can also partition your cloud infrastructure and define what resources are available to each group using Virtual Data Centers (VDC).

A VDC defines an assignment of one or several groups to a pool of physical resources. This pool of physical resources consists of resources from one or several clusters, which are logical agroupations of hosts and virtual networks. VDCs are a great way to partition your cloud into smaller clouds, and asign them to groups with their administrators and users, completely isolated from other groups.

.. image:: /images/sunstone_group_list.png
    :align: center

Read more about :doc:`groups <administration/users_and_groups/manage_groups.html>` and :doc:`VDCs <administration/users_and_groups/manage_groups.html#managing-vdc-and-resource-providers>`.

Access Control Lists
--------------------

vOneCloud implements a very useful ACL mechanism that enables fine-tuning of allowed operations for any user, or group of users. Each operation generates an authorization request that is checked against the registered set of ACL rules. There are predefined ACLs that implements default behaviors (like VDC isolation), but they can be altered by the cloud administrator.

.. image:: /images/sunstone_acl_list.png
    :align: center

Writing (or even reading) ACL rules is not trivial, more information about :doc:`ACLs here <administration/users_and_groups/manage_acl.html>`.

