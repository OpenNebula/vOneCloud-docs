.. _accounting_monitoring:

=======================
Accounting & Monitoring
=======================

vOneCloud is constantly monitoring the infrastructure resources to keep track of resource consumption. The objective is twofold: being able to have a clear picture of the infrastructure to aid in the resource scheduling, as well as being able to enforce :ref:`resource quotas <resource_quotas>` and give accounting information.

The monitoring subsystem gathers information relative to hosts and virtual machines, such as host and VM status, basic performance indicators and capacity consumption. vOneCloud comes preconfigured to retrieve such information directly from vCenter.

Using the information form the monitoring subsystem, vOneCloud is able to provide accounting information, both in text and graphically. An administrator can see the consumption of a particular user or group in terms of hours of CPU consumed, or total memory used in a given time window. This information is useful to feed a chargeback or billing platform.

Accounting information is available from the vCenter View:

.. image:: /images/accounting_vcenter_view.png
    :align: center

From the Group Admin View:

.. image:: /images/accounting_vdcadmin_view.png
    :align: center

And from the vCenter Cloud View:

.. image:: /images/accounting_cloud_view.png
    :align: center

Learn more on the :doc:`monitoring <administration/monitoring/mon.html>` and :doc:`accounting <administration/users_and_groups/accounting.html>` subsystems
