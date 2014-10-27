.. _features:

==================
vOneCloud Features
==================

.. _features_outofthebox:

vOneCloud leverages the functionality of OpenNebula. The following features come preconfigured and can be used **out-of-the-box** with vOneCloud:

* **Cloud User Interfaces**

  * AWS EC2 and EBS APIs
  * Simple, clean, intuitive portals for cloud consumers and VDC admins

* **On-demand Provision of Virtual Data Centers** 
  * Dynamic creation of Virtual Data Centers (VDCs) as fully-isolated virtual infrastructure environments where a group of users, under the control of the VDC administrator, can create and manage compute, storage and networking capacity
  * Placement of VDCs to multiple vCenters

* **Hybrid Cloud and Federation**
  * Cloud-bursting of VMs to public clouds
  * Federation of multiple OpenNebula Zones for scalability, isolation or multiple-site support

* **Fast Provisioning**
  * VM and service (multi-VM apps) templates
  * Automatic provision of VM and service (multi-VM apps) from a catalog
  * Automatic execution and scaling of multi-tiered applications 
  * Snapshotting 

* **Security and Resource Consumption Control**
  * Resource Quota Management to track and limit computing, storage and networking resource utilization
  * Integration with user management services like LDAP, Active Directory…
  * Fine-grained accounting and monitoring
  * Complete isolated VDCs and organizations
  * Fine-grained ACLs and user quotas
  * Powerful user, group and role management

* **Cloud Admin Interfaces**
  * Powerful CLI that resembles typical UNIX commands applications
  * SunStone Portal for administrators and advanced users



* `Standard Cloud Interfaces and Simple Provisioning Portal for Cloud Consumers <http://docs.opennebula.org/4.10/release_notes/release_notes/features.html#standard-cloud-interfaces-and-simple-provisioning-portal-for-cloud-consumers>`__. AWS EC2 and EBS APIs. Simple, clean, intuitive portals for cloud consumers and VDC admins.

* `On-demand Provision of Virtual Data Centers <http://docs.opennebula.org/4.10/release_notes/release_notes/features.html#on-demand-provision-of-virtual-data-centers>`__. Dynamic creation of Virtual Data Centers (VDCs) as fully-isolated virtual infrastructure environments where a group of users, under the control of the VDC administrator, can create and manage compute, storage and networking capacity. Placement of VDCs to multiple vCenters

* `Hybrid Cloud Computing and Cloud Bursting <http://docs.opennebula.org/4.10/release_notes/release_notes/features.html#hybrid-cloud-computing-and-cloud-bursting>`__. Cloud-bursting of VMs to public clouds. Federation of multiple OpenNebula Zones for scalability, isolation or multiple-site support.

* **Fast Provisioning**. VM and service (multi-VM apps) templates. Automatic provision of VM and service (multi-VM apps) from a catalog. Snapshotting

* `Management of Multi-tier Applications <http://docs.opennebula.org/4.10/release_notes/release_notes/features.html#management-of-multi-tier-applications>`__. Execution of multi-tiered applications with automatic scaling, write elasticity rules using selected key performance indicators from the hypervisor or `from the application <http://docs.opennebula.org/4.10/release_notes/release_notes/features.html#gain-insight-into-cloud-applications>`__.

* **Security and Resource Consumption Control**

  * `Complete isolated VDCs and organizations <http://docs.opennebula.org/4.10/release_notes/release_notes/features.html#advanced-multi-tenancy-with-group-management>`__. Create and group users, and their access to infrastructure resources.
  * Resource Quota Management to track and limit computing, storage and networking resource utilization
  * Integration with user management services like LDAP, Active Directory…
  * Fine-grained accounting and monitoring
  * Fine-grained ACLs and user quotas
  * Powerful user, group and role management

* **Cloud Admin Interfaces** 

  * Powerful CLI that resembles typical UNIX commands applications
  * Sunstone Portal for administrators and advanced users

* `Reliability, Efficiency and Massive Scalability <http://docs.opennebula.org/4.10/release_notes/release_notes/features.html#reliability-efficiency-and-massive-scalability>`__. Leverage years of testing and production use, and be sure that your Cloud Mangement Platform will be up to the task.

* `Support for Auth Backends <http://docs.opennebula.org/4.10/release_notes/release_notes/features.html#powerful-user-security-management>`__. Secure your Cloud infrastructure with different authorization and authentication mechanisms and backends.

.. _features_advanceconf:

vOneCloud can levarage all the functionality that OpenNebula delivers, but some of it needs **additional configuration** steps:

* `Centralized Management of Multiple Zones <http://docs.opennebula.org/4.10/release_notes/release_notes/features.html#centralized-management-of-multiple-zones>`__. Federate different datancenters by joining several vOneCloud instances.

* `Community Virtual Appliance Marketplace <http://docs.opennebula.org/4.10/release_notes/release_notes/features.html#community-virtual-appliance-marketplace>`__. Benefit from community contributions with an online catalog of ready-to-run virtual appliances.

* `Broad Commodity and Enterprise Platform Support <http://docs.opennebula.org/4.10/release_notes/release_notes/features.html#broad-commodity-and-enterprise-platform-support>`__. Underlying OpenNebula software features an amazingly flexible and plugin oriented architecture that eases the integration with existing datacenter components. Do no reinvent your datacenter, evolve it!.

* `Virtual <http://docs.opennebula.org/4.10/release_notes/release_notes/features.html#advanced-control-and-monitoring-of-virtual-infrastructure>`__ & `Physical <http://docs.opennebula.org/4.10/release_notes/release_notes/features.html#advanced-control-and-monitoring-of-physical-infrastructure>`__ Infrastructure Control. Manage all aspects of your physical (hypervisors, storage backends, etc) & virtualized (VM lifecycle, VM images, virtual networks, etc) from a centralized web interface (Sunstone).

Although the configuration is tailored for vCenter infrastructures, all the power of OpenNebula is contained in vOneCloud and it can be unleashed!
