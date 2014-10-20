.. _limitations:

=====================
vOneCloud Limitations
=====================

vOneCloud delegates a number of aspects to vCenter, instead of pursuing the management of almost every aspect as it traditionally does. vOneCloud will use pre defined Virtual Machine Templates existing in the vCenter set up to launch Virtual Machines, very much like it does in its hybrid drivers to access Amazon EC2, IBM SoftLayer and Microsoft Azure, although offering extra features like for instance VNC support and more lifecycle actions. 

The following limitations come mainly from this approach, and they won't be presented to the end user.

....

**No Context**

Virtual Machines won’t have the ability of being contextualized, so CONTEXT sections of the VM Templates won’t be honored.

**VM Unsupported Operations**

The following operations are NOT supported on vCenter VMs managed by OpenNebula, although they can be perfomed through vCenter.

- Attach/detach disk to a running VM
- Attach/detach network interface to a running VM
- Migrate VM to different ESX clusters

**No Security Groups**

Firewall rules as defined in Security Groups cannot be enforced in vCenter VMs.

....

`Read more about the limitations of OpenNebula <http://docs.opennebula.org/4.10/administration/virtualization/vcenterg.html#considerations-limitations>`__ interacting with vCenter.