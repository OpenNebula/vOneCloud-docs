.. _add_new_vcenter:

===========================================
Add New vCenters, VM Templates and Networks
===========================================

vOneCloud can manage an unlimited number of vCenters. Each vCenter is going to be represented by an vOneCloud host, which in turn abstracts all the ESX hosts managed by that particular instance of vCenter.

The suggested usage is to build vOneCloud templates for each VM Template in each vCenter. The built in scheduler in vOneCloud will decide which vCenter has the VM Template needed to launch the VM.

Add New vCenter Cluster
-----------------------

The mechanism to add a **new vCenter** is exactly the same as the one used to :ref:`import the first one into vOneCloud <import_vcenter>`. It can be performed graphically from the vCenter View:

.. image:: /images/add_new_vcenter.png
    :align: center

.. _encrypt_key:

.. note::

   vOneCloud will create a special key at boot time and save it in /var/lib/one/.one/one_key. This key will be used as a private key to encrypt and decrypt all the passwords for all the vCenters that vOneCloud can access. Thus, the password shown in the vOneCloud host representing the vCenter is the original password encrypted with this special key.

Add New VM Template
-------------------

.. _add_new_vm_template:

To create a new **vOneCloud VM Template**, let's see an example:

  Firsts things first, to avoid misunderstandings, there are two VM templates we will refer to: the vOneCloud VM Templates and the vCenter VM Templates. The formers are created in the vOneCloud web interface (Sunstone), whereas the latters are created directly through the vCenter Web Client.

  A cloud administrator builds two vOneCloud templates to represent one vCenter VM Template avaiable in vCenterA and another available in vCenterB. As previous work, the cloud administrator creates `two vCenter VM templates <https://pubs.vmware.com/vsphere-50/index.jsp?topic=%2Fcom.vmware.vsphere.vm_admin.doc_50%2FGUID-40BC4243-E4FA-4A46-8C8B-F50D92C186ED.html>`__, one in each vCenter.

  To create a vOneCloud VM Template representing a vCloud VM Template, log in into Sunstone as **vOneCloud** user as in explained :ref:`here <download_and_deploy>`, proceed to the ``Virtual Resources -> Templates``, and click on the **+** sign. Select *vCenter* as the hypervisor, and type in the *vCenter Template UUID*. You can also set a capacity (CPU and Memory) that would be honored at the time of instantiating the VM. In the *Scheduling* tab you can select the hostname of the specific vCenter. The *Context* tab allows to pass information onto the VM to tailor it for its final use (read more about it :ref:`here <build_template_context>`). In *Network* tab a valid Virtual Network (see below) can added to the VM, possible values for the MODEL type of the network card are:

  - virtuale1000
  - virtuale1000e
  - virtualpcnet32
  - virtualsriovethernetcard
  - virtualvmxnetm
  - virtualvmxnet2
  - virtualvmxnet3

  .. image:: /images/vcenter_wizard.png
    :align: center

  Fill in with UUID **uuidA** in and select host vCenterA. Repeat for vCenterB.

  If a user instantiates one of these templates, the :doc:`vOneCloud scheduler <administration/references/schg.html>` will pick the right vCenter in which to instantiate the VM Template.

  The variable KEEP_DISKS_ON_DONE can be used in the VM template to instruct vOneCloud not to erase the VM disks after it enters the DONE state (either through shutdown or cancel)

Using :ref:`the automated process for importing vCenter infrastructures <import_vcenter>`, vOneCloud will generate the above template for you at the time of importing vCenterA.

.. _add_multi_cluster_vm_template:

Add Multi Cluster VM Template
-----------------------------

A single vOneCloud VM Template can be used to represent different vCenter VM Templates in different vCenter clusters. These multi cluster templates must be created using the Advanced tab in the VM Template creation dialog of vOneCloud, stating two or more PUBLIC_CLOUD tags, one per vCenter VM Template that wants to be referenced.

The list of attributes that can be used to create vOneCloud VM Templates through the Advanced tab follows:


