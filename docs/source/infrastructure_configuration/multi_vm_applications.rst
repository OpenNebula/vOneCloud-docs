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

:doc:`Elasticity <advanced_administration/application_flow_and_auto-scaling/appflow_use_cli.html#elasticity>` of each service can be defined in relation with chosen Key Performance Indicators as reported by the hypervisor.

.. note::

    vOneCloud does not include the ``onegate`` component which is mentioned at some places in the application flow guide.

More information on this component in the :doc:`OneFlow guide <advanced_administration/application_flow_and_auto-scaling/oneapps_overview.html>`. Also, extended information on how to manage multi-tier applications is available :doc:`this guide <advanced_administration/application_flow_and_auto-scaling/appflow_use_cli.html>`.

