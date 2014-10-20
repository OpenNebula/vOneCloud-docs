.. _multi_vm_applications:

=====================
Multi VM Applications
=====================

vOneCloud enables the management of individual VMs lifecycle, but it also enables the management of sets of VMs (services) through the `OneFlow component <http://docs.opennebula.org/4.10/advanced_administration/application_flow_and_auto-scaling/oneapps_overview.html>`__. vOneCloud ships with a configured and running OneFlow, ready to manage services.

OneFlow allows users and administrators to define, execute and manage multi-tiered applications, or services composed of interconnected VMs with deployment dependencies between them. Each group of VMs is deployed and managed as a single entity.

You can learn how to manage multi-tier applications in `this guide <http://docs.opennebula.org/4.10/advanced_administration/application_flow_and_auto-scaling/appflow_use_cli.html>`__.

Moreover, `elasticity <http://docs.opennebula.org/4.10/advanced_administration/application_flow_and_auto-scaling/appflow_use_cli.html#elasticity>`__ of each service can be defined in relation with chosen Key Performance Indicators, either as reported by the hypervisor or by the service itself through the `OneGate component <http://docs.opennebula.org/4.10/advanced_administration/application_insight/onegate_overview.html>`__.

