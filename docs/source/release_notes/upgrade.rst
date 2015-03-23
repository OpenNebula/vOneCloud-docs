.. _upgrade:

=======
Upgrade
=======

Upgrading to a newer version of vOneCloud is only supported for users with an `active support subscription <http://vonecloud.today/#support>`__. The upgrade process is carried out in the :ref:`Control Panel web interface <control_panel>`. 

When a new vOneCloud release is available for download, users with an active support subscription will be notified in the Sunstone interface (in particular, in the Control Panel link), as well as in the main Dashboard area of the Control Panel, and will be able to upgrade with a single click. The Control Panel component will, behind the scenes:

- download the new vOneCloud packages
- install the new vOneCloud packages, keeping the existing configuration 
- restart the OpenNebula service, with no downtime whatsoever to the currently running virtual machines. 

The Control Panel will display a message after the upgrade is performed, at this moment vOneCloud services would be up and running and updated to the latest version.
