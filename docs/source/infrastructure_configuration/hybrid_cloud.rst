.. _hybrid_cloud:

=============
Hybrid Clouds
=============

vOneCloud is capable of outsourcing virtual machines to public cloud providers. This is known as cloud bursting, and it is a feature of hybrid clouds where VMs are launched in public clouds if the local infrastructure is saturated.

If you want to extend your private cloud (formed by vOneCloud and vCenter) to create a hybrid cloud, you will need to configure at least one of the supported public clouds: Amazon EC2, IBM SoftLayer and Microsoft Azure. All hybrid drivers are already enabled in vOneCloud, but you need to configure them first with your public cloud credentials.

You will need to access the :ref:`Control Panel <control_panel>` in order to configure the hybrid support in vOneCloud.

Step 1. Configure a Hybrid Region
--------------------------------------------------------------------------------

In the Control Panel is possible to add regions of Amazon EC2, IBM SoftLayer and Microsoft Azure to be used within vOneCloud.

.. image:: /images/cp_hybrid_region.png
    :align: center

Each region from the different supported cloud providers have different requirements in terms of configuration:

**Amazon EC2**

.. image:: /images/cp_hybrid_ec2.png
    :align: center

The capacity that you attach to this region will define the maximum number and type of Virtual Machines that vOneCloud will be able to launch in the represented Amazon EC2 region. The different instance types are defined as follows:

+-----------+------------+---------+
| **Name**  | **Memory** | **CPU** |
+-----------+------------+---------+
| m1.small  | 1.7 GB     | 1       |
+-----------+------------+---------+
| m1.medium | 3.75 GB    | 1       |
+-----------+------------+---------+
| m1.large  | 7.5 GB     | 2       |
+-----------+------------+---------+

Follow the tool tips that appear on mouse over to correctly configure the parameters.

You need the Access and Secret key to be retrieved from your AWS account. More information on Amazon EC2 support can be found :doc:`here <advanced_administration/cloud_bursting/ec2g.html>`.

**MS Azure**

.. image:: /images/cp_hybrid_az.png
    :align: center

The capacity that you attach to this region will define the maximum number and type of Virtual Machines that vOneCloud will be able to launch in the represented MS Azure region.  The different instance types are defined as follows:

+----------+------------+---------+
| **Name** | **Memory** | **CPU** |
+----------+------------+---------+
| Small    | 1.75 GB    |       1 |
+----------+------------+---------+
| Medium   | 3.5 GB     |       2 |
+----------+------------+---------+
| Large    | 7 GB       |       4 |
+----------+------------+---------+

Follow the tool tips that appear on mouse over to correctly configure the parameters.

You need the Pem Management Certificate to be retrieved from your AWS account. Follow the next steps to craft a valid certificate:

- First, the Subscription ID, that can be uploaded and retrieved from Settings -> Subscriptions
- Second, the Management Certificate file, that can be created with the following steps. We need the .pem file (for the ruby gem) and the .cer file (to upload to Azure):

.. code::

    ## Install openssl
    ## CentOS
    $ sudo yum install openssl
    ## Ubuntu
    $ sudo apt-get install openssl

    ## Create certificate
    $ openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout myPrivateKey.key -out myCert.pem
    $ chmod 600 myPrivateKey.key

    ## Concatenate key and pem certificate
    $ cat myCert.pem myPrivateKey.key > vOneCloud.pem

    ## Generate .cer file for Azure
    $ openssl  x509 -outform der -in myCert.pem -out myCert.cer

- Third, the certificate file (.cer) has to be uploaded to Settings -> Management Certificates

Afterwards, copy the context of the .pem certificate in the clipboard and paste it in the text area of the Control Panel Pem Management Certificate field.

More information on MS Azure support can be found :doc:`here <advanced_administration/cloud_bursting/azg.html>`.

.. note:: Azure hybrid connectors only support non authenticated http proxies

**IBM SoftLayer**

.. image:: /images/cp_hybrid_sl.png
    :align: center

The capacity that you attach to this region will define the maximum number and type of Virtual Machines that vOneCloud will be able to launch in the represented IBM SoftLayer region. The different instance types are defined as follows:

+--------------+------------+---------+
|   **Name**   | **Memory** | **CPU** |
+--------------+------------+---------+
| slcci.small  | 1 GB       |       1 |
+--------------+------------+---------+
| slcci.medium | 4 GB       |       2 |
+--------------+------------+---------+
| slcci.large  | 8 GB       |       4 |
+--------------+------------+---------+

Follow the tool tips that appear on mouse over to correctly configure the parameters.

You need your SoftLayer Username and the API Key that can be retrieved from your SoftLayer Control Panel. More information on IBM SoftLayer support can be found :doc:`here <advanced_administration/cloud_bursting/slg.html>`.

.. warning:: If vOneCloud is running behind a corporate http proxy, the SoftLayer hybrid connectors won't be available

Step 2. Restart vOneCloud services
--------------------------------------------------------------------------------

Click on the "Apply Settings" button. For changes to take effect, you need to restart vOneCloud services and wait for OpenNebula state to be ON.

.. image:: /images/cp_restart_one.png
    :align: center

Step 3. Create vOneCloud hybrid resources
--------------------------------------------------------------------------------

Afterwards, each region can be represented by vOneCloud hosts can be added from the vCenter View:

.. image:: /images/hybrid_vcenter_view.png
    :align: center

The hybrid approach is carried out using hybrid templates, which represents the virtual machines locally and remotely. The idea is to build a vOneCloud hybrid VM template that represents the same VM in vCenter and in the public cloud. This can be carried out using the hybrid section of the VM Template creation dialog (you can add one or more public cloud provider)

.. image:: /images/hybrid_create_template.png
    :align: center

Moreover, you need to add in the Scheduling tab a proper host representing the appropriate public cloud provider. For instance, for an EC2 hybrid VM Template:

.. image:: /images/scheduling_hybrid_template.png
    :align: center

Once templates are ready, they can be consumed at VM creation time from the Cloud View:

.. image:: /images/hybrid_cloud_view.png
    :align: center

Learn more about :doc:`hybrid support <advanced_administration/cloud_bursting/introh.html>`.
