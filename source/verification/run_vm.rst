.. _run_vm:

===================
Run Virtual Machine
===================

To run our first virtual machine, we stick with the easy-to-use Sunstone web UI.

In the left tab, click on ``Instances --> VMs`` to get a (currently empty) list of running virtual machines. Click on the plus button [+] to instantiate a new one.

.. image:: /images/run_vm_add.png
    :align: center

Select the imported VM Template, in this example here is a template called: "linuxTemplate". You can add/modify/remove network interfaces, from the template, before instantiate in the "Network" section below.

Click on the Create button to instantiate the virtual machine.

.. image:: /images/run_vm_create.png
    :align: center

Going back to the list of virtual machines in ``Instances --> VMs``, we can see our new machine. If the virtual machine is still not in RUNNING, click the button with refresh icon to reload the data.

.. image:: /images/run_vm_running.png
    :align: center

When the virtual machine is running, the "display" icon allows to open a graphical console.

.. image:: /images/run_vm_vnc.png
    :align: center
