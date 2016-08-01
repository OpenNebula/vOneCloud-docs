Resolved Issues in 2.0.1
================================================================================

vOneCloud 2.0.1 is based in OpenNebula 5.0.2 and as such it includes all the bug fixes and functionalities introduced in 5.0.2: `OpenNebula 5.0.2 Release Notes <http://docs.opennebula.org/5.0/intro_release_notes/release_notes/index.html>`__.

The following issues are noteworthy:

New functionality
--------------------------------------------------------------------------------

- `Resize capabilities for VR context <http://dev.opennebula.org/issues/4621>`__.
- `Modify cardinality of VR HA <http://dev.opennebula.org/issues/4597>`__.
- `Display colors for the labels <http://dev.opennebula.org/issues/4657>`__.
- `Search users by password field <http://dev.opennebula.org/issues/4614>`__.
- `Implement oneuser login in Sunstone <http://dev.opennebula.org/issues/4604>`__.
- `New action: VR Template instantiate <http://dev.opennebula.org/issues/4530>`__.
- `Service create dialog in admin view <http://dev.opennebula.org/issues/4348>`__.

Bug Fixes
--------------------------------------------------------------------------------

- `VM configuration tab can now be enabled in cloud view <http://dev.opennebula.org/issues/4626>`__.
- `Fix for VM modals in Cloud View <http://dev.opennebula.org/issues/4615>`__.
- `Fix for multiple value cluster attributes matching with automatically generated CLUSTER_ID <http://dev.opennebula.org/issues/4637>`__.
- `vCenter upload does not recognize new mime types <http://dev.opennebula.org/issues/4601>`__.
- `Service create and Service template instantiate repeat datatable IDs <http://dev.opennebula.org/issues/4664>`__.
- `VNet AR update does not select the right type <http://dev.opennebula.org/issues/4661>`__.
- `Sunstone session does not set zone_id <http://dev.opennebula.org/issues/4655>`__.
- `Changing owner or group of a service result in “Bad request” <http://dev.opennebula.org/issues/4653>`__.
- `groupadmin_vcenter view can't create new VMs <http://dev.opennebula.org/issues/4650>`__.
- `VM template delete dialog does not fill the selected res. names <http://dev.opennebula.org/issues/4646>`__.
- `Remove Save As Button from vCenter views <http://dev.opennebula.org/issues/4645>`__.
- `Labels container has style issues with a big number of labels, and long label names <http://dev.opennebula.org/issues/4641>`__.
- `Present VCPU and tie it to CPU in vCenter view  <http://dev.opennebula.org/issues/4638>`__.
- `MB/GB text overlaps select arrow  <http://dev.opennebula.org/issues/4629>`__.
- `Clone template modal does not have a close button  <http://dev.opennebula.org/issues/4625>`__.
- `Labels are not working for VR instances  <http://dev.opennebula.org/issues/4619>`__.
- `Auth_mad drivers are not listed in Sunstone <http://dev.opennebula.org/issues/4612>`__.
- `Attach nic modal disappear when selecting page 2 <http://dev.opennebula.org/issues/4606>`__.
- `Size column sorts alphabetically  <http://dev.opennebula.org/issues/4605>`__.
- `VM control operations are not visible when using firefox and sunstone in "dev" mode(while they are visible using chrome) <http://dev.opennebula.org/issues/4598>`__.
- `Strange behavior with capacity modification and unit switching <http://dev.opennebula.org/issues/4591>`__.
- `Confirmation dialogs cannot be submitted using the enter key <http://dev.opennebula.org/issues/3385>`__.
- `vCenter shutdown VM does not work if CDROM attached <http://dev.opennebula.org/issues/4608>`__.

Additionally, the following bug fixes have been applied on top of the fixes introduced by OpenNebula 5.0.2:

- `OneGate token is not being properly generated <http://dev.opennebula.org/issues/4696>`__.
- Add fallback for VM Template search in vCenter.
- Fix for CDROM detach.
