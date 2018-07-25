.. _import_vcenter:

=======================
Import Existing vCenter
=======================

Importing a vCenter infrastructure into vOneCloud can be carried out easily through the Sunstone Web UI. Follow the next steps to import an existing vCenter cluster as well as any already defined VM Template and Networks.

You will need the IP or hostname of the vCenter server, as well as a user declared as Administrator in vCenter.

Alternatively, in some enterprise environments declaring the user as Administrator is not allowed, in that case, you will need to grant the following permissions to a user depending on what OpenNebula's functionality you want to enable:

+---------------------------------------------+----------------------------------------------------------------------------+
|                  Privileges                 |                       Notes                                                |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Interact.DeviceConnection    | Required by a virtual machine reconfigure action                           |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Interact.SetCDMedia          | Required by a virtual machine reconfigure action                           |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Interact.SetFloppyMedia      | Required by a virtual machine reconfigure action                           |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Config.Rename                | Required by a virtual machine reconfigure action                           |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Config.Annotation            | Required by a virtual machine reconfigure action                           |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Config.AddExistingDisk       | Required by a virtual machine reconfigure action                           |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Config.AddNewDisk            | Required by a virtual machine reconfigure action                           |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Config.RemoveDisk            | Required by a virtual machine reconfigure action                           |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Config.CPUCount              | Required by a virtual machine reconfigure action                           |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Config.Memory                | Required by a virtual machine reconfigure action                           |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Config.RawDevice             | Required by a virtual machine reconfigure action                           |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Config.AddRemoveDevice       | Required by a virtual machine reconfigure action                           |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Config.Settings              | Required by a virtual machine reconfigure action                           |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Config.AdvancedConfig        | Required by a virtual machine reconfigure action                           |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Config.SwapPlacement         | Required by a virtual machine reconfigure action                           |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Config.HostUSBDevice         | Required by a virtual machine reconfigure action                           |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Config.DiskExtend            | Required by a virtual machine reconfigure action                           |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Config.ChangeTracking        | Required by a virtual machine reconfigure action                           |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Provisioning.ReadCustSpecs   | Required by a virtual machine reconfigure action                           |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Inventory.CreateFromExisting | Required by a virtual machine reconfigure action                           |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Inventory.CreateNew          | Required by a virtual machine reconfigure action                           |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Inventory.Move               | Required by a virtual machine reconfigure action                           |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Inventory.Register           | Required by a virtual machine reconfigure action                           |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Inventory.Remove             | Required by a virtual machine reconfigure action                           |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Inventory.Unregister         | Required by a virtual machine reconfigure action                           |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Inventory.Delete             | Required to delete a virtual machine                                       |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Provisioning.DeployTemplate  | Required to deploy a virtual machine from a particular template            |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Provisioning.CloneTemplate   | Required to create a copy of a particular template                         |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Interact.PowerOn             | Required to power on a virtual machine                                     |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Interact.PowerOff            | Required to power off or shutdown a virtual machine                        |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Interact.Suspend             | Required to suspend a virtual machine                                      |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Interact.Reset               | Required to reset/reboot a VM's guest Operating System                     |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.Inventory.Delete             | Required to delete a virtual machine or template                           |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.State.CreateSnapshot         | Required to create a new snapshot of a virtual machine.                    |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.State.RemoveSnapshot         | Required to remove snapshots from a virtual machine                        |
+---------------------------------------------+----------------------------------------------------------------------------+
| VirtualMachine.State.RevertToSnapshot       | Required to revert a virtual machine to a particular snapshot              |
+---------------------------------------------+----------------------------------------------------------------------------+
| Resource.AssignVirtualMachineToResourcePool | Required to assign a resource pool to a virtual machine                    |
+---------------------------------------------+----------------------------------------------------------------------------+
| Resource.ApplyRecommendation                | On all Storage Pods (Storage DRS cluster) represented by OpenNebula        |
+---------------------------------------------+----------------------------------------------------------------------------+
| Datastore.AllocateSpace                     | On all VMFS datastores represented by OpenNebula                           |
+---------------------------------------------+----------------------------------------------------------------------------+
| Datastore.LowLevelFileOperations            | On all VMFS datastores represented by OpenNebula                           |
+---------------------------------------------+----------------------------------------------------------------------------+
| Datastore.RemoveFile                        | On all VMFS datastores represented by OpenNebula                           |
+---------------------------------------------+----------------------------------------------------------------------------+
| Datastore.Browse                            | On all VMFS datastores represented by OpenNebula                           |
+---------------------------------------------+----------------------------------------------------------------------------+
| Datastore.FileManagement                    | On all VMFS datastores represented by OpenNebula                           |
+---------------------------------------------+----------------------------------------------------------------------------+
| Network.Assign                              | Required on any network the Virtual Machine will be connected to           |
+---------------------------------------------+----------------------------------------------------------------------------+
| System.Read                                 | Required to rename Uplink port group for a distributed switch only if you  |
|                                             | want OpenNebula to create distributed virtual switches.                    |
+---------------------------------------------+----------------------------------------------------------------------------+
| Host.Config.Network                         | Required an all **ESX hosts** where you want OpenNebula to create, update  |
|                                             | or delete virtual switches and port groups                                 |
+---------------------------------------------+----------------------------------------------------------------------------+
| DVSwitch.CanUse                             | Required to connect a VirtualEthernetAdapter to a distributed virtual      |
|                                             | switch either it was created in vSphere or created by OpenNebula           |
+---------------------------------------------+----------------------------------------------------------------------------+
| DVSwitch.Create                             | Required if you want OpenNebula to create distributed virtual switches     |
+---------------------------------------------+----------------------------------------------------------------------------+
| DVSwitch.HostOp                             | Required if you want OpenNebula to create distributed virtual switches     |
+---------------------------------------------+----------------------------------------------------------------------------+
| DVSwitch.PortSetting                        | Required if you want OpenNebula to create distributed virtual switches     |
+---------------------------------------------+----------------------------------------------------------------------------+
| DVSwitch.Modify                             | Required if you want OpenNebula to create distributed virtual switches     |
+---------------------------------------------+----------------------------------------------------------------------------+
| DVSwitch.Delete                             | Required if you want OpenNebula to destroy a distributed virtual switches  |
|                                             | that was previously created by OpenNebula.                                 |
+---------------------------------------------+----------------------------------------------------------------------------+
| DVPortgroup.Create                          | Required if you want OpenNebula to create distributed port groups          |
+---------------------------------------------+----------------------------------------------------------------------------+
| DVPortgroup.CanUse                          | Required to connect a VirtualEthernetAdapter to a distributed virtual port |
|                                             | group either it was created in vSphere or created by OpenNebula            |
+---------------------------------------------+----------------------------------------------------------------------------+
| DVSwitch.Modify                             | Required if you want OpenNebula to create distributed port groups          |
+---------------------------------------------+----------------------------------------------------------------------------+
| DVPortgroup.Delete                          | Required if you want OpenNebula to destroy a distributed port group that   |
|                                             | was previously created by OpenNebula.                                      |
+---------------------------------------------+----------------------------------------------------------------------------+

