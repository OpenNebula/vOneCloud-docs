.. _download_and_deploy:

================================================================================
Download and Deploy
================================================================================

Download links:

- `vOneCloud-1.2.1.ova <http://downloads.vonecloud.com>`__ (md5sum: c4ca5770230d18be4dc8dd985c1c2d6f)

You can import this OVA appliance to your vCenter infrastructure. It is based on
`CentOS 7 <http://www.centos.org/>`__ and has the VMware tools enabled.

The appliance requirements are kept to a strict minimum so it can be executed in
any vCenter installation. However, before deploying it, please read the :ref:`system requirements <system_requirements>`.

Follow the next steps to deploy a fully functional vOneCloud:

Step 1. Deploying the OVA
--------------------------------------------------------------------------------

Login to your vCenter installation and select the appropriate datacenter and cluster, where you want to deploy the appliance. Select the ``Deploy OVF Template``.

.. image:: /images/vOneCloud-download-deploy-001.png
    :align: center

You have the option now to input the URL of the appliance (you can find it at the top of this page), or if you have previously downloaded it, you can simply browse to the download path as such:

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

Select the datastore:

.. image:: /images/vOneCloud-download-deploy-005.png
    :align: center

Select the Network. You will need to choose a network that has access to the ESX hosts.

.. image:: /images/vOneCloud-download-deploy-006.png
    :align: center

Review the settings selection and click finish. Wait for the Virtual Machine to appear in the cluster.

.. image:: /images/vOneCloud-download-deploy-007.png
    :align: center

Now you can power on the Virtual Machine:

.. image:: /images/vOneCloud-download-deploy-008.png
    :align: center

.. _download_and_deploy_control_console:

Step 2. vOneCloud Control Console - Initial Configuration
--------------------------------------------------------------------------------

When the VM boots up you will see in the vCenter console in vCenter the :ref:`vOneCloud Control Console <control_console>`, showing this wizard:

.. image:: /images/control-console.png
    :align: center

In this wizard you should **configure the network**. If you are using DHCP you can simply skip to the next item.

If you are using a static network configuration, answer yes and you will need to use a ncurses interface to:

- "Edit a connection"
- Select "Wirect connection 1"
- Change IPv4 CONFIGURATION from <Automatic> to <Manual> and select "Show"
- Input the desired IP address/24 in Addresses
- Input Gateway and DNS Servers
- Select OK and then quit the dialog.

Next, you can **configure the proxy** if your network topology requires a proxy to access the internet. However please note that it's absolutely fine to use vOneCloud without any internet access at all, as you will be able to do most of the things, except for automatic upgrades and hybrid cloud access.

Afterwards you need to define a **root password.** You won't be using this very often, so write it down somewhere safe. It's your master password to the appliance.

The next item is the **oneadmin account password**. You will only need this to login to the vOneCloud Control Panel, a web-based configuration interface we will see very shortly. Check the :ref:`Accounts section <accounts>` to learn more about vOneCloud roles and users.

We have now finished the vOneCloud Control Console initial configuration wizard. As the wizard itself will point out now you can open the vOneCloud Control Panel by pointing your browser to `http://<appliance_ip>:8000` and using the `oneadmin` account and password just chosen.

Step 3. vOneCloud Control Panel - Manage Services
--------------------------------------------------------------------------------

The :ref:`vOneCloud Control Panel <control_panel>` will allow the administrator to:

- Check for new vOneCloud versions and manage upgrades.
- Configure Active Directory / LDAP integration and hybrid cloud drivers: Amazon EC2, Windows Azure and IBM SoftLayer.
- Start the OpenNebula services
- Manage automatic upgrades.

Click on the configuration icon if you need to configure one of the supported options. Keep in mind that you can run this configuration at any moment. We recommend to start inspecting vOneCloud's functionality before delving into advanced configuration options like the aforementioned ones.

After clicking on the Start button, proceed to log in to Sunstone (OpenNebula's frontend) by opening: `http://<appliance_ip>` and using the default login `CloudAdmin` / `CloudAdmin` user and password.

.. note::

  There is a guide available that documents the configuration interfaces of the appliance :ref:`here <app_conf>`.

Step 4. Enjoy the Out-of-the-Box Features
--------------------------------------------------------------------------------

After opening the Sunstone interface (`http://<appliance_ip>` with `CloudAdmin` / `CloudAdmin` user and password) you are now ready to enjoy the :ref:`out-of-the-box features <features_outofthebox>` of vOneCloud!

Move on to the :ref:`next section <import_vcenter>` to start using your cloud by importing your vCenter infrastructure.

.. _advanced_login:

Login to the Appliance
--------------------------------------------------------------------------------

.. warning::
    If you make **any** changes to OpenNebula configuration files under ``/etc/one`` please note that they **will** be either discarded in the next upgrade, or overwritten by vOneCloud Control Center. Keep in mind that only those features configurable in Sunstone or in vOneCloud Control Console and Control Panel are officially supported. Any other customizations are not supported by `vOneCloud Support <http://vonecloud.today/#support>`__.

All the functionality you need to run your vOneCloud can be accessed via Sunstone, and all the support configuration parameters are available either in the :ref:`vOneCloud Control Console <control_console>` or in the :ref:`vOneCloud Control Panel <control_panel>`.

To access the :ref:`vOneCloud command line interface <cli_interface>` open the vCenter console of the vOneCloud Virtual Machine appliance and change the tty (Ctrl + Alt + F2). Afterwards, log in with the `root` account and the password you used in the :ref:`initial configuration <download_and_deploy_control_console>`, and switch to the `oneadmin` user.
