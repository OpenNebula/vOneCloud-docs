.. _import_vcenter:

=================================
Import Existing vCenter Resources
=================================

Importing a vCenter infrastructure into OpenNebula can be carried out easily through the Sunstone Web UI. Follow the next steps to import an existing vCenter cluster as well as any already defined VM Template and Networks.

You will need the IP or hostname of the vCenter server, as well as a user declared as Administrator in vCenter. More information in the :onedoc:`main OpenNebula documentation <deployment/node_installation/vcenter_node_installation.html#permissions-requirement>`.


.. note:: For security reasons, you may define different users to access different ESX Clusters. A different user can be defined in OpenNebula per ESX cluster, which is encapsulated in OpenNebula as an OpenNebula host.

Step 1. Sunstone login
-----------------------

Log in into Sunstone as **oneadmin**, as explained in :ref:`the previous section <download_and_deploy>`.

The *oneadmin* account has full control of all the physical and virtual resources.

.. _acquire_resources:
 
Step 2. Acquire vCenter Resources
---------------------------------

To import new vCenter clusters to be managed in OpenNebula, proceed in Sunstone to the ``Infrastructure --> Hosts`` tab and click on the "+" green icon.

.. image:: /images/import_host.png
    :align: center




.. warning:: OpenNebula does not support spaces in vCenter cluster names.

In the dialog that pops up, select vCenter as Type in the drop-down. You now need to fill in the data according to the following table:

+--------------+------------------------------------------------------+
| **Hostname** | vCenter hostname (FQDN) or IP address                |
+--------------+------------------------------------------------------+
| **User**     | Username of a vCenter user with administrator rights |
+--------------+------------------------------------------------------+
| **Password** | Password for the above user                          |
+--------------+------------------------------------------------------+

.. image:: /images/import_host_getClusters.png
    :align: center

Select the vCenter cluster to import as OpenNebula Host and click on "Import".

.. image:: /images/import_host_import.png
    :align: center

After importing you should see a message indicating that the host was successfully imported.

.. image:: /images/import_host_import_success.png
    :align: center

.. _import_running_vms:

Now it's time to check that the vCenter import has been successful. In ``Infrastructure --> Hosts`` check if vCenter cluster has been imported, and if all the ESX hosts are available in the ESX tab.

.. note:: Take into account that one vCenter cluster (with all its ESX hosts) will be represented as one OpenNebula host. Is not possible to import individual ESX hosts, they need to be grouped in vCenter clusters.

.. image:: /images/import_host_hosts.png
    :align: center

Step 3. Import / Reacquire vCenter Resources
---------------------------------------------------------------------------------

.. _import_images_and_ds:

Datastores and Images
^^^^^^^^^^^^^^^^^^^^^

Datastores and VMDK images can be imported / reacquired from the ``Storage --> Datastores`` and ``Storage --> Images`` respectively. Since datastores are going to be used to hold the images from VM Templates, all datastore **must** be imported before VM Template import.

vCenter datastores hosts VMDK files and other file types so VMs and templates can use them, and these datastores can be represented in OpenNebula as both an Images datastore and a System datastore:

- Images Datastore. Stores the images repository. VMDK files are represented as OpenNebula images stored in this datastore.
- System Datastore. Holds disk for running virtual machines, copied or cloned from the Images Datastore.

For example, if we have a vcenter datastore called ''nfs'', when we import the vCenter datastore into OpenNebula, two OpenNebula datastores will be created as an Images datastore and as a System datastore pointing to the same vCenter datastore.

Here are the steps to import a datastore:

First go to ``Storage --> Datastores`` , click on the "+" green icon and click on "Import".

.. image:: /images/import_datastore.png
    :align: center

Select the Host (vCenter cluster) an"GetDatastores".

.. image:: /images/import_datastore_getDatastores.png
    :align: center

Select the datastore to import and click on "Import"

.. image:: /images/import_datastore_import.png
    :align: center

After importing you should see a message indicating that the datastore was successfully imported.

.. image:: /images/import_datastore_import_success.png
    :align: center

.. note:: If the vCenter instance features a read only datastore, please be aware that you should disable the SYSTEM representation of the datastore after importing it to avoid OpenNebula trying to deploy VMs in it.

When an image or a datastore is imported, OpenNebula will generate a name automatically that prevents conflicts if you try to import several files with the same name but that are located in different folders inside the datastore, or try to import datastores with the same name in different vCenter instances. These names can be changed once the image or datastore has been imported.

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

.. _import_networks:

Networks
^^^^^^^^

Similarly, Port Groups, Distributed Port Groups and NSX-T / NSx-V logical switches, can also be imported / reacquired from using a similar ``Import`` button in ``Network --> Virtual Networks``.

.. image:: /images/import_vnet.png
    :align: center

Select the Host and click on "Get Networks".

.. image:: /images/import_vnet_getNetworks.png
    :align: center

Select the network to import and click on "Import".

.. image:: /images/import_vnet_import.png
    :align: center

After importing you should see a message indicating that the network was successfully imported.

.. image:: /images/import_vnet_import_success.png
    :align: center

