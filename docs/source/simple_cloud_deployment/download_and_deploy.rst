.. _download_and_deploy:

================================================================================
Download and Deploy
================================================================================

vOneCloud can be download as an appliance from here:
`http://appliances.c12g.com/vOneCloud/vOneCloud-4.10-beta.ova <http://appliances.c12g.com/vOneCloud/vOneCloud-4.10-beta.ova>`_

You can import this OVA appliance to your vCenter infrastructure. It is based on
`CentOS 7 <http://www.centos.org/>`_ and has the VMware tools enabled.

The appliance requirements are kept to a strict minimum so it can be executed in
any vCenter installation. However, before deploying it, please read the :ref:`system requirements <system_requirements>`.

Deploying the OVA
--------------------------------------------------------------------------------

001.png

Login to your vCenter installation and select the appropriate datacenter and cluster, where you want to deploy the appliance. Select the ``Deplpy OVF Template``.

.. image:: /images/vOneCloud-download-deploy-001.png
    :align: center

001a.png

You have the option now to input the URL of the appliance (you can find it at the top of this page), or if you have previously downloaded it, you can simply browse to the download path as such:

.. image:: /images/vOneCloud-download-deploy-001a.png
    :align: center

002.png

Input a name for and select the cluster:

.. image:: /images/vOneCloud-download-deploy-002.png
    :align: center

003.png

Select the resource:

.. image:: /images/vOneCloud-download-deploy-003.png
    :align: center

004.png

Select the storage:

.. image:: /images/vOneCloud-download-deploy-004.png
    :align: center

005.png

Select the Network. You will need to choose a network that has access to the vCenter hosts.

.. image:: /images/vOneCloud-download-deploy-005.png
    :align: center

006.png

Review the settings selection and click finish. Wait for the Virtual Machine to appear in the cluster.

.. image:: /images/vOneCloud-download-deploy-006.png
    :align: center

007.png

.. image:: /images/vOneCloud-download-deploy-007.png
    :align: center

008.png

Now you can power on the Virtual Machine:

.. image:: /images/vOneCloud-download-deploy-008.png
    :align: center

010.png

Allow for a few minutes for the Appliance start and report the IP.

.. image:: /images/vOneCloud-download-deploy-010.png
    :align: center

Connecting to the Sunstone Interface
--------------------------------------------------------------------------------

Now that you have the IP of the appliance you can open the Sunstone Web Interface: ``http://<appliance-ip>:9869``.

.. image:: /images/sunstone_login.png
    :align: center

To login type in these credentials:

- **Username**: vOneCloud
- **Password**: opennebula

Advanced Usage - Login to the Appliance
--------------------------------------------------------------------------------

All the functionality you need to run your vOneCloud can be accessed via
Sunstone. However, if you are and advanced user and want to log into the
appliance, you can do so by opening a console in your vCenter client and log in
with these credentials:

- **Username**: root
- **Password**: opennebula

Note that SSH access to the root account has been disable.
