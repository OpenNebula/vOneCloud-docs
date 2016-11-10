.. _introduction_gc:

============
Introduction
============

vOneCloud will use pre configured vCenter VM Templates, which leverages the functionality provided by vCenter to build such templates. Additionally, vOneCloud provides functionality to tailor the VM guest Operating System to adjust it for the end user needs. OpenNebula provides two mechanisms to configure the newly created VMs.

* OpenNebula Contextualization: It allows configuration and information sharing between the vOneCloud interface and the Virtual Machine. This methods needs to build a a template for contextualization and to prepare the :onedoc:`guest OS <operation/vm_setup/vcenter.html?#vcenter-contextualization>`.
* :ref:`vCenter Customization Specifications <vcenter_customization>`: It ties the template with a vCenter Customization Specification so it is configured on VM creation

.. warning:: These options can not be used together. A template can use either OpenNebula Contextualization or vCenter customization.

This section will instruct on the needed actions to be taken into account to build vOneCloud Templates to deliver cloud users with personalized and perfectly adjusted Virtual Machines.
