.. _accounts:

================================================================================
Accounts
================================================================================

vOneCloud ships with several pre-created user accounts which will be described in this section:

+----------+-----------------------+-------------------------+----------------------------------------------------------------------------------+
| Account  |       Interface       |           Role          |                                   Description                                    |
+==========+=======================+=========================+==================================================================================+
| root     | linux                 | Appliance administrator | This user can log into the appliance (local login, no SSH).                      |
+----------+-----------------------+-------------------------+----------------------------------------------------------------------------------+
| oneadmin | linux                 | Service user            | Used to run all OpenNebula services.                                              |
+----------+-----------------------+-------------------------+----------------------------------------------------------------------------------+
| oneadmin | OpenNebula Sunstone   | Cloud Administrator     | Cloud Administrator. Run any task in OpenNebula, including creating other users. |
+----------+-----------------------+-------------------------+----------------------------------------------------------------------------------+

`root` linux account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

vOneCloud runs on top of Linux (in particular `CentOS 8 <http://www.centos.org/>`__), therefore the administrators of the vOneCloud appliance should be able to have console access to the appliance. The appliance comes with a `root` account with an undefined password. This password **must** be set during the first boot of the appliance. The :ref:`vOneCloud Control Console <control_console>` will prompt the administrator for a new root password.

`oneadmin` linux account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The main use of this account is to run all OpenNebula services.

`oneadmin` OpenNebula (Sunstone) account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This account is used to log into Sunstone. It is a Cloud Administrator account, capable of running any task within OpenNebula. This account should be used to create other accounts within Sunstone, either with the same level of privileges (by placing a new account in the `oneadmin` group) or final user without admin privileges. This password **must** be set during the first boot of the appliance. The :ref:`vOneCloud Control Console <control_console>` will prompt the administrator for a new oneadmin password.
