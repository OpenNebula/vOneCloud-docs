.. _accounting_monitoring:

=======================
Accounting & Monitoring
=======================

vOneCloud is constantly monitoring the infrastructure and the users to keep track of the resource consumption. The objective is twofold, being able to have a clear picture of the infrastructure to aid in the resource scheduling, as well as being able to enforce :ref:`resource quotas <resource_quotas>` and give accounting information.

The monitoring subsystem gathers information relative to hosts and virtual machines, such as host and VM status, basic performance indicators and capacity consumption. vOneCloud comes preconfigured to retrieve such information directly from vCenter. You can learn more on the monitoring subsystem `here <http://docs.opennebula.org/4.10/administration/monitoring/mon.html>`__.

Using the information form the monitoring subsystem, vOneCloud is able to provide accounting information, both in text and graphically. An administrator can see the consumption of a particular user or group in terms of hours of CPU consumed, or total memory used in a given time window. Thus information is useful to feed a chargeback or billing platform. 

|accounting_image|

.. |accounting_image| image:: /images/accounting_admin_view.png
