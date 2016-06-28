.. _components:

================================================================================
Components
================================================================================

This diagram reflects the relationship between the components that compose the vOneCloud platform.

.. image:: /images/vonecloud-components.png
    :align: center

vCenter infrastructure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- vOneCloud is an appliance that is executed on vCenter. vOneCloud then leverages this previously set up infrastructure composed of vCenter and ESX nodes.

OpenNebula (Cloud Manager)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- :doc:`OpenNebula <intro_release_notes/concepts_terminology/intro.html>` acts as the Cloud Manager of vOneCloud, responsible for managing your virtual vCenter resources and adding a Cloud layer on top of it.

- **Sunstone** is the web-based graphical interface of OpenNebula. It is available at `http://<appliance_ip>`. This interface is at the same time the main administration interface for you cloud infrastructure, and consumer interface for the final users of the cloud.

Control Console and Control Panel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Control Console and Control Panel are two components which have the goal of configuring different aspects of the vOneCloud appliance: network, appliance user accounts, OpenNebula (Sunstone) configuration and services. 

- The :ref:`Control Console <control_console>` is a text based wizard accessible through the vCenter console to the vOneCloud appliance and has relevance in the bootstrap process and the configuration of the appliance
- The :ref:`Control Panel <control_panel>` is a slick web interface and is oriented to the configuration of the vOneCloud services as well as used to update to a newer version of vOneCloud.