+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|     Attribute      |                                                                                                                            Meaning                                                                                                                             |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| CPU                | Physical CPUs to be used by the VM. This does not have to relate to the CPUs used by the vCenter VM Template, OpenNebula will change the value accordingly                                                                                                     |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MEMORY             | Physical Memory in MB to be used by the VM. This does not have to relate to the CPUs used by the vCenter VM Template, OpenNebula will change the value accordingly                                                                                             |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NIC                | Valid MODELs are: virtuale1000, virtuale1000e, virtualpcnet32, virtualsriovethernetcard, virtualvmxnetm, virtualvmxnet2, virtualvmxnet3.                                                                                                                       |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GRAPHICS           | Multi-value - Only VNC supported.                                                                                                                                                                                                                              |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PUBLIC_CLOUD       | Multi-value. TYPE must be set to vcenter, VM_TEMPLATE must point to the uuid of the vCenter VM that is being represented and HOST must refer to the name of the vCenter Cluster (represented by a vOneCloud host) where the template is available              |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SCHED_REQUIREMENTS | NAME="name of the vCenter cluster where this VM Template can instantiated into a VM".                                                                                                                                                                          |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| CONTEXT            | All sections will be honored except FILES                                                                                                                                                                                                                      |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| KEEP_DISKS_ON_DONE | (Optional) Prevent OpenNebula from erasing the VM disks upon reaching the done state (either via shutdown or cancel)                                                                                                                                           |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| VCENTER_DATASTORE  | By default, the VM will be deployed to the datastore where the VM Template is bound to. This attribute allows to set the name of the datastore where this VM will be deployed.  This can be overwritten explicitly at deployment time from the CLI or Sunstone |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

  .. image:: /images/vcenter_wizard.png
    :align: center

Add New Network/Distributed vSwitch
-----------------------------------

**vCenter Networks/Distributed vSwitches** for a particular vCenter cluster can be imported in vOneCloud after the cluster is imported using the `same procedure <import_running_vms>`__ to import vCenter clusters, making use of the ``Infrastructure --> Hosts`` tab in the vCenter View.

A representation of a vCenter Network or Distributed vSwitch in vOneCloud can be created in vOneCloud by creating a Virtual Network and setting the BRIDGE property to **exactly the same name as the vCenter Network**. Leave "Default" network model if you don't need to define VLANs for htis network, otherwise chose the "VMware" network model.

.. image:: /images/vnet_bridge.png
  :align: center

Several different Address Ranges can be added as well in the Virtual Network creation and/or Update dialog, pretty much in the same way as it can be done at the time of acquiring the resources explained in the :ref:`Import vCenter guide <acquire_resources>`.

Add New Datastore
-----------------

The vCenter datastore in vOneCloud is tied to a vCenter OpenNebula host in the sense that all operations to be perfomed in the datastore are going to be performed through the vCenter instance associated to the vOneCloud host, which happens to hold the needed credentials to access the vCenter instance.

Creation of empty datablocks and VMDK image cloning are supported, as well as image deletion. 

Adding a new datastore and representing existing VMDK images enables disk attach/detach functionality. VM disks in vCenter VMs that exist in the VM template (ie, not added through vOneCloud) are not able to be managed through vOneCloud.

Images cannot be upload to the vCenter datastore, but existing images can be represented. In order to create an image in vOneCloud that represents a vCenter datastore, use the following parameters:

+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|    Attribute     |                                                                                                                                                                                                   Description                                                                                                                                                                                                   |
+==================+=================================================================================================================================================================================================================================================================================================================================================================================================================+
| ``NAME``         | Arbitrary name of the image                                                                                                                                                                                                                                                                                                                                                                                     |
+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``PERSISTENT``   | Must be set to 'YES'                                                                                                                                                                                                                                                                                                                                                                                            |
+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``PATH``         | Path of the VMDK file in the datastore. For instance, an image win10.vmdk in a Windows folder should be set to Windows/win10.vmdk                                                                                                                                                                                                                                                                               |
+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ADAPTER_TYPE`` | Possible values (careful with the case): lsiLogic, ide, busLogic. More information `in the VMware documentation <http://pubs.vmware.com/vsphere-60/index.jsp#com.vmware.wssdk.apiref.doc/vim.VirtualDiskManager.VirtualDiskAdapterType.html>`__                                                                                                                                                                 |
+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``DISK_TYPE``    | The type of disk has implications on performance and occupied space. Values (careful with the case): delta,eagerZeroedThick,flatMonolithic,preallocated,raw,rdm,rdmp,seSparse,sparse2Gb,sparseMonolithic,thick,thick2Gb,thin. More information `in the VMware documentation <http://pubs.vmware.com/vsphere-60/index.jsp?topic=%2Fcom.vmware.wssdk.apiref.doc%2Fvim.VirtualDiskManager.VirtualDiskType.html>`__ |
+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


Import Running VMs
------------------

**Running** and **Powered Off VMs** can be imported through the WILDS tab in the Host info tab representing the vCenter cluster where the VMs are running in.

.. image:: /images/import_wild_vms.png
    :width: 90%
    :align: center

Read more about the :doc:`vCenter drivers <administration/virtualization/vcenterg.html>`. Regarding the vCenter datastores in vOneCloud, refer to the :doc:`vCenter datastore guide <administration/storage/vcenter_ds.html>`
