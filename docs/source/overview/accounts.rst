.. _accounts:

================================================================================
Accounts
================================================================================

The vOneCloud platform ships with several pre-created user accounts which will be described in this section:

+------------+-------------------------+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|  Account   |        Interface        |                Role               |                                                                                            Description                                                                                             |
+============+=========================+===================================+====================================================================================================================================================================================================+
| root       | linux                   | Appliance administrator           | This user can log into the appliance (local login, no SSH).                                                                                                                                        |
+------------+-------------------------+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| oneadmin   | vOneCloud Control Panel | vOneCloud Appliance administrator | Used to configure several aspects of the vOneCloud Appliance infrastructure: OpenNebula services, automatic upgrades, and drivers configuration (hybrid drivers and Active Directory integration). |
+------------+-------------------------+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| CloudAdmin | OpenNebula (Sunstone)   | Cloud Administrator               | Cloud Administrator. Run any task in OpenNebula, including creating other users.                                                                                                                   |
+------------+-------------------------+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Different :ref:`cloud roles <users_and_roles>` can be used in order to offer and consume cloud provisioning services in Sunstone (vOneCloud Web UI). These roles can be defined through Sunstone, and in particular CloudAdmin comes preconfigured as the Cloud Administrator.

`root` linux account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

vOneCloud runs on top of Linux (in particular `CentOS 7 <http://www.centos.org/>`), therefore the administrators of the vOneCloud appliance should be able to have console access to the appliance. The appliance comes with a `root` account with an undefined password. This password **must** be set during the first boot of the appliance. The :ref:`vOneCloud Control Console <control_console>` will prompt the administrator for a new root password.

Please note that ssh acccess to the root account is disabled by default in the appliance, the only possible way of logging in, is to log in using an alternate TTY in the vCenter console of the vOneCloud appliance and logging in.

.. note::

    Console access to the appliance is not required by vOneCloud. Use it only under special circumstances. If you are a user with an active support subscription, make sure any changes applied in the appliance are supported by the vOneCloud support.

`oneadmin` account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The main use of this account is to access the vOneCloud Control Panel (http://<appliance_ip>:8000). Only this account will have access to the Control Panel, no other user will be allowed to log in.

However, the `oneadmin` account is also a valid Sunstone account, but we **strongly recommend not to use this account to access the Sunstone Web UI**, relying instead in the pre-existing `CloudAdmin` account (see below).

The `oneadmin` account password is set by the admin user during the initial configuration of the vOneCloud Control Console. The **password can only be changed in the vOneCloud Control Console**. After changing it the user **must** restart the OpenNebula service in the :ref:`vOneCloud Control Panel <control_panel>`.

`CloudAdmin` OpenNebula (Sunstone) account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This account is used to log into Sunstone. It is a Cloud Administrator account, capable of running any task within OpenNebula, however, since this account cannot log into the vOneCloud Control Panel, it cannot control Appliance infrastructure, only the virtual resources.

This account should also be used to create other accounts within Sunstone, either with the same level of privileges (by placing a new account in the `oneadmin` group) or final user without admin privileges. These final users can either be :ref:`VDCadmins or cloud consumers <vdc_management>`.

The default password for this account is `CloudAdmin` (just like the username). Make sure you change the password within Sunstone once you log in.