Virtual Networks can be further refined with the inclusion of different :onedoc:`Address Ranges <operation/network_management/manage_vnets.html#address-space>`. This refinement can be done at import time, defining the size of the network one of the following supported Address Ranges:

- IPv4: Need to define at least starting IP address. MAC address can be defined as well
- IPv6: Can optionally define starting MAC address, GLOBAL PREFIX and ULA PREFIX
- Ethernet: Does not manage IP addresses but rather MAC addresses. If a starting MAC is not provided, OpenNebula will generate one.

It is possible to limit the bandwidth of any VM NIC associated to a particular virtual network by using the Inbound/Outbound Traffic QoS values as seen in the next image.

.. image:: /images/limit_network_bw.png
    :align: center

.. _import_vm_templates:

VM Templates
^^^^^^^^^^^^

.. warning:: Since datastores are going to be used to hold the images from VM Templates, all datastore **must** be imported before VM Template import.

In OpenNebula, Virtual Machines are deployed from VMware VM Templates that must exist previously in vCenter and must be imported into OpenNebula. There is a one-to-one relationship between each VMware VM Template and the equivalent OpenNebula VM Template. Users will then instantiate the OpenNebula VM Template and OpenNebula will create a Virtual Machine clone from the vCenter template.

vCenter **VM Templates** can be imported and reacquired using the ``Import`` button in ``Templates --> VMs``.

.. image:: /images/import_template.png
    :align: center

Select the Host and click on "Get Templates".

.. image:: /images/import_template_getTemplate.png
    :align: center

Select the template to import and click on "Import".

.. image:: /images/import_template_import.png
    :align: center

After importing you should see a message indicating that the template was successfully imported.

.. image:: /images/import_template_import_success.png
    :align: center

.. _operations_on_templates:
.. _vmtemplates_and_networks:

When a VMware VM Template is imported, OpenNebula will detect any virtual disk and network interface within the template. For each virtual disk, OpenNebula will create an image representing each disk discovered in the template. In the same way, OpenNebula will create a network representation for each standard or distributed port group associated to virtual network interfaces found in the template. The imported OpenNebula VM templates can be modified selecting the VM Template in ``Virtual Resources --> Templates`` and clicking on the Update button, so the resulting VMs are adjusted to user needs.

Among other options available through the Sunstone web interface:

- Information can be passed into the instantiated VM, through either :onedoc:`Contextualization or Customization <operation/vm_setup/index.html>`
- Network interface cards can be added or removed to give VMs access to different networks
- Disks can be added or removed
- Capacity (MEMORY and CPU) can be modified
- VNC capabilities can be disabled

Existing VMs
^^^^^^^^^^^^

If the vCenter infrastructure has running or powered off **Virtual Machines**, OpenNebula can import and subsequently manage them. To import vCenter VMs, proceed to the **Wilds** tab in the Host info tab representing the vCenter cluster where the VMs are running in, select the VMs to be imported and click on the import button.

.. image:: /images/import_wild.png
    :align: center

.. image:: /images/import_wild_import.png
    :align: center

After importing you should see a message indicating that the VM was successfully imported.

.. image:: /images/import_wild_import_success.png
    :align: center

.. _operations_on_running_vms:

After the VMs are in the Running state, you can operate on their life-cycle, assign them to particular users, attach or detach network interfaces, create snapshots, do capacity resizing (change CPU and MEMORY after powering the VMs off), etc.

All the funcionality that OpenNebula supports for regular VMs is present for imported VMs with some exceptions. The following operations *cannot* be performed on an imported VM:

- Recover --recreate
- Undeploy (and Undeploy --hard)
- Stop


Once a Wild VM is imported, OpenNebula will reconfigure the vCenter VM so VNC connections can be established once the VM is monitored.

.. _name_prefix_note:

.. note:: VMs instantiated through OpenNebula will be named in vCenter as 'one-<vid>-<VM Name>', where <vid> is the id of the VM and VM Name is the name given to the VM in OpenNebula. This value can be changed using a special attribute set in the vCenter cluster representation, the OpenNebula hostt. This attribute is called "VM_PREFIX", and will evaluate one variable, $i, to the id of the VM. This attribute can be set in the "Attributes" section of the OpenNebula host.

.. note:: After a VM Template is cloned and booted into a vCenter Cluster it can access VMware advanced features and it can be managed through the OpenNebula provisioning portal -to control the life-cycle, add/remove NICs, make snapshots- or through vCenter (e.g. to move the VM to another datastore or migrate it to another ESX).

.. note:: The name assigned to the VM Template in OpenNebula contains the vCenter VM Template’s name, vCenter cluster’s name and a random string hash. That name is used to prevent conflicts when several templates with the same name are found in a vCenter instance. Once the vCenter template has been imported, the name can be changed to a more human-friendly name.

.. _cluster_prefix:

.. note:: OpenNebula does not support spaces in VMDKs paths nor names.

.. note:: Resources imported from vCenter will have their names appended with a the name of the cluster where this resources belong in vCenter, to ease their identification within OpenNebula.

.. note:: vCenter VM Templates, Networks, Distributed vSwitches, Datastores, VMDKs and Virtual Machines can be imported regardless of their position inside VM Folders, since OpenNebula will search recursively for them.
