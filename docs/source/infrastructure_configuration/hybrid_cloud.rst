.. _hybrid_cloud:

=============
Hybrid Clouds
=============

vOneCloud is capable of outsourcing virtual machines to public cloud providers. This is known as cloud bursting, and it is a feature of hybrid clouds where VMs are launched in public clouds if the local infrastructure is saturated.

If you want to extend your private cloud (formed by vOneCloud and vCenter) to create a hybrid cloud, you will need to configure at least one of the supported public clouds: `Amazon EC2 <http://docs.opennebula.org/4.10/advanced_administration/cloud_bursting/ec2g.html>`__, `IBM SoftLayer <http://docs.opennebula.org/4.10/advanced_administration/cloud_bursting/slg.html>`__ or `Microsoft Azure <http://docs.opennebula.org/4.10/advanced_administration/cloud_bursting/azg.html>`__. All hybrid drivers are already enabled in vOneCloud, but you need to configure them first with your public cloud credentials.

You can add hybrid hosts from the vCenter View:

.. image:: /images/hybrid_vcenter_view.png
    :align: center

The hybrid approach is carried out using hybrid templates, which represents the virtual machines locally and remotely. The idea is to build a vOneCloud hybrid VM template that represents the same VM in vCenter and in the public cloud. Let's see an example of such a template, assuming that vCenter Template uuidA and Amazon EC2 AMI ami-xxxx represents the same virtual machine (for instance, a web server serving a web portal):

.. code::

    CPU=1
    MEMORY=1024

    PUBLIC_CLOUD=[
      TYPE="vcenter",
      VM_TEMPLATE="uuidA" ]

    PUBLIC_CLOUD=[
      TYPE="ec2",
      AMI="ami-00bafcb5",
      KEYPAIR="gsg-keypair",
      INSTANCETYPE=m1.small]

Once templates are ready, they can be consumed at VM creation time from the Cloud View:

.. image:: /images/hybrid_cloud_view.png
    :align: center

Learn more about `hybrid support <http://docs.opennebula.org/4.10/advanced_administration/cloud_bursting/introh.html>`__.
