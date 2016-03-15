.. _import_vcenter:

=======================
Import Existing vCenter
=======================

Importing a vCenter infrastructure into vOneCloud can be carried out easily through the Sunstone Web UI. Follow the next steps to import an existing vCenter as well as any already defined VM Template and Networks.

You will need the IP or hostname of the vCenter server, as well as an administrator credentials to successfuly import resources from vCenter.

Step 1. Sunstone login
-----------------------

Log in into Sunstone as **CloudAdmin**, as explained in :ref:`the previous section <download_and_deploy>`.

.. _acquire_resources:

Step 2. Acquire vCenter Resources
---------------------------------

In Sunstone, proceed to the ``Infrastructure --> Hosts`` tab and click on the "+" green icon.

.. image:: /images/import_cluster.png
    :align: center

.. warning:: vOneCloud does not currently support spaces in vCenter cluster names

In the dialog that pops up, select vCenter as Type in the dropdown. You now need to fill in the data according to the following table:

+--------------+------------------------------------------------------+
| **Hostname** | vCenter hostname (FQDN) or IP address                |
+--------------+------------------------------------------------------+
| **User**     | Username of a vCenter user with administrator rights |
+--------------+------------------------------------------------------+
| **Password** | Password for the above user                          |
+--------------+------------------------------------------------------+

.. image:: /images/vcenter_create.png
    :align: center

After the vCenter cluster is selected in Step 2, a paginated list of vCenter VM Templates and both Networks and Distributed vSwitches will be presented to be imported into vOneCloud. Select all the Templates, Networks and Distributed vSwitches you want to import, and vOneCloud will generate vOneCloud VM Template and Virtual Networks resources representing the vCenter VM templates and vCenter Networks and Distributed vSwitches respectively.

.. _cluster_prefix:

Networks, Distributes vSwitches and VM Templates resources imported from vCenter will have their names appended with a the name of the cluster where this resources belong in vCenter, to ease their identification within vOneCloud.

.. _operations_on_templates:

These vOneCloud VM templates can be modified selecting the VM Template in ``Virtual Resources --> Templates`` and clicking on the Update button, so the resulting VMs are adjusted to user needs. Among other options available through the Sunstone web interface:

- Information can be passed into the instantiated VM, through either :ref:`Contextualization or Customization <guest_configuration>`.
- Network interface cards can be added to give VMs access to different networks
- Capacity (MEMORY and CPU) can be modified
- VNC capabilities can be enabled

.. _name_suffix_note:

.. note:: VMs instantiated through vOneCloud will be named in vCenter as 'one-<vid>-<VM Name>', where <vid> is the id of the VM and VM Name is the name given to the VM in vOneCloud. This value can be changed using a special attribute set in the vCenter cluster representation in vOneCloud, ie, the OpenNebula host. This attribute is called "VM_PREFIX", and will evaluate one variable, $i, to the id of the VM. A value of "one-$i-" in that parameter would have the same behaviour as the default. This attribute can be set in the "Attributes" section of the vOneCloud host, in the info panel that shows after clicking on the desire host.

Also, Virtual Networks can be further refined with the inclusion of different :doc:`Address Ranges <user/virtual_resource_management/vgg.html#the-address-range-ar>`. This refinement can be done at import time, defining the size of the network one of the following supported Address Ranges:

- IPv4: Need to define at least starting IP address. MAC address can be defined as well
- IPv6: Can optionally define starting MAC adddress, GLOBAL PREFIX and ULA PREFIX
- Ethernet: Does not manage IP addresses but rather MAC addresses. If a starting MAC is not provided, vOneCloud will generate one.

The networking information will also be passed onto the VM in the :ref:`Contextualization <build_template_context>` process.

.. _vmtemplates_and_networks:

Regarding the vCenter VM Templates and Networks, is important to take into account:

- vCenter **VM Templates with already defined NICs** that reference Networks in vCenter will be imported without this information in vOneCloud. These NICs will be invisible for vOneCloud, and therefore cannot be detached from the Virtual Machines. The imported Templates in vOneCloud can be updated to add NICs from Virtual Networks imported from vCenter (being Networks or Distributed vSwitches).

- We recommend therefore to use **VM Templates in vCenter without defined NICs**, to add them later on in the vOneCloud VM Templates

.. _import_running_vms:

(Optional) Step 3. Import / Reacquire Virtual Machines, VM Templates and Networks
---------------------------------------------------------------------------------

If the vCenter infrastructure has running (or powered off) Virtual Machines, vOneCloud can import and subsequently manage them. To import vCenter VMs, proceed to the  WILDS tab in the Host info tab representing the vCenter cluster where the VMs are running in, select the VMs to be imported and click on the import button.

.. image:: /images/import_wild_vms.png
    :width: 90%
    :align: center

.. _operations_on_running_vms:

After the VMs are in the Running state, you can operate on their lifecycle, assign them to particular users, attach or detach network interfaces, create snapshots, do capacity resizing (change CPU and MEMORY after powering the VMs off), etc. All the funcionality that vOneCloud supports for regular VMs is present for imported VMs.

.. note:: This ability to import VMs also applies to hybrid hosts, it is possible through this same machanism to import VMs from SoftLayer, Azure and EC2.

Running VMs with open VNC ports are imported with the ability to stablish VNC connection to them via vOneCloud. To activate the VNC ports, you need to right click on the VM while it is shut down and click on "Edit Settings", and set the ``remotedisplay.*`` settings show in the following images.

.. image:: /images/vm_advanced_settings.png
    :align: center

.. image:: /images/set_vnc_port.png
    :align: center

The following operations *cannot* be performed on an imported VM:

- Delete --recreate
- Undeploy (and Undeploy --hard)
- Migrate (and Migrate --live)
- Stop

vCenter VM Templates can be imported and reacquired using the ``Import`` button in ``Virtual Resources --> Templates``. Fill in the credentials and the IP or hostname of vCenter and click on the "Get Templates" button. Similarly, Networks and Distributed vSwitches can also be imported / reacquired from using a similar ``Import`` button in ``Infrastructure --> Virtual Networks``.

.. image:: /images/import_vcenter_templates.png
    :align: center

.. note:: The vCenter VM Templates, Networks, Distributed vSwitches and running Virtual Machines can be imported regardless of their position inside VM Folders, since vOneCloud will search recursively for them.

Step 4. Check Resources
-----------------------

Now it's time to check that the vCenter import has been succesful. In ``Infrastructure --> Hosts`` check vCenter has been imported, and if all the ESX hosts are available:

.. note:: Take into account that one vCenter cluster (with all its ESX hosts) will be represented as one vOneCloud host.

.. image:: /images/import_vcenter_esx_view.png
    :align: center

Step 5. Instantiate a VM Template
---------------------------------

Everything is ready! Now vOneCloud is prepared to manage Virtual Machines. In Sunstone, go to ``Virtual Resources --> Templates``, select one of the templates imported in **Step 2** and click on Instantiate. Now you will be able to control the lifecycle of the VM.

More information on available operations over VMs :doc:`here <user/virtual_resource_management/vm_guide_2.html>`.
