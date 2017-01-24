
.. _system_requirements:

===================
System Requirements
===================

.. warning:: It is advised to manage one vCenter by only one vOneCloud (ie, do not manage the same vCenter from two different vOneClouds). Otherwise VMs from both server will clash and produce errors.

The following components are needed to be present in the infrastructure to implement a cloud infrastructure run by vOneCloud:

+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|    **Component**    |                                                                                                                                                             **Observations**                                                                                                                                                             |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vCenter 5.5 and 6.0 | - ESX hosts, VM Templates and Running VMs expected to be managed by vOneCloud needs to be grouped into clusters                                                                                                                                                                                                                          |
|                     | - The IP or DNS needs to be known, as well as the credentials (username and password) of an :onedoc:`admin user <deployment/node_installation/vcenter_node_installation.html>`.                                                                                                                                                          |
|                     | - DRS is not required but it is recommended. vOneCloud does not schedule to the granularity of ESX hosts, and you would need DRS to select the actual ESX host within the cluster. Otherwise the VM will be started in the ESX host associated to the VM Template                                                                        |
|                     | - Ideally, all ESX belonging to the same vCenter cluster to be exposed to vOneCloud need to share at least one datastore among them, although this is not a hard requirement.                                                                                                                                                            |
|                     | - VMs that will be instantiated through vOneCloud need to be saved as VMs Templates in vCenter. vOneCloud only creates new VMs by instantiating VM Templates.                                                                                                                                                                            |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ESX 5.5 and 6.0     | - With at least 2 GB of free RAM and 1 free CPU                                                                                                                                                                                                                                                                                          |
|                     | - To enable VNC functionality from vOneCloud there are two requirements: 1) the ESX hosts need to be reachable from vOneCloud and 2) the ESX firewall should allow for VNC connections (see the note below)                                                                                                                              |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Guest OS            | - VMware tools are needed in the guestOS to enable several features (contextualization and networking feedback). Please install `VMware Tools (for Windows) <https://www.vmware.com/support/ws55/doc/new_guest_tools_ws.html>`__ or `Open Virtual Machine Tools <https://github.com/vmware/open-vm-tools>`__ (for \*nix) in the guestOS. |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. note:: To enable VNC functionality for vOneCloud, repeat the following procedure for each ESX:

   - In the vSphere client proceed to Home -> Inventory -> Hosts and Clusters
   - Select the ESX host, Configuration tab and select Security Profile in the Software category.
   - In the Firewall section, select Edit. Enable GDB Server, then click OK.

   Make sure that the ESX hosts are reachable from vOneCloud.

vOneCloud ships with a default of 2 CPUs and 2 GB of RAM, and as such it has been certified for infrastructures of the following dimensions:

- Up to 4 vCenters
- Up to 40 ESXs managed by each vCenter
- Up to 1.000 VMs in total, each vCenter managing up to 250 VMs
- Up to 100 users, being the concurrent limit 10 users accessing the system simultaneously

.. note:: For infrastructures exceeding the aforementioned limits, we recommend an installation of OpenNebula from scratch on a bare metal server, using the :onedoc:`vCenter drivers <deployment/vmware_infrastructure_setup/vcenter_driver.html>`
