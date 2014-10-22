.. _multi_vm_applications:

=====================
Multi VM Applications
=====================

vOneCloud enables the management of individual VMs, but also the management of sets of VMs (services) through the OneFlow component. 

vOneCloud ships with a running OneFlow, ready to manage services, allowing administrators to define multi-tiered applications using the vCenter View:

.. image:: /images/oneflow_vcenter_view.png
    :align: center

End users can consume services from the Cloud View:

.. image:: /images/oneflow_cloud_view.png
    :align: center

`Elasticity <http://docs.opennebula.org/4.10/advanced_administration/application_flow_and_auto-scaling/appflow_use_cli.html#elasticity>`__ of each service can be defined in relation with chosen Key Performance Indicators, either as reported by the hypervisor or by the service itself through the `OneGate component <http://docs.opennebula.org/4.10/advanced_administration/application_insight/onegate_overview.html>`__.

More information on this component in the `OneFlow guide <http://docs.opennebula.org/4.10/advanced_administration/application_flow_and_auto-scaling/oneapps_overview.html>`__. Also, extended information on how to manage multi-tier applications in `this guide <http://docs.opennebula.org/4.10/advanced_administration/application_flow_and_auto-scaling/appflow_use_cli.html>`__.
