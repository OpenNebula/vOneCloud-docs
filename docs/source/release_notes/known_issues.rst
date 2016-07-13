.. _known_issues:

============================
Known Issues and Limitations
============================

Known Issues
================================================================================

These known issues will be addressed in future versions of vOneCloud.

Error during upgrades if Proxy is configured
--------------------------------------------

There is a problem when upgrading from 1.2.x if proxy is configured that requires a manual intervention. Upgrade normally, and you will see that the start job has failed. Login to the vOneCloud console as explained :ref:`here <advanced_login>`, and execute the following commands:

.. code::

    echo export http_proxy=<yourproxy> > /etc/profile.d/proxy.sh
    source /etc/profile.d/proxy.sh
    gem install mysql --no-ri --no-rdoc
    sudo -u oneadmin onedb upgrade -u oneadmin -p oneadmin -d opennebula
    /usr/lib/one/vonecloud-control-center/scripts/opennebula-server.sh restart

Control Panel link not working with SSL activated
--------------------------------------------------------------------------------

Control Panel link in Sunstone is known not to work in SSL configurations. Please remove the 's' in 'https' in the URL in order to properly access the Control Panel.

Save As Template feature not working
--------------------------------------------------------------------------------

Save As Template button in the Cloud View triggers a feature that is not present in vOneCloud. The preferred way to create new templates is the "Instantiate to Persistent" button at instantiation time.

To disable this button, you need to `login <_advanced_login>` into the appliance and change line 57 of /etc/one/sunstone-views/cloud.yaml to read:

   VM.save_as_template: false

and restart OpenNebula through the Control Panel.

Found more?
-----------

If you find any new issue, please let us know in the `Community Questions section of the vOneCloud Support Portal <https://support.vonecloud.com/hc/communities/public/questions>`__.

.. _limitations:

Limitations
================================================================================

These limitations will be addressed in future versions of vOneCloud:

+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          **Limitation**         |                                                                       **Description**                                                                       |
+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **VM Unsupported Operations**   | The following operations are only supported from vCenter:                                                                                                   |
|                                 | - Migrate VM to different ESX clusters                                                                                                                      |
+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **No spaces in Clusters**       | VMware Clusters with space in their names are not supported                                                                                                 |
+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **No spaces in VMDKs**          | VMDKs with spaces in their names or paths (ie, folders that contain them) are not supported for importing, attaching or uploading                           |
+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **No spaces in Datastores**     | Datastore names cannot contain spaces to be managed from vOneCloud                                                                                          |
+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **No CDROM drive creation**     | Attaching a new CDROM ISO will add a new (or change the existing) ISO to an already existing CDROM drive that needs to be present in the VM                 |
+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **No FILES support in context** | Contextualization in vOneCloud does not support passing files to Virtual Machines                                                                           |
+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Cannot import "one-" VMs**    | VMs deployed by another instance of vOneCloud, or machines named with a leading "one-" cannot be imported again                                             |
+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **vCenter password length**     | Cannot be more than 22 characters                                                                                                                           |
+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Browser support**             | Internet Explorer (>= 9), Firefox (> 3.5) and Chrome browsers are supported. Other browsers, including Safari, are **not** supported and may not work well. |
+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Browser Adblock plug ins**    | Features like VNC and VM log viewer may be affected by Adblock plug ins. Please disable these plug ins if you are experiencing issues                       |
+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

If you find any new limitation, feel free to add a feature request in `Community - Feature Request section of the vOneCloud Support Portal <https://support.vonecloud.com/hc/communities/public/topics/200215442-Community-Feature-Requests>`__.