.. note:: For security reasons, you may define different users to access different ESX Clusters. A different user can be defined in OpenNebula per ESX cluster, which is encapsulated in OpenNebula as an OpenNebula host.

Step 1. Sunstone login
-----------------------

Log in into Sunstone as **CloudAdmin**, as explained in :ref:`the previous section <download_and_deploy>`.

The *CloudAdmin* user comes pre configured and is the **Cloud Administrator**, in full control of all the physical and virtual resources and using the vCenter view. Views will be explained later in its own section.


.. _acquire_resources:

Step 2. Acquire vCenter Resources
---------------------------------

To import new vCenter clusters to be managed in vOneCloud, proceed in Sunstone to the ``Infrastructure --> Hosts`` tab and click on the "+" green icon.

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

Now it's time to check that the vCenter import has been successful. In ``Infrastructure --> Hosts`` check if vCenter cluster has been imported, and if all the ESX hosts are available in the ESX tab.

.. note:: Take into account that one vCenter cluster (with all its ESX hosts) will be represented as one vOneCloud host.

.. image:: /images/import_vcenter_esx_view.png
    :align: center

Step 3. Import / Reacquire vCenter Resources
---------------------------------------------------------------------------------

**Existing VMs**

If the vCenter infrastructure has running or powered off **Virtual Machines**, vOneCloud can import and subsequently manage them. To import vCenter VMs, proceed to the **Wilds** tab in the Host info tab representing the vCenter cluster where the VMs are running in, select the VMs to be imported and click on the import button.

