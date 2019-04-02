.. _guest_contextualization:

=======================
Guest Contextualization
=======================

The information defined at the :ref:`VM Template building <build_template_context>` time is presented to the VM using the VMware VMCI channel. This information comes encoded in base64 and can be gathered using the VMware Tools.

.. note:: VMware tools are needed in the guestOS to enable several features (contextualization and networking feedback). Please install `VMware Tools (for Windows) <https://www.vmware.com/support/ws55/doc/new_guest_tools_ws.html>`__ or `Open Virtual Machine Tools <https://github.com/vmware/open-vm-tools>`__ (for \*nix) in the guestOS.

In order to make your VMs aware of OpenNebula, you **must** install the :ref:`official packages <guest_contextualization_packages>`. Packages for both Linux and Windows exist that can collect this data and configure the supported parameters.

In Linux guests, the information can be consumed using the following command:

.. code::

   $ vmtoolsd --cmd 'info-get guestinfo.opennebula.context' | base64 -d
   MYSQLPASSWORD = 'MyPassword'
   ENABLEWORDPRESS = 'YES'

.. _guest_contextualization_packages:


The Linux packages can be downloaded from its `project page <https://github.com/OpenNebula/addon-context-linux/releases/tag/v5.0.0>`__ and the Windows one from its `project page <https://github.com/OpenNebula/addon-context-windows>`__. The steps to prepare a contextualized VM Template are:


Step 1. Start a VM with the OS you want to Customize
----------------------------------------------------

Supported contextualization packages are available for the following OS's:

* **CentOS/RHEL** >= 6
* **Debian** >= 6
* **Ubuntu** >= 11.10
* **Alpine Linux** >= 3.6, 3.7, 3.8
* **FreeBSD**, 11, 12
* **Windows** >= 7
* **Windows Server** >= 2008

If you already happen to have a VM or Template in vCenter with the installed OS you can start it and prepare it to be used with vOneCloud. Alternatively you can start an installation process with the OS media.


Step 2. Download Contextualization Packages to the VM
-----------------------------------------------------

CentOS/RHEL 6.x
~~~~~~~~~~~~~~~

.. code::

    # wget https://github.com/OpenNebula/addon-context-linux/releases/download/v5.8.0/one-context-5.8.0-1.el6.noarch.rpm

CentOS/RHEL 7.x
~~~~~~~~~~~~~~~

.. code::

    # wget https://github.com/OpenNebula/addon-context-linux/releases/download/v5.8.0/one-context-5.8.0-1.el7.noarch.rpm

OpenSUSE 42,15 / SLES 12
~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    # wget https://github.com/OpenNebula/addon-context-linux/releases/download/v5.8.0/one-context-5.8.0-1.suse.noarch.rpm

Debian/Ubuntu/Devuan
~~~~~~~~~~~~~~~~~~~~

.. code::

    # wget https://github.com/OpenNebula/addon-context-linux/releases/download/v5.8.0/one-context_5.8.0-1.deb

Alpine Linux
~~~~~~~~~~~~

.. code::

    # wget https://github.com/OpenNebula/addon-context-linux/releases/download/v5.8.0/one-context-5.8.0-r1.apk

Windows
~~~~~~~

Download and install the MSI package (preferred way) into ``C:\``:

.. code:: 
  
    https://github.com/OpenNebula/addon-context-windows/releases/download/v5.8.0/one-context-5.8.0.msi

Or execute this command in powershell:

.. code::

    (New-Object Net.WebClient).DownloadFile("https://github.com/OpenNebula/addon-context-windows/releases/download/v5.8.0/one-context-5.8.0.msi", "C:\one-context-5.8.0.msi")

Step 3. Install Contextualization Packages and Dependencies
-----------------------------------------------------------

CentOS/RHEL 6
~~~~~~~~~~~~~

.. code::

    # yum install -y epel-release
    # yum install -y one-context-[0-9]*el6*rpm

CentOS/RHEL 7
~~~~~~~~~~~~~

.. code::

    # yum install -y epel-release
    # yum install -y one-context-[0-9]*el7*rpm

OpenSUSE
~~~~~~~~

.. code::

    # zypper --no-gpg-check install -y one-context-[0-9]*suse*rpm

Debian/Ubuntu/Devuan
~~~~~~~~~~~~~~~~~~~~

.. code::

    # apt-get purge -y cloud-init
    # dpkg -i one-context_*deb || apt-get install -fy

Alpine Linux
~~~~~~~~~~~~

.. code::

    # apk add --allow-untrusted one-context-[0-9]*apk

Windows
~~~~~~~

* double-click on the downloaded MSI package icon in the same way you open other documents to install it
* execute ``sysprep`` to prepare the OS for duplication. You can find more information at:

https://technet.microsoft.com/en-us/library/cc721940(v=ws.10).aspx

Or for particular contextualization scripts:

* Open the Local Group Policy Dialog by running ``gpedit.msc``.
* Go to *Computer Configuration* -> *Windows Settings* -> *Scripts* -> *startup* (right click).
* Browse to the ``startup.vbs`` file and enable it as a startup script.

Step 4. Install VMware Tools
----------------------------

CentOS, Debian/Ubuntu
~~~~~~~~~~~~~~~~~~~~~

``open-vm-tools`` are installed as a dependency of contextualization package.

Windows
~~~~~~~

In vCenter open the VM menu, go to "Guest OS" section, click in "Install VMware Tools..." and follow the instructions.

Step 5. Power Off the Machine and Save it
-----------------------------------------

These are the steps needed to finish the process:

* Power off the machine so it is in a consistent state the next time it boots
* Click on the Save As Template button in the Cloud View

.. image:: /images/save_as_template.png
    :align: center

Alternatively use the :ref:`instantiate as persistent <instantiate_to_persistent>` functionality for this step, that will create the new VM Template as soon as you terminate the VM.
