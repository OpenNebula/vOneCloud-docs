.. _guest_contextualization:

=======================
Guest Contextualization
=======================

The information defined at the :ref:`VM Template building <build_template_context>` time is presented to the VM using the VMware VMCI channel. This information comes encoded in base64 can be gathered using the VMware Tools.

Packages for Linux and Windows exist that can collect this data and configure some parameters.

+--------------------+---------------------------------------------------------+
|     Parameter      |                       Description                       |
+====================+=========================================================+
| ``SET_HOST``       | Change the hostname of the VM. In Windows the machine   |
|                    | needs to be restarted.                                  |
+--------------------+---------------------------------------------------------+
| ``SSH_PUBLIC_KEY`` | SSH public keys to add to authorized_keys file.         |
|                    | This parameter only works with Linux guests.            |
+--------------------+---------------------------------------------------------+
| ``USERNAME``       | Create a new administrator user with the given          |
|                    | user name. Only for Windows guests.                     |
+--------------------+---------------------------------------------------------+
| ``PASSWORD``       | Password for the new administrator user. Used with      |
|                    | ``USERNAME`` and only for Windows guests.               |
+--------------------+---------------------------------------------------------+
| ``DNS``            | Add DNS entries to ``resolv.conf`` file. Only for Linux |
|                    | guests.                                                 |
+--------------------+---------------------------------------------------------+
| ``NETWORK``        | If set to "YES" vOneCloud will pass Networking          |
|                    | for the different NICs onto the VM                      |
+--------------------+---------------------------------------------------------+

In Linux guests, the information can be consumed using the following command (and acted accordingly):

.. code::

   $ vmtoolsd --cmd 'info-get guestinfo.opennebula.context' | base64 -d
   MYSQLPASSWORD = 'MyPassword'
   ENABLEWORDPRESS = 'YES'


Linux Packages
==============

The linux packages can be downloaded from its `project page <https://github.com/OpenNebula/addon-context-linux/releases/tag/v4.8.1>`__ and installed in the guest OS. There is one rpm file for Debian and Ubuntu and an rpm for RHEL and CentOS. After installing the package shutdown the machine and create a new template.


Windows Package
===============

The official `addon-opennebula-context <https://github.com/OpenNebula/addon-context-windows>`__ provides all the necessary files to run the contextualization in Windows 2008 R2.

The contextualization procedure is as follows:

1. Download ``startup.vbs`` and ``context.ps1`` to the Windows VM and save them in ``C:\``.
2. Open the Local Group Policy Dialog by running ``gpedit.msc``. Under: Computer Configuration -> Windows Settings -> Scripts -> startup (right click); browse to the ``startup.vbs`` file and enable it as a startup script.

After that power off the VM and create a new template from it.