.. image:: /images/import_wild_vms.png
    :width: 90%
    :align: center

.. _operations_on_running_vms:

After the VMs are in the Running state, you can operate on their life-cycle, assign them to particular users, attach or detach network interfaces, create snapshots, do capacity resizing (change CPU and MEMORY after powering the VMs off), etc.

All the funcionality that vOneCloud supports for regular VMs is present for imported VMs with some exceptions. The following operations *cannot* be performed on an imported VM:

- Recover --recreate
- Undeploy (and Undeploy --hard)
- Migrate (and Migrate --live)
- Stop


Once a Wild VM is imported, vOneCloud will reconfigure the vCenter VM so VNC connections can be established once the VM is monitored.

.. _import_images_and_ds:

**Datastores and Images**

Datastores and VMDK images can be imported / reacquired from the ``Storage --> Datastores`` and ``Storage --> Images`` respectively. Since datastores are going to be used to hold the images from VM Templates, all datastore **must** be imported before VM Template import.

vCenter datastores hosts VMDK files and other file types so VMs and templates can use them, and these datastores can be represented in OpenNebula as both an Images datastore and a System datastore:

- Images Datastore. Stores the images repository. VMDK files are represented as OpenNebula images stored in this datastore.
- System Datastore. Holds disk for running virtual machines, copied or cloned from the Images Datastore.

For example, if we have a vcenter datastore called ''nfs'', when we import the vCenter datastore into OpenNebula, two OpenNebula datastores will be created as an Images datastore and as a System datastore pointing to the same vCenter datastore.

.. note:: If the vCenter instance features a read only datastore, please be aware that you should disable the SYSTEM representation of the datastore after importing it to avoid OpenNebula trying to deploy VMs in it.

When an image or a datastore is imported, vOneCloud will generate a name automatically that prevents conflicts if you try to import several files with the same name but that are located in different folders inside the datastore, or try to import datastores with the same name in different vCenter instances. The image name contains the file’s name, the datastore’s name and a 12 character hash, whereas the datastore contains the datastore name, the vcenter instance name, the datacenter where it lives and the datastore type between parentheses. These names can be changed once the image or datastore has been imported. 

When the vCenter hypervisor is used we have three OpenNebula image types:

- OS: A bootable disk Image. Every VM template must define one DISK referring to an Image of this type. These images can be imported or :onedoc:`uploaded<deployment/vmware_infrastructure_setup/datastore_setup.html#vcenter-upload-vmdk>`.
- CDROM: These Images are read-only data. These images can also be imported or :onedoc:`uploaded<deployment/vmware_infrastructure_setup/datastore_setup.html#vcenter-upload-iso>`.
- DATABLOCK: A datablock Image is a storage for data. These Images can be created from previous existing data (e.g uploading a VMDK file), or as an :onedoc:`empty drive<deployment/vmware_infrastructure_setup/datastore_setup.html#vcenter-create-datablock>`.

OpenNebula images can be also classified in persistent and non-persistent images:

- Non-persistent images. These images are used by at least one VM. It can still be used by other VMs. When a new VM using a non-persistent image is deployed a copy of the VMDK file is created.
- Persistent images. A persistent image can be use only by a VM. It cannot be used by new VMs. The original file is used, no copies are created.

Disks attached to a VM will be backed by a non-persistent or persistent image although volatile disks are also supported. Volatile disks are created on-the-fly on the target hosts and they are disposed when the VM is shutdown.

Datastore will be monitored for free space and availability. Images can be used for:

- disk attach/detach on VMs
- enrich VM Templates to add additional disks or CDROMs

.. _import_vm_templates:

**VM Templates**

.. warning:: Since datastores are going to be used to hold the images from VM Templates, all datastore **must** be imported before VM Template import.

In vOneCloud, Virtual Machines are deployed from VMware VM Templates that must exist previously in vCenter and must be imported into vOneCloud. There is a one-to-one relationship between each VMware VM Template and the equivalent vOneCloud VM Template. Users will then instantiate the OpenNebula VM Template and OpenNebula will create a Virtual Machine clone from the vCenter template.

