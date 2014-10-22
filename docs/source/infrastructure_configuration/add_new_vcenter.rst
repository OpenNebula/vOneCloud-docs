.. _add_new_vcenter:

================
Add New vCenters
================

vOneCloud can manage more than one instance of vCenter. Each vCenter is going to be represented by an vOneCloud host, which in turn abstracts all the ESX hosts managed by that particular instance of vCenter.

This approach is quite similar to the hybrid approach. The suggested usage is to build vOneCloud templates that represents the same VM Template across different vCenters. The built in scheduler in vOneCloud will decide which vCenter is suitable to host a VM requested by the user, based on based on performance metrics. 

The mechanism to add a new vCenter is exactly the same as the one used to :ref:`import the first one into vOneCloud <import_vcenter>`. It can be performed graphicaly from the vCenter View:

.. image:: /images/add_new_vcenter.png
    :align: center

Everything is clearer with an example, so here we go:

  Firsts things first, to avoid misunderstandings, there two VM templates we will talk about now: the vOneCloud VM Templates and the vCenter VM Templates. The first ones are created in the vOneCloud web interface (Sunstone), whereas the latter are created directly through the vCenter web interface (vSphere Web Client).

  A cloud administrator wants to define a single vOneCloud template that represents the same virtual machine (for instance, a web portal) across two different vCenters. As previous work, the cloud administrator creates `two vCenter VM templates <https://pubs.vmware.com/vsphere-50/index.jsp?topic=%2Fcom.vmware.vsphere.vm_admin.doc_50%2FGUID-40BC4243-E4FA-4A46-8C8B-F50D92C186ED.html>`__, one in each vCenter, each one tailored to launch the same virtual machine. This can be achieved either by configuring the same software in two virtual machines, or by copying the images of the VM from one vCenter to the other. 

  Once the two vCenter VM templates are created (let's assume they have **uuidA** and **uuidB**), a vOneCloud VM template can be created to represent the same VM. If a user instantiates this template, the vOneCloud scheduler will pick one vCenter or the other based on configurable `scheduler policies <http://docs.opennebula.org/4.10/administration/references/schg.html>`__. Since the vOneCloud template references two vCenter VM Templates, but both of them launch the same Virtual Machine, the end result is the same regardless of which vCenter ends up doing the job. This is true for 2 or more vOneCloud managed vCenters.

  To create a vOneCloud VM template, log in into Sunstone as **vonecloud** user as in explained :ref:`here <download_and_deploy>`, proceed to the ``Virtual Resources -> Templates``, and click on the **+** sign. In the upper right corner there will be two tabs, click on the "Advanced" one, and input the following:

.. code::

    CPU=1
    MEMORY=1024

    PUBLIC_CLOUD=[
      TYPE="vcenter",
      LOCATION="vCenterA"
      VM_TEMPLATE="uuidA" ]

    PUBLIC_CLOUD=[
      TYPE="vcenter",
      LOCATION="vCenterB",
      VM_TEMPLATE="uuidB" ]

Read more about the `vCenter drivers <http://docs.opennebula.org/4.10/administration/virtualization/vcenterg.html>`__.
