.. _control_console:

================================================================================
Control Console
================================================================================

This is a text-based interface available used to run basic configuration tasks in the vOneCloud appliance.

.. image:: /images/control-console.png
    :align: center

The Control Console is available by opening the vOneCloud appliance console in vCenter. It requires no authentication since only the vCenter administrator will be able to open the vOneCloud console.

This component runs in two stages. The initial bootstrap stage, and the basic configuration stage.

.. _constrol_console_initial_bootstrap:

Initial Boostrap
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The initial bootstrap is a configuration wizard which is part of the deployment process of vOneCloud, and it **must** be run. During this step the user will be prompted to configure the following aspects:

* Configure Network
* Set the root password
* Change the password for oneadmin in OpenNebula
* Configure proxy

Once this wizard has been executed the user is ready to open the vOneCloud Control Panel at `http://<appliance_ip>:8000` in order to continue with the deployment configuration and to start the OpenNebula service.

Note that during this step the `oneadmin` account password will be set, which will be then used to access the vOneCloud Control Panel.

.. _control_console_basic_configuration:

Basic Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

At any given moment, the vOneCloud administrator may choose to open the vOneCloud appliance console in vCenter to perform some additional configuration:

* Networking configuration, which is useful if the networking configuration changes at any given time.
* Proxy configuration.
* Change the oneadmin password. Note that this step requires that the vOneCloud administrator restarts the OpenNebula service in the :ref:`vOneCloud Control Panel <control_panel>`.


