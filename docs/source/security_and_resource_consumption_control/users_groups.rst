.. _user_groups:

=============================
Users, Roles, Groups and ACLs
=============================

vOneCloud offers a powerful mechanism for managing users, grouping them and asing roles to them. A powerful permissions and Access Control List mechanisms ensures the ability to allow or forbid access to any resource controlled by vOneCloud, being physical or virtual

User & Roles
------------

vOneCloud can manage different types of users, attending to the permissions they have over infrastructure and logical resources:

- **Cloud Administrators**, with enough privileges to perform any operation on any object.
- **Infrastructure User**, accounts may access most of the functionality to manage resources.
- **VDC Administrators** accounts manage a limited set of resources and users.
- **VDC Users** access a simplified Sunstone view with limited actions to create new VMs, and perform basic life cycle operations.
- **Public users** can only access OpenNebula through a public API, but can not access the xml-rpc API directly.

Learn more about user management `here <http://docs.opennebula.org/4.10/administration/users_and_groups/manage_users.html>`__.

Group & VDC Management
----------------------

A `group <http://docs.opennebula.org/4.10/administration/users_and_groups/manage_groups.html>`__ in vOneCloud is an authorization boundary for users, but it can also be used to partition the cloud infrastructure and define what resources are available to each group.

A resource provider is a set of physical hosts and associated datastores and virtual networks, which is logically grouped into a cluster. When you assign a resource provider to a group, users in that group will be able to use the Datastores and Virtual Networks of that cluster.

A group and an associated resource provider forms a Virtual Datacenter (VDC). Read more about them `here <http://docs.opennebula.org/4.10/administration/users_and_groups/manage_groups.html#managing-vdc-and-resource-providers>`__. VDCs are a great way to partition your cloud into smaller clouds, with their administrator and users, completely isolated from other VDCs.

Access Control Lists
--------------------

vOneCloud implements a very useful `ACL mechanism <http://docs.opennebula.org/4.10/administration/users_and_groups/manage_acl.html>`__. The ACL authorization system enables fine-tuning of allowed operations for any user, or group of users. Each operation generates an authorization request that is checked against the registered set of ACL rules. There are predefined ACLs that implements default behaviors (like VDC isolation), but they can be altered by the cloud administrator.
