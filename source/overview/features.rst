.. _features:

================================================================================
vOneCloud Features
================================================================================

.. _features_outofthebox:

vOneCloud leverages the :onedoc:`functionality of OpenNebula <intro_release_notes/concepts_terminology/key_features.html>`. The following features come pre-configured and can be used out-of-the-box with vOneCloud:

* **Cloud User Interfaces**

  * Simple, clean, intuitive portals for cloud consumers and Virtual Datacenter (VDC) administrators.

* **Cloud Admin Interfaces**

  * Sunstone Portal for administrators and advanced users
  * Powerful CLI that resembles typical UNIX commands applications

* **Import Existing Resources**

  * Import existing vCenter VM Templates
  * Import existing vCenter Networks and Distributed vSwitches
  * Import existing running and powered off Virtual Machines
  * Import existing Datastores and VMDK images
  * Import existing Storage Pods

* **On-demand Provision of Virtual Data Centers**

  * Dynamic creation of Virtual Data Centers (VDCs) as fully-isolated virtual infrastructure environments where a group of users, under the control of the group administrator, can create and manage compute capacity
  * Placement of VDCs to multiple vCenters
  * Resource Pool Confinement, restrict vOneCloud users/groups to a subset of hardware specified by a Resource Pool

* **Fast Provisioning**

  * Automatic provision of Virtual Machines and Services (Multi-VM applications) from a Template catalog
  * VM Template cloning and editing capabilities to maintain Template catalog
  * Automatic execution and scaling of multi-tiered applications
  * Snapshot management
  * Contextualization capabilities, including the ability to run any script at VM boot time
  * VM capacity resizing (CPU and Memory)
  * Full networking support: vCenter Network and Distributed vSwitch import and creation
  * Full storage support: non persistent images and volatile disks
  * Connect Virtual Networks using a Virtual Router
  * Attach/detach network interfaces functionality
  * VNC connection to VMs, including the ability to set keymap
  * Attach/detach disk functionality
  * Save a running VM as a VM Template
  * Disk resize at boot time and in poweroff state
  * Migrate VMs between vCenter clusters
  * Migrate VMs between vCenter datastores

* **Virtualization Management**

  * Folder management
  * Limit and monitor VM network and disk consumption
  * Linked clone support
  * Import VM Templates with network and storage information
  * Chose datastore and Resource Pool where VMs will be deployed to
  * Instantiate to persistent to easily create a VM Template catalog
  * Marketplace support

* **Docker provisioning**

  * Create Docker engines
  * Integration with Docker Machine

* **Security and Resource Consumption Control**

  * Resource Quota Management to track and limit computing resource utilization
  * Fine-grained accounting and monitoring
  * Complete isolated VDCs and organizations
  * Fine-grained ACLs and user quotas
  * Powerful user, group and role management
  * Showback functionality to report resource usage cost

* **Enterprise Datacenter Component Integration Capabilities**

  * Integration with user management services like Active Directory and LDAP.
  * HTTP Proxy support

* **Reliability, Efficiency and Massive Scalability**

  * Profit from years of testing and production use
  * Be sure that your Cloud Management Platform will be up to the task

vOneCloud additionally brings new configuration and upgrade tools:

* **Appliance and Services Configuration**

  * Control Console for vOneCloud appliance configuration
  * Control Panel (Web UI) for vOneCloud services configuration and debugging

* **Smooth Upgrade Process**

  * Automatic upgrade process and notifications through the Control Panel available for users with an active support subscription

If you feel that there is a particular feature interesting for the general public, feel free to add a feature request in `Community - Feature Request section of the vOneCloud Support Portal <https://support.vonecloud.com/hc/communities/public/topics/200215442-Community-Feature-Requests>`__.

.. _features_advanceconf:

If you are building a large-scale cloud, are interested in the federation of multiple controller instances, or want to integrate with third party components, customize the product or manage open source hypervisors, we recommend an installation of `OpenNebula <http://opennebula.org>`__.
