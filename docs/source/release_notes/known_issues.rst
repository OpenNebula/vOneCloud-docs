.. _known_issues:

============================
Known Issues and Limitations
============================

Known Issues
================================================================================

+------------------------------------------------------------+-----------------------------------------------------------------------------------+
| **Hybrid IP addresses not shown in Sunstone VM datatable** | They are displayed in the info panel of the VM, which appears below the datatable |
|                                                            | after clicking the VM in the datatable                                            |
+------------------------------------------------------------+-----------------------------------------------------------------------------------+
| **Running VMs are imported without VNC**                   | All running VMs are imported without VNC capabilities in vOneCloud, regardless of |
|                                                            | the availability of an open VNC port on said VMs                                  |
+------------------------------------------------------------+-----------------------------------------------------------------------------------+

These known issues will be addressed in future versions of vOneCloud.

If you find any new issue, please let us know in the `Community Questions section of the vOneCloud Support Portal <https://support.vonecloud.com/hc/communities/public/questions>`__.

.. _limitations:

vOneCloud Limitations
================================================================================

vOneCloud will use pre defined Templates existing in the vCenter to launch Virtual Machines. The following limitations apply:

+-------------------------------------+-----------------------------------------------------------------------------------------------------------------+
|            **Limitation**           |                                                 **Description**                                                 |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| **VM Unsupported Operations**       | The following operations are only supported from vCenter:                                                       |
|                                     |  - Attach/detach disk to a running VM                                                                           |
|                                     |  - Migrate VM to different ESX clusters                                                                         |
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
| **No multi-VM app support**         | OneFlow component is not yet shipped with vOneCloud                                                             |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| **Cannot import "one-" VMs**        | VMs deployed by another instance of vOneCloud, or machines named with a leading "one-" cannot be imported again |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------------+

These limitations will be addressed in future versions of vOneCloud.

If you find any new limitation, feel free to add a feature request in `Community - Feature Request section of the vOneCloud Support Portal <https://support.vonecloud.com/hc/communities/public/topics/200215442-Community-Feature-Requests>`__.
