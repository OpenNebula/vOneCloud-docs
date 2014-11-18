.. _hybrid_cloud:

=============
Hybrid Clouds
=============

vOneCloud is capable of outsourcing virtual machines to public cloud providers. This is known as cloud bursting, and it is a feature of hybrid clouds where VMs are launched in public clouds if the local infrastructure is saturated.

If you want to extend your private cloud (formed by vOneCloud and vCenter) to create a hybrid cloud, you will need to configure at least one of the supported public clouds: Amazon EC2, IBM SoftLayer and Microsoft Azure. All hybrid drivers are already enabled in vOneCloud, but you need to configure them first with your public cloud credentials. 

To configure the drivers you need first to :ref:`log into the vOneCloud console <advanced_login>`, and set in the following files (all of them can be found in /etc/one, and edited as root) depending on which public cloud you want to enable(refer to the linked guide for more detailed information):

+-------------------------------------------------------------------------------------------------------+-----------------+
| `Amazon EC2 <http://docs.opennebula.org/4.10/advanced_administration/cloud_bursting/ec2g.html>`__     | ec2_driver.conf |
+-------------------------------------------------------------------------------------------------------+-----------------+
| `IBM SoftLayer <http://docs.opennebula.org/4.10/advanced_administration/cloud_bursting/slg.html>`__   | sl_driver.conf  |
+-------------------------------------------------------------------------------------------------------+-----------------+
| `Microsoft Azure <http://docs.opennebula.org/4.10/advanced_administration/cloud_bursting/azg.html>`__ | az_driver.conf  |
+-------------------------------------------------------------------------------------------------------+-----------------+

Afterwards, hybrid hosts can be added from the vCenter View:

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

Learn more about `hybrid support <http://docs.opennebula.org/4.10/advanced_administration/cloud_bursting/introh.html>`__.
