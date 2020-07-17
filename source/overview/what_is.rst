.. _what_is:

========
What Is?
========

.. image:: /images/vonecloud_logo.png
    :align: center

vOneCloud |release| ships with the following components under the hood:

+-----------------------+--------------------------------------------------------------------------------------------------+
|       **CentOS**      |                                                8                                                 |
+-----------------------+--------------------------------------------------------------------------------------------------+
| **OpenNebula**        | |release| (:onedoc:`release notes <intro_release_notes/release_notes/index.html>`)               |
+-----------------------+--------------------------------------------------------------------------------------------------+
| **MariaDB**           | Default version shipped in CentOS 8                                                              |
+-----------------------+--------------------------------------------------------------------------------------------------+
| **Phusion Passenger** | Default version shipped in EPEL 8 (used to run Sunstone)                                         |
+-----------------------+--------------------------------------------------------------------------------------------------+

OpenNebula
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

OpenNebula is a simple, yet powerful and flexible turnkey open source solution to build Private Clouds and manage Data Center virtualization based on VMware, KVM, LXD and Firecracker. Its integration with AWS and Microsoft Azure offers flexibility in creating hybrid cloud infrastructures, as well as with bare-metal providers like Packet and AWS for trouble-free deployment of Edge Computing resources. Its compatibility with other open source platforms and third-party technologies like Kubernetes, Ansible, Docker and Terraform make it a versatile enterprise solution. OpenNebula’s maturity builds upon over a decade of software releases and thousands of enterprise deployments, being widely used by industry and research leaders.

OpenNebula on VMware
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

OpenNebula is intended for companies willing to create a self-service cloud environment on top of their VMware infrastructure without having to abandon their investment in VMware and retool the entire stack. In these environments, OpenNebula seamlessly integrates with existing vCenter infrastructures to leverage advanced features—such as vMotion, HA or DRS scheduling—provided by the VMware vSphere product family. OpenNebula exposes a multi-tenant, cloud-like provisioning layer on top of vCenter, including features like Virtual Data Centers (VDCs), data center federation, or hybrid cloud computing connecting in-house vCenter infrastructure with public clouds. Resources like VM, VM Templates, datastores and networks can be easily imported from vCenter infrastructures to OpenNebula. OpenNebula also makes it possible to take steps towards liberating your stack from vendor lock-in. Once you have built your cloud with OpenNebula on VMware, you can then add new resources based on open source hypervisors⁠—like KVM—and hence use OpenNebula as a migration framework to the open cloud.

vOneCloud
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

vOneCloud is a virtual appliance for vSphere that builds on top of your vCenter an OpenNebula cloud for development, testing or product evaluation in 5 minutes. In a nutshell, it is an OVA file with a configured CentOS and OpenNebula installation ready to import resources from vCenter environments. vOneCloud is free to download and use. The virtual appliance does not interfere with existing vSphere configurations, procedures and workflows. This means that you can try it and if you decide not to adopt it, you can just delete it. vOneCloud can be also used for small-size production deployments.

.. image:: /images/vonecloud_ontop.png
    :align: center
