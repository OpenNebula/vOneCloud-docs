.. _add_new_vcenter:

=================================
Add New vCenters And VM Templates
=================================

vOneCloud can manage an unlimited number of vCenters. Each vCenter is going to be represented by an vOneCloud host, which in turn abstracts all the ESX hosts managed by that particular instance of vCenter.

The suggested usage is to build vOneCloud templates for each VM Template in each vCenter. The built in scheduler in vOneCloud will decide which vCenter has the VM Template needed to launch the VM.

The mechanism to add a new vCenter is exactly the same as the one used to :ref:`import the first one into vOneCloud <import_vcenter>`. It can be performed graphically from the vCenter View:

.. image:: /images/add_new_vcenter.png
    :align: center

.. note::

   vOneCloud will create a special key at boot time and save it in /var/lib/one/.one/one_key. This key will be used as a private key to encrypt and decrypt all the passwords for all the vCenters that vOneCloud can access. Thus, the password shown in the vOneCloud host represneting the vCenter is the original password encrypted with this special key.

Everything is clearer with an example, so here we go:

  Firsts things first, to avoid misunderstandings, there are two VM templates we will refer to: the vOneCloud VM Templates and the vCenter VM Templates. The formers are created in the vOneCloud web interface (Sunstone), whereas the latters are created directly through the vCenter Web Client.

  A cloud administrator builds two vOneCloud templates to represent one vCenter VM Template avaiable in vCenterA and another available in vCenterB. As previous work, the cloud administrator creates `two vCenter VM templates <https://pubs.vmware.com/vsphere-50/index.jsp?topic=%2Fcom.vmware.vsphere.vm_admin.doc_50%2FGUID-40BC4243-E4FA-4A46-8C8B-F50D92C186ED.html>`__, one in each vCenter.

  To create a vOneCloud VM template representing a vCloud vM Template, log in into Sunstone as **vOneCloud** user as in explained :ref:`here <download_and_deploy>`, proceed to the ``Virtual Resources -> Templates``, and click on the **+** sign. Select *vCenter* as the hypervisor, and type in the *vCenter Template UUID*. In the *Scheduling* tab you can select the hostname of the specific vCenter.

  .. image:: /images/vcenter_wizard.png
    :align: center

  Fill in with UUID **uuidA** in and select host vCenterA. Repeat for vCenterB.

  If a user instantiates one of these templates, the `vOneCloud scheduler <http://docs.opennebula.org/4.10/administration/references/schg.html>`__ will pick the right vCenter in which to instantiate the VM Template.

Using :ref:`the automated process for importing vCenter infrastructures <import_vcenter>`, vOneCloud will generate the above template for you at the time of importing vCenterA.

Read more about the `vCenter drivers <http://docs.opennebula.org/4.10/administration/virtualization/vcenterg.html>`__.
