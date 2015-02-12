.. _limitations:

=====================
vOneCloud Limitations
=====================

vOneCloud will use pre defined Templates existing in the vCenter to launch Virtual Machines. The following limitations apply:

+------------------------------------+----------------------------------------------------------------------------------------+
| **VM Unsupported Operations**      | The following operations are only supported from vCenter:                              |
|                                    |  - Attach/detach disk to a running VM                                                  |
|                                    |  - Migrate VM to different ESX clusters                                                |
+------------------------------------+----------------------------------------------------------------------------------------+
| **No MultivCenter Templates**      | vOneCloud Templates representing two or more vCenter VM                                |
|                                    | Templates cannot currently be defined.                                                 |
+------------------------------------+----------------------------------------------------------------------------------------+
| **No spaces in Clusters**          | VMware Clusters with space in their names are not supported                            |
+------------------------------------+----------------------------------------------------------------------------------------+
| **No proxy support for SoftLayer** | If vOneCloud is running behind a corporate http proxy, the SoftLayer hybrid connectors |
|                                    | won't be available                                                                     |
+------------------------------------+----------------------------------------------------------------------------------------+
| **No FILES support in context**    | Contextualization in vOneCloud does not support passing files to Virtual Machines      |
+------------------------------------+----------------------------------------------------------------------------------------+
| **No multi-VM app support**        | OneFlow component is not yet shipped with vOneCloud                                    |
+------------------------------------+----------------------------------------------------------------------------------------+

These limitations will be addressed in future versions of vOneCloud. 

If you find any new limitation, feel free to add a feature request in `Community - Feature Request section of the vOneCloud Support Portal <https://support.vonecloud.com/hc/communities/public/topics/200215442-Community-Feature-Requests>`__.