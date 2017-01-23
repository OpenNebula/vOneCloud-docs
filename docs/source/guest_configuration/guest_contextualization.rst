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
* **Windows** >= 7
* **Windows Server** >= 2008

If you already happen to have a VM or Template in vCenter with the installed OS you can start it and prepare it to be used with vOneCloud. Alternatively you can start an installation process with the OS media.


Step 2. Download Contextualization Packages to the VM
-----------------------------------------------------

CentOS/RHEL
~~~~~~~~~~~

.. code::

    # wget https://github.com/OpenNebula/addon-context-linux/releases/download/v5.0.3/one-context_5.0.3.rpm

Debian/Ubuntu
~~~~~~~~~~~~~

.. code::

    # wget https://github.com/OpenNebula/addon-context-linux/releases/download/v5.0.3/one-context_5.0.3.deb

Windows
~~~~~~~

Download and install the MSI package (preferred way) into ``C:\``:
https://github.com/OpenNebula/addon-context-windows/releases/download/v5.2.0/one-context-5.2.0.msi

Or download particular contextualization scripts to ``C:\``:

* https://raw.githubusercontent.com/OpenNebula/addon-context-windows/v5.2.0/context.ps1
* https://raw.githubusercontent.com/OpenNebula/addon-context-windows/v5.2.0/startup.vbs

Step 3. Install Contextualization Packages and Dependencies
-----------------------------------------------------------

CentOS/RHEL 6
~~~~~~~~~~~~~

.. code::

    # rpm -Uvh one-context*rpm
    # yum install -y epel-release
    # yum install ruby # only needed for onegate command
    # yum install -i dracut-modules-growroot
    # dracut -f

CentOS/RHEL 7
~~~~~~~~~~~~~

.. code::

    # rpm -Uvh one-context*rpm
    # yum install -y epel-release
    # yum install ruby # only needed for onegate command
    # yum install -y cloud-utils-growpart

Debian/Ubuntu
~~~~~~~~~~~~~

.. code::

    # dpkg -i one-context*deb
    # apt-get install ruby # only needed for onegate command
    # apt-get install -y cloud-utils

Windows
~~~~~~~

* Open the Local Group Policy Dialog by running ``gpedit.msc``.
* Go to *Computer Configuration* -> *Windows Settings* -> *Scripts* -> *startup* (right click).
* Browse to the ``startup.vbs`` file and enable it as a startup script.

Step 4. Install VMware Tools
----------------------------

CentOS
~~~~~~

.. code::

    # yum install open-vm-tools

Debian/Ubuntu
~~~~~~~~~~~~~

.. code::

    # apt-get install open-vm-tools

Windows
~~~~~~~

In vCenter open the VM menu, go to "Guest OS" section, click in "Install VMware Tools..." and follow the instructions.

Step 5. Power Off the Machine and Save it
-----------------------------------------

These are the steps needed to finish the preparation and import it to OpenNebula:

* Power off the machine so it is in a consistent state the next time it boots
* Make sure that you take out any installation media used in the previous steps
* Remove the network interfaces from the VM
* Convert the VM into a Template
* Import the template in OpenNebula

Alternatively use the :ref:`instantiate as persistent <instantiate_to_persistent>` functionality for this step, that will create the new VM Template as soon as you terminate the VM.
