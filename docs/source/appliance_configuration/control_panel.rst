.. _control_panel:

================================================================================
Control Panel
================================================================================

This is a web based interface available at `http://<appliance_ip>:8000`. Handles many aspects of the vOneCloud platform configuration.

To log in the administrator will need the `oneadmin` account, which is set in the initial configuration of the Control Console.

The next section documents the available information and actions in this interface

Appliance Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the dashboard of the Control Panel you will be able to see the following information:

+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
|     Parameter     |                                                                        Description                                                                        |
+===================+===========================================================================================================================================================+
| UUID              | Each vOneCloud appliance has an automatically generated UUID used to identify it. This information is required by vOneCloud Support for paying customers. |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Installation Date | Records the date of the vOneCloud first deployment.                                                                                                       |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Version           | Active vOneCloud version                                                                                                                                  |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Upgrade Date      | Records the date of last vOneCloud upgrade.                                                                                                               |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

Additionally vOneCloud will report the subscription status:

* No subscription detected
* Active subscription
* Expired subscription

Configuration Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The configuration action handles the supported configuration of the vOneCloud appliance:

* Hybrid drivers (EC2, SoftLayer, Azure).
* Active Directory or LDAP integration.

If the configuration is changed while OpenNebula is running, it will need to be restarted. A warning will appear in the dashboard reminding the user to restart the OpenNebula service.

Service Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The OpenNebula services can be managed in the main dashboard: start, stop and restart.

Any of this actions will trigger one or more tasks. If one of this tasks fails, the user will be notified, and paying customers will be able to send the error report to the vOneCloud Support.

.. _control_panel_automatic_upgrades:

Automatic Upgrades
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When a new vOneCloud release is available for download users will be notified. Paying customers will be able to upgrade with a single click. In the main Dashboard area the user will be notified if there is a new release available. In that case the user will be able to click a button that will start the upgrade.



.. note::
    Before running an automatic upgrade users are recommend to create a vCenter snapshot of the vOneCloud appliance in order to revert back to it in case of failure.


