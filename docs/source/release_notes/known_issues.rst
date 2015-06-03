.. _known_issues:

============================
Known Issues and Limitations
============================

Known Issues
================================================================================

These known issues will be addressed in future versions of vOneCloud.

Hybrid IP addresses not shown in Sunstone VM datatable
------------------------------------------------------

They are displayed in the info panel of the VM, which appears below the datatable after clicking the VM in the datatable

Error during upgrades if Proxy is configured
--------------------------------------------

There is a problem when upgrading from 1.2.x to 1.4.0 if proxy is configured that requires a manual intervention. Upgrade normally, and you will see that the start job has failed. Login to the vOneCloud console as explained :ref:`here <advanced_login>`, and execute the following commands:

.. code::

    echo export http_proxy=<yourproxy> > /etc/profile.d/proxy.sh
    source /etc/profile.d/proxy.sh
    gem install mysql --no-ri --no-rdoc
    sudo -u oneadmin onedb upgrade -u oneadmin -p oneadmin -d opennebula
    /usr/lib/one/vonecloud-control-center/scripts/opennebula-server.sh restart


Found more?
-----------

If you find any new issue, please let us know in the `Community Questions section of the vOneCloud Support Portal <https://support.vonecloud.com/hc/communities/public/questions>`__.

.. _limitations:

Limitations
================================================================================

These limitations will be addressed in future versions of vOneCloud:

+-------------------------------------+-----------------------------------------------------------------------------------------------------------------+
|            **Limitation**           |                                                 **Description**                                                 |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| **VM Unsupported Operations**       | The following operations are only supported from vCenter:                                                       |
|                                     | - Attach/detach disk to a running VM                                                                            |
|                                     | - Migrate VM to different ESX clusters                                                                          |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| **No MultivCenter Templates**       | vOneCloud Templates representing two or more vCenter VM                                                         |
|                                     | Templates cannot currently be defined.                                                                          |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| **No spaces in Clusters**           | VMware Clusters with space in their names are not supported                                                     |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| **No proxy support for SoftLayer**  | If vOneCloud is running behind a corporate http proxy, the SoftLayer hybrid connectors                          |
|                                     | won't be available                                                                                              |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| **No auth proxy support for Azure** | Azure driver only supports proxies without authentication. That is, without                                     |
|                                     | username and password.                                                                                          |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| **No FILES support in context**     | Contextualization in vOneCloud does not support passing files to Virtual Machines                               |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| **Cannot import "one-" VMs**        | VMs deployed by another instance of vOneCloud, or machines named with a leading "one-" cannot be imported again |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| **VM resize not supported**         | VMs cannot have CPU and Memory changed                                                                          |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------------+

If you find any new limitation, feel free to add a feature request in `Community - Feature Request section of the vOneCloud Support Portal <https://support.vonecloud.com/hc/communities/public/topics/200215442-Community-Feature-Requests>`__.
