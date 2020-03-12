.. _components:

================================================================================
Components
================================================================================

This diagram reflects the relationship between the components that compose or interacts with vOneCloud.

vCenter infrastructure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- vOneCloud is an appliance that is executed on vCenter. vOneCloud then leverages this previously set up infrastructure composed of vCenter and ESX nodes.

OpenNebula (Cloud Manager)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- :onedoc:`OpenNebula <intro_release_notes/concepts_terminology/intro.html>` acts as the Cloud Manager of vOneCloud, responsible for managing your virtual vCenter resources and adding a Cloud layer on top of it.

- **Sunstone** is the web-based graphical interface of OpenNebula. It is available at `http://<appliance_ip>`. This interface is at the same time the main administration interface for you cloud infrastructure, and consumer interface for the final users of the cloud.

Control Console
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :ref:`Control Console <control_console>` is a text based wizard accessible through the vCenter console to the vOneCloud appliance and has relevance in the bootstrap process and the configuration of the appliance