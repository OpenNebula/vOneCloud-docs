.. _download_and_deploy:

================================================================================
Download and Deploy
================================================================================

Download links:

- `vOneCloud-1.2.ova <http://downloads.vonecloud.today>`__
- `md5sum.txt <http://appliances.opennebula.systems/vOneCloud/md5sum.txt>`__

You can import this OVA appliance to your vCenter infrastructure. It is based on
`CentOS 7 <http://www.centos.org/>`__ and has the VMware tools enabled.

The appliance requirements are kept to a strict minimum so it can be executed in
any vCenter installation. However, before deploying it, please read the :ref:`system requirements <system_requirements>`.

Follow the next steps to deploy a fully functional vOneCloud:

Step 1. Deploying the OVA
--------------------------------------------------------------------------------

Login to your vCenter installation and select the appropriate datacenter and cluster, where you want to deploy the appliance. Select the ``Deploy OVF Template``.

.. image:: /images/vOneCloud-download-deploy-001.png
    :align: center

You have the option now to input the URL of the appliance (you can find it at the top of this page), or if you have previously downloaded it, you can simply browse to the download path as such:

.. image:: /images/vOneCloud-download-deploy-001a.png
    :align: center

.. image:: /images/vOneCloud-download-deploy-002.png
    :align: center

Select the name and folder:

.. image:: /images/vOneCloud-download-deploy-003.png
    :align: center

Select a resource to run the appliance:

.. image:: /images/vOneCloud-download-deploy-004.png
    :align: center

Select the datastore:

.. image:: /images/vOneCloud-download-deploy-005.png
    :align: center

Select the Network. You will need to choose a network that has access to the vCenter hosts.

.. image:: /images/vOneCloud-download-deploy-006.png
    :align: center

Review the settings selection and click finish. Wait for the Virtual Machine to appear in the cluster.

.. image:: /images/vOneCloud-download-deploy-007.png
    :align: center

Now you can power on the Virtual Machine:

.. image:: /images/vOneCloud-download-deploy-008.png
    :align: center

.. todo::

    Divided into steps: Open VMware console (screenshot). Run initial bootstrap, login to vOneCloud Control Center, configure OpenNebula, start OpenNebula, open Sunstone (info about credentials). Link to: Now you will be able to use the :ref:`out-of-the-box features <features_outofthebox>` of vOneCloud!

Advanced Usage [Optional]
-------------------------

.. todo::

   add vOneCloud Control Center link in the following section

.. warning::
    This section is entirely optional and only advanced users should perform these actions.

    If you make **any** changes to OpenNebula configuration files under ``/etc/one`` please note that they **will** be either discarded in the next upgrade, or overwritten by vOneCloud Control Center and overwritten by the  upgrade.

.. _advanced_login:

Login to the Appliance
~~~~~~~~~~~~~~~~~~~~~~

.. todo::

   Rewrite this:

   All the functionality you need to run your vOneCloud can be accessed via
   Sunstone. However, in order to enable some of the :ref:`advanced features
   <features_advanceconf>` of vOneCloud some extra configurations steps are needed
   that must be performed in the command line of vOneCloud, and can be carried out
   opening a console in your vCenter client and log in with these credentials:

   - **Username**: root
   - **Password**: opennebula

   .. note:: SSH access to the root account has been disabled.

.. todo::

   Change oneadmin password and configure the network have been removed from this guide. Decide whether to place links to those actions.
