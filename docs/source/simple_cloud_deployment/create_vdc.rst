.. _create_vdc:

===========================
Create a Virtual Datacenter
===========================

The provisioning model by default in vOneCloud is based on three different :ref:`roles <user_groups>` using three different web :ref:`interfaces <interfaces>`.

*vOneCloud* user comes preconfigured and is the **cloud administrator**, in full control of all the physical and virtual resources and using the vCenter view.

The whole cloud can be divided in isolated partitions, called Virtual Datacenters, or VDCs. A VDC is defined as a group of users allowed to use a set of physical hosts and their associated resources, in a transparent way. A **VDC Admin** manages her partition of the cloud, including user management, but only within her VDC, not for the whole cloud like the **cloud administrator**.

Let's create a VDC *Production* with an administrator called **vdcadmin**:

.. image:: /images/create_vdc_adminview.png
    :align: center

In the *Resources* tab you can chose which physical resources are assigned to the VDC. By default it will use all the available resources.

Now login again using this newly created **vdcadmin**. The VDC Admin view will kick in. Try it our creating the first *vdcuser* and assign them quotas on resource usage:

.. image:: /images/create_vdc_vdcview.png
    :align: center

As *vOneCloud* user, in the vCenter View, you can assign a VM Template to this VDC:

.. image:: /images/create_vdc_change_template.png
    :align: center

If you log with *vdcuser*, the view will change to the Cloud View, designed for end user, where **vdcuser** can start consuming VMs based on the VM Template shared by the **cloud administrator** and allowed by the **vdcadmin**:

.. image:: /images/create_vdc_cloudview.png
    :align: center

Read more about `VDC managing <http://docs.opennebula.org/4.10/administration/users_and_groups/manage_groups.html#managing-vdc-and-virtual-resources>`__.
