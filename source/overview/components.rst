.. _components:

================================================================================
Components
================================================================================

This diagram reflects the relationship between the components that compose or interacts with vOneCloud.

.. image:: /images/vonecloud_components.png
    :align: center

vCenter Infrastructure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- vOneCloud is an appliance that is executed on vCenter. vOneCloud leverages this previously set up infrastructure composed of vCenter and ESX nodes.

OpenNebula
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- :onedoc:`OpenNebula <intro_release_notes/concepts_terminology/intro.html>` is a Cloud Management Platform responsible for managing your virtual vCenter resources and adding a Cloud layer on top of it.

- :onedoc:`Sunstone </deployment/sunstone_setup/index.html>` is the web-based graphical interface of OpenNebula. It is available at ``http://<appliance_ip>``. This interface is at the same time the main administration interface for th cloud infrastructure, and consumer interface for the final users of the cloud.

.. _control_console:

Control Console
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- The Control Console is a text based wizard accessible through the vCenter console to the vOneCloud appliance. It is available by opening the vOneCloud appliance console in vCenter. It requires no authentication since only the vCenter administrator will be able to open the vOneCloud console.

- It can be used to to configure the network, root password and change the password of the OpenNebula oneadmin user.