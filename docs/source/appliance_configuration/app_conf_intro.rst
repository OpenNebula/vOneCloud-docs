.. _app_conf_intro:

================================================================================
Introduction
================================================================================

The vOneCloud appliance features a Control Center to simplify the configuration tasks needed to set-up, configure, maintain and upgrade the cloud. This Control Center is divided in two components:

**Control Console**

Text-based interface available in the appliance console in vCenter. Handles initial configuration of the appliance and basic configuration at any given time.

* Networking configuration.
* Proxy configuration.
* Sets main user account passwords.

.. image:: /images/control-console.png
    :align: center

**Control Center**


Web based interface available at `http://<appliance_ip>:8000`. Handles many aspects of the vOneCloud platform configuration.

* Handles OpenNebula services (start/stop/restart).
* Infrastructure Configuration Management:

  * Hybrid drivers (EC2, SoftLayer, Azure).
  * Active Directory or LDAP integration.

* Handles automatic upgrades of the whole vOneCloud platform. [#automatic_upgrades]_

.. image:: /images/control-center.png
    :align: center

.. [#automatic_upgrades] Automatic upgrades are only available to paying customers.


