.. _build_template_context:

=========================================
Building a Template for Contextualization
=========================================

In order to pass information to the instantiated VM template, the Context section of the vOneCloud VM Template can be used. These templates can be updated in the Virtual Resources -> Templates tab of the vOneCloud GUI, and they can be updated regardless if they are :ref:`directly imported from vCenter <acquire_resources>` or :ref:`created through the vOneCloud Templates tab <add_new_vm_template>`.

.. note::

    Installing the Contextualization packages in the Virtual Machine image is required to pass this information to the instantiated VM template. Make sure you follow the :ref:`Guest Contextualization <guest_contextualization>` guide to properly prepare your VM templates.

.. image:: /images/vm_template_context.png
    :align: center

.. warning:: Passing files to VMs through contextualization is not supported

Different kinds of context information can be passed onto the VMs:

OneGate Token
-------------

vOneCloud has a centralized service to share data between Virtual Machines and the main daemon, useful to set monitoring information that can be gathered inside the VM and configuration data. It also lets you send scaling actions when the Virtual Machine belongs to a Service.

To do so the client installed with the contextualization packages (``onegate``) needs some information:

* **Token**: it's the key specific to each VM used to authenticate with the
  service
* **OneGate endpoint**: the address where the OneGate daemon is reachable

To fill this information you have to click the "Add OneGate token" check box.

Network Configuration
---------------------

vOneCloud does not rely on a DHCP server to configure networking in the Virtual Machines. To do this configuration it injects the network information in the contextualization section. This is done checking the "Add Network configuration" check box. When vOneCloud finds this option it adds the IP information for each of the network interfaces configured plus extra information that resides in the Virtual Network template, like DNS, gateway and network mask.

The parameters used from the Virtual Network template are explained in the OpenNebula documentation, :doc:`Managing Virtual Networks section <operation/network_management/manage_vnets.html#manage-vnets>`.

User Credentials
----------------

One of the other very important things you have to configure is user credentials to connect to the newly created Virtual Machine. 

For Linux base images we recommend to use SSH public key authentication and using it with vOneCloud is very convenient. The first thing the users should do its to add their SSH public key (or keys) to its vOneCloud user configuration, this can be done in the Settings section of the web interface. The Context section of the VM Template needs to have the "Add SSH contextualization" check box selected. Using this system the new Virtual Machines will be configured with the SSH public key of the user that instantiated it.

For Windows machines SSH is not available but you can use the options ``USERNAME`` and ``PASSWORD`` to create and set the password of an initial administrator, they can be set as :ref:`Custom Vars <custom_vars>`.

Execute Scripts on Boot
-----------------------

To be able to execute commands on boot, for example, to install some software, you can use the option ``Start script`` text area. When this option is used a new file that contains the value of the option will be created and executed.

For Windows machines this is a PowerShell script. For Linux machines this can be any scripting language as long as it is installed in the base image and the proper shebang line is set (shell scripts don't need shebang).

In this example some commands will be executed using ``bash`` shell that will install the package ``ntpdate`` and set the time.

.. code::

    #!/bin/bash
    yum update
    yum install -y ntpdate
    ntpdate 0.pool.ntp.org"

If you are using complex scripts, it is a good idea to use the "encode script in Base64" option.

Advanced Contextualization
--------------------------

There are more options that can be set in the contextualization section. You can read about them in the :doc:`Virtual Machine Definition File reference section <operation/references/template.html#template-context>`

User Inputs
-----------

These inputs are a special kind of contextualization that built into the templates. At instantiation time, the end user will be asked to fill in information for the defined inputs, and the answers will be packed and passed onto the VM.

For instance, vOneCloud administrator can build a VM Template that will ask for the MySQL password (the MySQL software will be configured at VM boot time and this password will be set) and for instance whether or not to enable WordPress:

.. image:: /images/admin_user_input.png
    :align: center

The end user will then be presented with the following form when instantiating the previously defined VM Template

.. image:: /images/end_user_input.png
    :align: center

.. _custom_vars:

Custom vars
-----------

These are personalized information to pass directly to the VM, in the form of Key - Value.

