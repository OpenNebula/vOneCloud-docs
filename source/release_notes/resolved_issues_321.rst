.. _resolved_issues_in_3.2.1:

========================
Resolved Issues in 3.2.1
========================

vOneCloud 3.2.1 is a maintenance release with the following minor improvements:

- Order of elements in list API calls can be selected (ascending or descending).
- XMLRPC calls can report the client IP and PORT.
- New quotas for VMS allow you to configure limits for VMs “running”.
- The Virtual Machines that are associated to a Virtual Router have all actions allowed except nic-attach/dettach.

Also 3.2.1 features the following bugfixes:

- User quotas error.
- Migrate vCenter machines provide feedback to oned.
- Fixed problem migrating vCenter machines to a cluster with a lot of ESX.
- Improve feedback for ‘mode’ option in Sunstone server.
- Accounting data does not display.
- Spurios syntax help on onehost delete.
- No way for hide Lock/Unlock button for VM in Sunstone view.
- Update LDAP driver to use new escaping functionality (and issue).
- Start script base64 enconding fails when using non utf8 characters.
- Error when creating a vnet from Sunstone using advanced mode.
- Restricted attributes not enforced on attach disk operation.
- Improve the dialog when attach nic or instanciated vm in network tab.
- VNC on ESXi can Break Firewall.
- Slow monitoring of the live migrating VMs on destination host.
- onehost sync should ignore vCenter hosts.
- NIC Model is ignored on VM vCenter Template.
- Unable to query VMs with non ASCII character.
- vCenter unimported resources cache not working as expected.
- Wild importation from vCenter host refactor.
- Removing CD-ROM from vCenter imported template breaks the template.
- Error with restricted attributes when instantiating a VM.
- Onevcenter cli tool few improvements and examples added.
- OPENNEBULA_MANAGED deleted when updating a VM Template.
- Unable to update the Running Memory quota.
- Monitoring VMs fails when there is not datastore associated.