vCenter **VM Templates** can be imported and reacquired using the ``Import`` button in ``Virtual Resources --> Templates``. Fill in the credentials and the IP or hostname of vCenter and click on the "Get Templates" button.

.. image:: /images/import_vcenter_templates.png
    :align: center

.. _operations_on_templates:
.. _vmtemplates_and_networks:

When a VMware VM Template is imported, vOneCloud will detect any virtual disk and network interface within the template. For each virtual disk, vOneCloud will create an vOneCloud image representing each disk discovered in the template. In the same way, vOneCloud will create a network representation for each standard or distributed port group associated to virtual network interfaces found in the template. The imported vOneCloud VM templates can be modified selecting the VM Template in ``Virtual Resources --> Templates`` and clicking on the Update button, so the resulting VMs are adjusted to user needs. 

Among other options available through the Sunstone web interface:

- Information can be passed into the instantiated VM, through either :ref:`Contextualization or Customization <guest_configuration>`
- Network interface cards can be added or removed to give VMs access to different networks
- Disks can be added or removed
- Capacity (MEMORY and CPU) can be modified
- VNC capabilities can be disabled

Check the :ref:`advanced features guide<add_new_vcenter>` for additional features available for VM Templates.

.. _name_prefix_note:

.. note:: VMs instantiated through vOneCloud will be named in vCenter as 'one-<vid>-<VM Name>', where <vid> is the id of the VM and VM Name is the name given to the VM in vOneCloud. This value can be changed using a special attribute set in the vCenter cluster representation in vOneCloud, ie, the vOneCloud host. This attribute is called "VM_PREFIX", and will evaluate one variable, $i, to the id of the VM. A value of "one-$i-" in that parameter would have the same behaviour as the default. This attribute can be set in the "Attributes" section of the vOneCloud host, in the info panel that shows after clicking on the desire host.

.. note:: After a VM Template is cloned and booted into a vCenter Cluster it can access VMware advanced features and it can be managed through the OpenNebula provisioning portal -to control the life-cycle, add/remove NICs, make snapshots- or through vCenter (e.g. to move the VM to another datastore or migrate it to another ESX). OpenNebula will poll vCenter to detect these changes and update its internal representation accordingly.

.. note:: The name assigned to the template in OpenNebula contains the template’s name, vCenter cluster’s name and a 12 character hash. That name is used to prevent conflicts when several templates with the same name are found in a vCenter instance. Once the vCenter template has been imported, that OpenNebula’s name can be changed to a more human-friendly name.

.. _import_networks:

**Networks**

Similarly, **Networks** and Distributed vSwitches can also be imported / reacquired from using a similar ``Import`` button in ``Infrastructure --> Virtual Networks``.

Virtual Networks can be further refined with the inclusion of different :onedoc:`Address Ranges <operation/network_management/manage_vnets.html#address-space>`. This refinement can be done at import time, defining the size of the network one of the following supported Address Ranges:

- IPv4: Need to define at least starting IP address. MAC address can be defined as well
- IPv6: Can optionally define starting MAC address, GLOBAL PREFIX and ULA PREFIX
- Ethernet: Does not manage IP addresses but rather MAC addresses. If a starting MAC is not provided, vOneCloud will generate one.

The networking information will also be passed onto the VM in the :ref:`Contextualization <build_template_context>` process.

It is possible to limit the bandwidth of any VM NIC associated to a particular virtual network by using the Inbound/Outbound Traffic QoS values as seen in the next image.

.. image:: /images/limit_network_bw.png
    :align: center

.. _cluster_prefix:

.. note:: vOneCloud does not support spaces in VMDKs paths nor names.

.. note:: Resources imported from vCenter will have their names appended with a the name of the cluster where this resources belong in vCenter, to ease their identification within vOneCloud.

.. note:: vCenter VM Templates, Networks, Distributed vSwitches, Datastores, VMDKs and Virtual Machines can be imported regardless of their position inside VM Folders, since vOneCloud will search recursively for them.

Step 4. Instantiate a VM Template
---------------------------------

Everything is ready! Now vOneCloud is prepared to manage Virtual Machines. In Sunstone, go to ``Virtual Resources --> Templates``, select one of the templates imported in **Step 3** and click on Instantiate. Now you will be able to control the life cycle of the VM.

More information on available operations over VMs :onedoc:`here <operation/vm_management/vm_instances.html>`.
