.. _features:

==================
vOneCloud Features
==================

.. _features_outofthebox:

vOneCloud leverages the :doc:`functionality of OpenNebula <release_notes/release_notes/features.html>`. The following features come preconfigured and can be used **out-of-the-box** with vOneCloud:

* **Cloud User Interfaces**

  * Simple, clean, intuitive portals for cloud consumers and Virtual Datacenter (VDC) administrators.

* **Cloud Admin Interfaces**

  * SunStone Portal for administrators and advanced users
  * Powerful CLI that resembles typical UNIX commands applications

* **Import Existing Resources**

  * Import existing vCenter VM Templates
  * Import existing vCenter Networks and Distributed vSwitches
  * Import existing running Virtual Machines

* **On-demand Provision of Virtual Data Centers**

  * Dynamic creation of Virtual Data Centers (VDCs) as fully-isolated virtual infrastructure environments where a group of users, under the control of the group administrator, can create and manage compute capacity
  * Placement of VDCs to multiple vCenters

* **Hybrid Cloud**

  * Cloud-bursting of VMs to public clouds

* **Fast Provisioning**

  * Automatic provision of Virtual Machines and Services (Multi-VM applications) from a Template catalog
  * VM Template cloning and editing capabilities to maintain Template catalog
  * Automatic execution and scaling of multi-tiered applications
  * Snapshotting

* **Security and Resource Consumption Control**

  * Resource Quota Management to track and limit computing resource utilization
  * Fine-grained accounting and monitoring
  * Complete isolated VDCs and organizations
  * Fine-grained ACLs and user quotas
  * Powerful user, group and role management
  * vCenter Network and Distributed vSwitch support
  * Attach/detach network interfaces funcionality
  * Showback functionality to report resource usage cost

* **Enterprise Datacenter Component Integration Capabilities**

  * Integration with user management services like Active Directory and LDAP.
  * HTTP Proxy support

* **Reliability, Efficiency and Massive Scalability**

  * Profit from years of testing and production use
  * Be sure that your Cloud Mangement Platform will be up to the task
  
vOneCloud additionally brings new configuration and upgrade tools:
  
* **Appliance and Services Configuration**

  * Control Console for vOneCloud appliance configuration
  * Control Panel (Web UI) for vOneCloud services configuration and debugging

* **Smooth Upgrade Process**

  * Automatic upgrade process and notifications through the Control Panel available for users with an active support subscription 

If you feel that there is a particular feature interesting for the general public, feel free to add a feature request in `Community - Feature Request section of the vOneCloud Support Portal <https://support.vonecloud.com/hc/communities/public/topics/200215442-Community-Feature-Requests>`__.

.. _features_advanceconf:

vOneCloud can leverage all the functionality that OpenNebula delivers, but some of it needs **additional configuration** steps:

* :doc:`Centralized Management of Multiple Zones <release_notes/release_notes/features.html#centralized-management-of-multiple-zones>`. Federate different datacenters by joining several vOneCloud instances.

* :doc:`Community Virtual Appliance Marketplace <release_notes/release_notes/features.html#community-virtual-appliance-marketplace>`. Create your own marketplace or benefit from community contributions with an online catalog of ready-to-run virtual appliances.

* :doc:`Broad Commodity and Enterprise Platform Support <release_notes/release_notes/features.html#broad-commodity-and-enterprise-platform-support>`. Underlying OpenNebula software features an amazingly flexible and plugin oriented architecture that eases the integration with existing datacenter components. Do no reinvent your datacenter, evolve it!

* :doc:`Virtual <release_notes/release_notes/features.html#advanced-control-and-monitoring-of-virtual-infrastructure>` & :doc:`Physical <release_notes/release_notes/features.html#advanced-control-and-monitoring-of-physical-infrastructure>` Infrastructure Control. Manage all aspects of your physical (hypervisors, storage backends, etc) & virtualized (VM lifecycle, VM images, virtual networks, etc) from a centralized web interface (Sunstone).

Although the configuration is tailored for vCenter infrastructures, all the power of OpenNebula is contained in vOneCloud and it can be unleashed!
