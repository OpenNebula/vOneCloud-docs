.. _explore:

================================================================================
Explore OpenNebula Functionality
================================================================================

Now that you have and up and running OpenNebula installatoin thanks to the vOneCloud appliance, it is time to explore the cool features for Private Cloud that OpenNebula offers:


 - Self service portal for resource provisioning. OpenNebula's :onedoc:`Cloud View <operation/sunstone_enduser/cloud_view.html>` offers a powerful, easy to use point and click interface for cloud resource consumption and management.

 - OpenNebula offers a sofisticated :onedoc:`provisioning model <deployment/cloud_design/opennebula_provisioning_model.html>` enabling real world multi tenancy environments. This model is based on :onedoc:`groups of users <operation/users_groups_management/manage_groups.html>` and their belonging to :onedoc:`Virtual Datacenters <operation/users_groups_management/manage_vdcs.html>`.

 - Support for :onedoc:`application containerization <advanced_components/applications_containerization/index.html>`, automatic provisioning of docker hosts.

 - Multi-VMs applications can be orchestrated through :onedoc:`OneFlow <advanced_components/application_flow_and_auto-scaling/index.html>`.

 - Application insight can be extracted using :onedoc:`OneGate <advanced_components/application_insight/index.html>`, to create application aware elasticity rules

 - Access to a curated catalog of ready to use appliances, the `OpenNebula public marketplace <http://marketplace.opennebula.systems>`__, as well as the possiblity to create :onedoc:`private marketplaces <advanced_components/marketplace/index.html>`.

 - :onedoc:`NSX support <deployment/vmware_infrastructure_setup/nsx_setup.html>` to leverage the SDN capabilities. Both NSX-t and NSX-v are supported.

 - Different :onedoc:`authentication <deployment/authentication_setup/index.html>` backends other than the native OpenNebula authentication.

 - :onedoc:`Dissagregated Datacenters <advanced_components/ddc/index.html>`, the ability to grow the private cloud using the bare-metal offering of public cloud providers.

 - Rich :onedoc:`API <integration/system_interfaces/index.html>` with bindings for different languages: ruby, python, go...

 - Hybrid cloud drivers, to trasparently manage VMs in :onedoc:`Amazon EC2 <advanced_components/cloud_bursting/ec2g.html>` and :onedoc:`Microsoft Azure <advanced_components/cloud_bursting/azg.html>`.

 - Consumption control to limit the usage of the cloud, using :onedoc:`quotas <operation/users_groups_management/quota_auth.html>` with real time monitoring, :onedoc:`accounting <operation/users_groups_management/accounting.html>` and :onedoc:`showback <operation/users_groups_management/showback.html>`.

 - :onedoc:`Virtual Router <operation/network_management/vrouter.html>` with NFV capabilities.
