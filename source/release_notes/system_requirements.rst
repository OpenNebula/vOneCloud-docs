
.. _system_requirements:

===================
System Requirements
===================

.. warning:: It is advised to manage one vCenter by only one vOneCloud (ie, do not manage the same vCenter from two different vOneClouds). Otherwise VMs from both server will clash and produce errors.

The following components are needed to be present in the infrastructure to implement a cloud infrastructure run by vOneCloud:

+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|             **Component**             |                                                                                                                                                             **Observations**                                                                                                                                                             |
+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vCenter 5.5/6.0/6.5                   | - ESX hosts, VM Templates and Running VMs expected to be managed by vOneCloud needs to be grouped into clusters                                                                                                                                                                                                                          |
|                                       | - The IP or DNS needs to be known, as well as the credentials (username and password) of an :onedoc:`admin user <deployment/node_installation/vcenter_node_installation.html>`.                                                                                                                                                          |
|                                       | - DRS is not required but it is recommended. vOneCloud does not schedule to the granularity of ESX hosts, and you would need DRS to select the actual ESX host within the cluster. Otherwise the VM will be started in the ESX host associated to the VM Template                                                                        |
|                                       | - Ideally, all ESX belonging to the same vCenter cluster to be exposed to vOneCloud need to share at least one datastore among them, although this is not a hard requirement.                                                                                                                                                            |
|                                       | - VMs that will be instantiated through vOneCloud need to be saved as VMs Templates in vCenter. vOneCloud only creates new VMs by instantiating VM Templates.                                                                                                                                                                            |
+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ESX 5.5/6.0/6.5                       | - With at least 2 GB of free RAM and 1 free CPU                                                                                                                                                                                                                                                                                          |
|                                       | - To enable VNC functionality from vOneCloud there are two requirements: 1) the ESX hosts need to be reachable from vOneCloud and 2) the ESX firewall should allow for VNC connections (see the note below)                                                                                                                              |
+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Guest OS                              | - VMware tools are needed in the guestOS to enable several features (contextualization and networking feedback). Please install `VMware Tools (for Windows) <https://www.vmware.com/support/ws55/doc/new_guest_tools_ws.html>`__ or `Open Virtual Machine Tools <https://github.com/vmware/open-vm-tools>`__ (for \*nix) in the guestOS. |
+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| IE (>= 9), Firefox (> 3.5) and Chrome | Other browsers, including Safari, are **not** supported and may not work well. Note that IE11 is NOT supported with compatibility mode enabled.                                                                                                                                                                                          |
+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. note:: To enable VNC functionality for vOneCloud, repeat the following procedure for each ESX. The following package adds the VNC ruleset (port range 5900-65535) and permits access to these ports.

   - `ZIP <https://downloads.opennebula.org/packages/opennebula-5.4.0/fw-vnc-5.4.0.zip>`__
   - `VIB <https://downloads.opennebula.org/packages/opennebula-5.4.0/fw-vnc-5.4.0.vib>`__

   * Allow custom VIB package to be installed (in the vSphere client)

     * Login the vSphere client
     * Go to Home -> Inventories -> Hosts and Clusters
     * Select the ESX host and its tab **Manage** or **Configure** (depends on the vSphere version)
     * Select **Security Profile** in the **System category**
     * At the very bottom, select edit on **Host Image Profile Acceptance Level**
     * Switch to **Community Supported** and confirm with **OK**

   .. image:: /images/vcenter_acceptance_level.png
       :width: 50%
       :align: center

   * Install VIB package (in the ESX host UI)

     * Login the ESX host UI
     * Go to Help -> Update in top right corner
     * Provide the VIB URL or absolute local path and click on **Update**

   .. image:: /images/vcenter_install_vib.png
       :width: 50%
       :align: center

   * Restrict VNC access to the OpenNebula Front-end only (in the vSphere client)

     * Go back again to the ESX host details in the vSphere client
     * Reload the vSphere page to see current data
     * Check again **Security Profile** in the **System category**, look on the Firewall/Incoming Connections for new **VNC** item
     * Click on **Edit** for the Firewall
     * Find the VNC and optionally restrict access only to your OpenNebula Front-end (e.g. for 192.168.0.1):

   .. image:: /images/vcenter_enable_vnc.png
       :width: 90%
       :align: center

   Also, make sure that the ESX hosts are reachable from vOneCloud.

vOneCloud ships with a default of 2 CPUs and 2 GB of RAM, and as such it has been certified for infrastructures of the following dimensions:

- Up to 4 vCenters
- Up to 40 ESXs managed by each vCenter
- Up to 1.000 VMs in total, each vCenter managing up to 250 VMs
- Up to 100 users, being the concurrent limit 10 users accessing the system simultaneously

.. note:: For infrastructures exceeding the aforementioned limits, we recommend an installation of OpenNebula from scratch on a bare metal server, using the :onedoc:`vCenter drivers <deployment/vmware_infrastructure_setup/vcenter_driver.html>`
