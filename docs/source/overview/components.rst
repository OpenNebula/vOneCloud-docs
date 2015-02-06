.. _components:

================================================================================
Components
================================================================================

This diagram reflects the relationship between the components that compose the vOneCloud platform.

.. image:: /images/vonecloud-components.png
    :align: center

vCenter infrastructure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

vOneCloud is an appliance that is executed under vCenter. vOneCloud then leverages this previously set up infrastructure composed of vCenter and ESX nodes.

OpenNebula (Cloud Manager)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`OpenNebula <http://docs.opennebula.org/4.10/design_and_installation/building_your_cloud/intro.html>`_ acts as the Cloud Manager of vOneCloud, responsible for managing your virtual vCenter resources and adding a Cloud layer on top of it.

**Sunstone** is the web-based graphical interface of OpenNebula. It is available at `http://<appliance_ip>`. This interface is at the same time the main administration interface for you cloud infrastructure, and consumer interface for the final users of the cloud.

Control Panel and Control Console
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Control Panel and Control Console are two components which have the goal of
configuring different aspects of the vOneCloud appliance: network, appliance
user accounts, OpenNebula (Sunstone) configuration and services.
