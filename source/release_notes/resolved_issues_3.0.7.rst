.. _resolved_issues_in_3.0.7:

========================
Resolved Issues in 3.0.7
========================

vOneCloud 3.0.7 is a maintenance release with the following minor improvements:

- Better updateconf, check VM state to allocate a new cluster VNC port
- Better timeouts for xml-rpc clients
- Fix history records when VMs are imported in POWEROFF state
- Changed cpu mode and fallback
- Filter in CLI commands now accept != operator
- Improved Sunstone text fields

Also 3.0.7 feature the following bugfixes:

- vCenter driver is capable of import network names with slashes
- Fix check in updateconf for non-running VMs
- Changing overcommitment on a host updates other hosts too
- Fixed bug with updateconf and vnc port
- Sunstone reloads the page with a group change of a user
- Memory overcommitment doesn't support float values
- Changes in VM Template not saved during update
- Rollback datastore quotas. Add datastore quotas to one.vmtemplate.instantiate
- Disk SIZE is not a valid integer
- Do not reset resizes and quotas after a recover --recreate
- AR size change in reservations should be disabled in Sunstone
- Multiple DISK attributes into VM Template section
- VM created w/ wrong disk size (size on instantiate)
- Error in group create/update
- ActionManager threads counter not decreased
- Groups shouldn't be cached in Sunstone
