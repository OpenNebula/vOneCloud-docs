.. _resource_quotas:

===============
Resource Quotas
===============

vOneCloud quota system tracks user and group usage of system resources, allowing the cloud administrator to set limits on the usage of these resources. 

Quota limits can be set for:

- **users**, to individually limit the usage made by a given user.
- **groups**, to limit the overall usage made by all the users in a given group. 

Tacking the usage on:

+------------+----------------------------------------------------------------------------------------+
| Datastores | Control the amount of storage capacity allocated to each user/group for each datastore |
+------------+----------------------------------------------------------------------------------------+
| Compute    | Limit the overall memory, cpu or VM instances                                          |
+------------+----------------------------------------------------------------------------------------+
| Network    | Limit the number of IPs a user/group can get from a given network                      |
+------------+----------------------------------------------------------------------------------------+
| Images     | Limit the how many VM instances from a given user/group are using a given image        |
+------------+----------------------------------------------------------------------------------------+

Quotas can be updated either from the vCenter View:

.. image:: /images/sunstone_update_quota.png
    :align: center

or from the VDC Admin View:

.. image:: /images/vdc_admin_update_quota.png
    :align: center

Writing (or even reading) ACL rules is not trivial. Please refer to `this guide <http://docs.opennebula.org/4.10/administration/users_and_groups/quota_auth.html>`__ to find out more.
