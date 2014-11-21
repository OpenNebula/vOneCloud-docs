.. _guest_contextualization:

=======================
Guest Contextualization
=======================

The information defined at the :ref:`VM Template building <build_template_context>` time is presented to the VM using the VMware VMCI channel. This information comes encoded in base64 can be gathered using the VMware Tools. 

In the current vOneCloud release guest contextualization packages are not available, thus the contextualization process needs to be manually build in each guest image.

In Linux guests, the information can be consumed using the following command (and acted accordingly):

.. code::

   $ vmtoolsd --cmd 'info-get guestinfo.opennebula.context' | base64 -d
   MYSQLPASSWORD="MyPassword"
   ENABLEWORDPRESS="YES"
