.. _download_and_deploy:

================================================================================
Download and Deploy
================================================================================

vOneCloud can be downloaded by completing the form `here <http://downloads.vonecloud.com>`__.

The OVA can be imported in an existing vCenter infrastructure. It is based on `CentOS 8 <http://www.centos.org/>`__ and has VMware tools enabled.

The appliance requirements are kept to a strict minimum so it can be executed in any vCenter installation. However, before deploying it, please read the :ref:`system requirements <requirements>`.

Follow the next steps to deploy a fully functional OpenNebula cloud.

Step 1. Deploying the OVA
--------------------------------------------------------------------------------

Login to your vCenter installation and select the appropriate datacenter and cluster where you want to deploy the appliance. Select ``Deploy OVF Template``.

.. image:: /images/vOneCloud-download-deploy-001.png
    :align: center

You have the option now to browse to the download path of the OVA that can be downloaded from the link above:

.. image:: /images/vOneCloud-download-deploy-001a.png
    :align: center

.. image:: /images/vOneCloud-download-deploy-002.png
    :align: center

Select the name and folder:

.. image:: /images/vOneCloud-download-deploy-003.png
    :align: center

Select a resource to run the appliance:

.. image:: /images/vOneCloud-download-deploy-004.png
    :align: center

Review details:

.. image:: /images/vOneCloud-download-deploy-004b.png

Select the datastore:

.. image:: /images/vOneCloud-download-deploy-005.png
    :align: center

Select the Network. You will need to choose a network that has access to the ESX hosts.

.. image:: /images/vOneCloud-download-deploy-006.png
    :align: center

Review the settings selection and click finish. Wait for the Virtual Machine to appear in the cluster.

.. image:: /images/vOneCloud-download-deploy-007.png
    :align: center

After importing the vOneCloud OVA, and before powering it on, the vOneCloud Virtual Machine can be edited to, for instance, add a new network interface, increase the amount of RAM, the available CPUs for performance, etc.

In order to achieve this, please right click on the vOneCloud VM, and select Edit Settings. The next dialog should pop up:

.. image:: /images/edit-settings.png
    :align: center

If you want for instance to add a new network interface, select Network from the drop-down in New device (at the bottom of the dialog):

.. image:: /images/add-nic.png
    :align: center

Now you can power on the Virtual Machine.

.. image:: /images/vOneCloud-download-deploy-008.png
    :align: center

.. _download_and_deploy_control_console:

Step 2. vOneCloud Control Console - Initial Configuration
--------------------------------------------------------------------------------

When the VM boots up you will see in the VM console in vCenter the :ref:`vOneCloud Control Console <control_console>`, showing this wizard:

.. image:: /images/control-console.png
    :align: center

If you are presented instead with the following:

.. image:: /images/control-console-wrong.png
    :align: center

You are being presented with the wrong tty. You will need to press Ctrl+Alt+F1 to access the Control Console.

In this wizard you need to **configure the network**. If you are using DHCP you can simply skip to the next item.

If you are using a static network configuration, answer yes and you will need to use a ncurses interface to:

- "Edit a connection"
- Select "System eth0"
- Change IPv4 CONFIGURATION from <Automatic> to <Manual> and select "Show"
- Input the desired IP address/24 in Addresses
- Input Gateway and DNS Servers
- Select OK and then quit the dialog

An example of static network configuration on the available network interface on the 10.0.1.x class C network, with a gateway in 10.0.1.1 and using 8.8.8.8 as the DNS server:

.. image:: /images/network-conf-example.png
    :align: center

The second action is the **oneadmin account password**. You will need this to login to OpenNebula. Check the :ref:`Accounts section <accounts>` to learn more about vOneCloud roles and users.

.. image:: /images/set_oneadmin_password.png
    :align: center

And the in the third action, you need to define a **root password.** You won't be using this very often, so write it down somewhere safe. It's your master password to the appliance.

.. image:: /images/set_root_password.png
    :align: center

Step 3. Enjoy the Out-of-the-Box Features
--------------------------------------------------------------------------------

After opening the Sunstone interface (``http://<appliance_ip>`` with oneadmin credentials) you are now ready to enjoy the out-of-the-box features of OpenNebula!

.. image:: /images/sunstone-login.png
    :align: center

.. image:: /images/sunstone-main.png
    :align: center

Move on to the :ref:`next section <import_vcenter>` to start using your cloud by importing your existing vCenter infrastructure resources.

.. _advanced_login:

Login to the Appliance
--------------------------------------------------------------------------------

To access the OpenNebula command line interface, ssh to vOneCloud using the `root` account and password. In OS X and Linux environments, simply use `ssh` to log into the root account of vOneCloud's IP. For Windows environments you can use software like `PuTTY <http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html>`__ or even SFTP clients like `WinSCP <https://winscp.net/>`__.

Alternatively,  open the vCenter console of the vOneCloud Virtual Machine appliance and change the tty (Ctrl + Alt + F2). Afterwards, log in with the `root` account and the password you used in the :ref:`initial configuration <download_and_deploy_control_console>`, and switch to the `oneadmin` user.
