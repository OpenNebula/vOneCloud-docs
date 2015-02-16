.. _build_template_context:

========================================
Building a Template for Contextulization
========================================

In order to pass information to the instantiated VM template, the Context section of the vOneCloudVM Template can be used. These templates can be update in the Virtual Resources -> Templates tab of the vOneCloud GUI, and they can be updated regardless if they are :ref:`directly imported from vCenter <acquire_resources>` or :ref:`created through the vOneCloud Templates tab <add_new_vm_template>`.

.. image:: /images/vm_template_context.png
    :align: center

.. warning:: Passing files and network information to VMs through contextualization is currently not supported

Different kinds of context information can be passed onto the VMs:

Network & SSH
-------------

Networking information can be passed onto the VM, namely the information needed to correctly configure each one of the VM network interfaces.

You can add here an public keys that will be available in the VM at launch time to configure user access through SSH.

User Inputs
-----------

These inputs are a special kind of contextualization that built into the templates. At instantiation time, the end user will be asked to fill in information for the defined inputs, and the answers will be packed and passed onto the VM.

For instance, vOneCloud adminsitrator can build a VM Template that will ask for the MySQL password (the MySQL software will be configured at VM boot time and this password will be set) and for instance whether or not to enable WordPress:

.. image:: /images/admin_user_input.png
    :align: center

The end user will then be presented with the following form when instantiating the previously defined VM Template

.. image:: /images/end_user_input.png
    :align: center


Custom vars
-----------

These are personalized information to pass directly to the VM, in the form of Key - Value.
