.. _import_vcenter:

=======================
Import Existing vCenter
=======================

Importing a vCenter infrastructure into vOneCloud can be carried out easily through the Sunstone Web UI. Follow the next steps to import an existing vCenter as well as any already defined VM Template.

You will need the IP or hostname of the vCenter server, as well as an administrator credentials to successfuly import resources from vCenter.

Step 1. Sunstone login
-----------------------

Log in into Sunstone as **vOneCloud**, as explained in :ref:`the previous section <download_and_deploy>`.

.. _acquire_resources:

Step 2. Acquire vCenter Resources
---------------------------------

In Sunstone, proceed to the ``Infrastructure --> Hosts`` tab and click on the "+" green icon.

.. image:: /images/import_cluster.png
    :align: center

In the dialog that pops up, select vCenter as Type in the dropdown. You now need to fill in the data according to the following table:

+--------------+------------------------------------------------------+
| **Hostname** | vCenter hostname or IP address                       |
+--------------+------------------------------------------------------+
| **User**     | Username of a vCenter user with administrator rights |
+--------------+------------------------------------------------------+
| **Password** | Password for the above user                          |
+--------------+------------------------------------------------------+

.. image:: /images/vcenter_create.png
    :align: center

After the vCenter cluster is selected in Step 2, a list of vCenter VM templates will be presented to be imported into vOneCloud. Select all the templates you want to import, and vOneCloud will generate vOneCloud VM template resources representing the vCenter VM templates.

These vOneCloud VM templates can be edited to add information to be passed into the instantiated VM. This process is called :ref:`Contextualization <build_template_context>`.

.. note:: The vCenter VM Templates can be imported regardless of their position inside VM Folders, since vOneCloud will search recursively for them.

Step 3. Check resources
-----------------------

Now it's time to check that the vCenter import has been succesful. In ``Infrastructure --> Hosts`` check vCenter has been imported, and if all the ESX hosts are available:

.. note:: Take into account that one vCenter cluster (with all its ESX hosts) will be represented as one vOneCloud host.

.. image:: /images/import_vcenter_esx_view.png
    :align: center

Step 4. Instantiate a VM Template
---------------------------------

Everything is ready! Now vOneCloud is prepared to manage Virtual Machines. In Sunstone, go to ``Virtual Resources --> Templates``, select one of the templates imported in **Step 2** and click on Instantiate. Now you will be able to control the lifecycle of the VM.

More information on available operations over VMs `here <http://docs.opennebula.org/4.10/user/virtual_resource_management/vm_guide_2.html>`__.
