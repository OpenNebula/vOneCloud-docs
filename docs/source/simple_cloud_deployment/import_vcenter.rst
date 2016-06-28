.. _import_vcenter:

=======================
Import Existing vCenter
=======================

Importing a vCenter infrastructure into vOneCloud can be carried out easily through the Sunstone Web UI. Follow the next steps to import an existing vCenter as well as any already defined VM Template and Networks.

You will need the IP or hostname of the vCenter server, as well as an administrator credentials to successfully import resources from vCenter.

Step 1. Sunstone login
-----------------------

Log in into Sunstone as **CloudAdmin**, as explained in :ref:`the previous section <download_and_deploy>`.

.. _acquire_resources:

Step 2. Acquire vCenter Resources
---------------------------------

To import new vCenter clusters to be managed in voneCloud, proceed in Sunstone to the ``Infrastructure --> Hosts`` tab and click on the "+" green icon.

.. image:: /images/import_cluster.png
    :align: center

.. warning:: vOneCloud does not support spaces in vCenter cluster names.

In the dialog that pops up, select vCenter as Type in the drop-down. You now need to fill in the data according to the following table:

+--------------+------------------------------------------------------+
| **Hostname** | vCenter hostname (FQDN) or IP address                |
+--------------+------------------------------------------------------+
| **User**     | Username of a vCenter user with administrator rights |
+--------------+------------------------------------------------------+
| **Password** | Password for the above user                          |
+--------------+------------------------------------------------------+

.. image:: /images/vcenter_create.png
    :align: center

.. _import_running_vms:

Step 3. Import / Reacquire vCenter Resources
---------------------------------------------------------------------------------

**Existing VMs**

If the vCenter infrastructure has running or powered off **Virtual Machines**, vOneCloud can import and subsequently manage them. To import vCenter VMs, proceed to the  WILDS tab in the Host info tab representing the vCenter cluster where the VMs are running in, select the VMs to be imported and click on the import button.

.. image:: /images/import_wild_vms.png
    :width: 90%
    :align: center

.. _operations_on_running_vms:

After the VMs are in the Running state, you can operate on their life-cycle, assign them to particular users, attach or detach network interfaces, create snapshots, do capacity resizing (change CPU and MEMORY after powering the VMs off), etc. All the funcionality that vOneCloud supports for regular VMs is present for imported VMs.

.. note:: This ability to import VMs also applies to hybrid hosts, it is possible through this same machanism to import VMs from SoftLayer, Azure and EC2.

Running VMs with open VNC ports are imported with the ability to stablish VNC connection to them via vOneCloud. To activate the VNC ports, you need to right click on the VM while it is shut down and click on "Edit Settings", and set the ``remotedisplay.*`` settings show in the following images.

.. image:: /images/vm_advanced_settings.png
    :align: center

.. image:: /images/set_vnc_port.png
    :align: center

The following operations *cannot* be performed on an imported VM:

- Recover --recreate
- Undeploy (and Undeploy --hard)
- Migrate (and Migrate --live)
- Stop

**VM Templates**

vCenter **VM Templates** can be imported and reacquired using the ``Import`` button in ``Virtual Resources --> Templates``. Fill in the credentials and the IP or hostname of vCenter and click on the "Get Templates" button. 

.. image:: /images/import_vcenter_templates.png
    :align: center

.. _operations_on_templates:

These vOneCloud VM templates can be modified selecting the VM Template in ``Virtual Resources --> Templates`` and clicking on the Update button, so the resulting VMs are adjusted to user needs. Among other options available through the Sunstone web interface:

- Information can be passed into the instantiated VM, through either :ref:`Contextualization or Customization <guest_configuration>`.
- Network interface cards can be added to give VMs access to different networks
- Capacity (MEMORY and CPU) can be modified
- VNC capabilities can be disabled

.. _name_prefix_note:

.. note:: VMs instantiated through vOneCloud will be named in vCenter as 'one-<vid>-<VM Name>', where <vid> is the id of the VM and VM Name is the name given to the VM in vOneCloud. This value can be changed using a special attribute set in the vCenter cluster representation in vOneCloud, ie, the vOneCloud host. This attribute is called "VM_PREFIX", and will evaluate one variable, $i, to the id of the VM. A value of "one-$i-" in that parameter would have the same behaviour as the default. This attribute can be set in the "Attributes" section of the vOneCloud host, in the info panel that shows after clicking on the desire host.

.. _vmtemplates_and_networks:

Regarding the vCenter VM Templates and Networks, is important to take into account:

- vCenter **VM Templates with already defined NICs** that reference Networks in vCenter will be imported without this information in vOneCloud. These NICs will be invisible for vOneCloud, and therefore cannot be detached from the Virtual Machines. The imported Templates in vOneCloud can be updated to add NICs from Virtual Networks imported from vCenter (being Networks or Distributed vSwitches).

- We recommend therefore to use **VM Templates in vCenter without defined NICs**, to add them later on in the vOneCloud VM Templates

**Networks**

Similarly, **Networks** and Distributed vSwitches can also be imported / reacquired from using a similar ``Import`` button in ``Infrastructure --> Virtual Networks``. 

Virtual Networks can be further refined with the inclusion of different :doc:`Address Ranges <operation/network_management/manage_vnets.html#address-space>`. This refinement can be done at import time, defining the size of the network one of the following supported Address Ranges:

- IPv4: Need to define at least starting IP address. MAC address can be defined as well
- IPv6: Can optionally define starting MAC address, GLOBAL PREFIX and ULA PREFIX
- Ethernet: Does not manage IP addresses but rather MAC addresses. If a starting MAC is not provided, vOneCloud will generate one.

The networking information will also be passed onto the VM in the :ref:`Contextualization <build_template_context>` process.

.. _import_images_and_ds:

**Datastores and Images**

Datastores and VMDK images can be imported / reacquired from the ``Storage --> Datastores`` and ``Storage --> Images`` respectively.

Datastore will be monitored for free space and availability. Images can be used for:

- disk attach/detach on VMs
- enrich VM Templates to add additional disks or CDROMs

.. _cluster_prefix:

.. note:: Resources imported from vCenter will have their names appended with a the name of the cluster where this resources belong in vCenter, to ease their identification within vOneCloud.

.. note:: vCenter VM Templates, Networks, Distributed vSwitches, Datastores, VMDKs and Virtual Machines can be imported regardless of their position inside VM Folders, since vOneCloud will search recursively for them.

Step 4. Check Resources
-----------------------

Now it's time to check that the vCenter import has been successful. In ``Infrastructure --> Hosts`` check vCenter has been imported, and if all the ESX hosts are available.

.. note:: Take into account that one vCenter cluster (with all its ESX hosts) will be represented as one vOneCloud host.

.. image:: /images/import_vcenter_esx_view.png
    :align: center

Step 5. Instantiate a VM Template
---------------------------------

Everything is ready! Now vOneCloud is prepared to manage Virtual Machines. In Sunstone, go to ``Virtual Resources --> Templates``, select one of the templates imported in **Step 3** and click on Instantiate. Now you will be able to control the life cycle of the VM.

More information on available operations over VMs :doc:`here <operation/vm_management/vm_instances.html>`.
